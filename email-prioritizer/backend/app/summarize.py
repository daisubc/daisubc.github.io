"""Summarize and prioritize emails.

Primary path: an open-source LLM via an OpenAI-compatible Chat Completions API.
Fallback path: a transparent rule-based heuristic so the app always works,
even with no model configured (used for local dev and the demo endpoint).
"""
from __future__ import annotations

import json
import re

from openai import OpenAI

from .config import Settings
from .models import ProcessedEmail, RawEmail

SYSTEM_PROMPT = """You are an assistant that triages a person's email inbox.
For each email you receive, produce a concise summary and assign a priority.

Priority guidance:
- high: time-sensitive, needs a personal reply/decision, from a real person about
  something important (deadlines, meetings, money, urgent requests, your boss).
- medium: useful and possibly actionable but not urgent (updates, FYIs, threads
  you're part of, scheduling that isn't imminent).
- low: newsletters, marketing, automated notifications, receipts, social updates.

Respond with STRICT JSON only, no prose, in exactly this shape:
{
  "summary": "<=2 sentence plain-language summary of what the email says/wants",
  "priority": "high" | "medium" | "low",
  "priority_score": <integer 0-100, higher = more important/urgent>,
  "category": "<short tag e.g. Meeting, Deadline, Newsletter, Receipt, Personal>",
  "action_required": <true|false>,
  "reason": "<short reason for the priority>"
}"""


def _truncate(text: str, limit: int = 4000) -> str:
    text = (text or "").strip()
    return text[:limit]


def _llm_process_one(client: OpenAI, model: str, email: RawEmail) -> ProcessedEmail:
    user_content = (
        f"From: {email.sender}\n"
        f"Subject: {email.subject}\n"
        f"Date: {email.date}\n\n"
        f"{_truncate(email.body or email.snippet)}"
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
        temperature=0.2,
        response_format={"type": "json_object"},
    )
    data = json.loads(resp.choices[0].message.content or "{}")
    priority = str(data.get("priority", "medium")).lower()
    if priority not in ("high", "medium", "low"):
        priority = "medium"
    score = data.get("priority_score", {"high": 80, "medium": 50, "low": 20}[priority])
    try:
        score = max(0, min(100, int(score)))
    except (TypeError, ValueError):
        score = {"high": 80, "medium": 50, "low": 20}[priority]

    return ProcessedEmail(
        id=email.id,
        sender=email.sender,
        subject=email.subject,
        date=email.date,
        summary=str(data.get("summary", "")).strip() or (email.snippet[:200]),
        priority=priority,
        priority_score=score,
        category=str(data.get("category", "General")).strip() or "General",
        action_required=bool(data.get("action_required", False)),
        reason=str(data.get("reason", "")).strip(),
    )


# --- Heuristic fallback -----------------------------------------------------

_HIGH_WORDS = re.compile(
    r"\b(urgent|asap|immediately|deadline|today|tomorrow|important|action required|"
    r"past due|overdue|final notice|interview|offer|invoice due|payment failed)\b",
    re.I,
)
_LOW_WORDS = re.compile(
    r"\b(newsletter|unsubscribe|sale|% off|promo|digest|no-?reply|notification|"
    r"weekly update|daily digest)\b",
    re.I,
)
_QUESTION = re.compile(r"\?|\bcan you\b|\bplease\b|\bcould you\b|\blet me know\b", re.I)


def _heuristic_process_one(email: RawEmail) -> ProcessedEmail:
    text = f"{email.subject}\n{email.body or email.snippet}"
    score = 50
    category = "General"
    if _LOW_WORDS.search(text) or re.search(r"no-?reply", email.sender, re.I):
        score -= 30
        category = "Newsletter/Notification"
    if _HIGH_WORDS.search(text):
        score += 35
        category = "Time-sensitive"
    action = bool(_QUESTION.search(text)) or _HIGH_WORDS.search(text) is not None
    if action:
        score += 10
    score = max(0, min(100, score))
    priority = "high" if score >= 70 else "low" if score <= 35 else "medium"

    raw = (email.body or email.snippet).strip()
    summary = re.sub(r"\s+", " ", raw)[:200] or "(no preview available)"

    return ProcessedEmail(
        id=email.id,
        sender=email.sender,
        subject=email.subject,
        date=email.date,
        summary=summary,
        priority=priority,
        priority_score=score,
        category=category,
        action_required=action,
        reason="Rule-based estimate (no LLM configured).",
    )


def process_emails(
    emails: list[RawEmail], settings: Settings
) -> tuple[list[ProcessedEmail], bool, str | None]:
    """Return (processed, llm_used, model_name). Falls back to heuristics on any error."""
    if settings.llm_enabled:
        try:
            client = OpenAI(
                base_url=settings.llm_base_url,
                api_key=settings.llm_api_key or "ollama",
                timeout=settings.llm_timeout,
            )
            processed = [_llm_process_one(client, settings.llm_model, e) for e in emails]
            processed.sort(key=lambda x: x.priority_score, reverse=True)
            return processed, True, settings.llm_model
        except Exception as exc:  # noqa: BLE001 - degrade gracefully, never 500 the user
            print(f"[summarize] LLM path failed, falling back to heuristics: {exc}")

    processed = [_heuristic_process_one(e) for e in emails]
    processed.sort(key=lambda x: x.priority_score, reverse=True)
    return processed, False, None
