"""Fetch recent messages from the Gmail REST API.

The frontend obtains a short-lived OAuth access token (scope
gmail.readonly) via Google Identity Services in the browser, then sends it
here. This keeps the backend stateless: it never stores credentials.
"""
from __future__ import annotations

import base64
from typing import Any

import httpx

from .models import RawEmail

GMAIL_API = "https://gmail.googleapis.com/gmail/v1/users/me"


def _header(payload: dict[str, Any], name: str) -> str:
    for h in payload.get("headers", []):
        if h.get("name", "").lower() == name.lower():
            return h.get("value", "")
    return ""


def _decode_part(data: str) -> str:
    try:
        return base64.urlsafe_b64decode(data.encode("utf-8")).decode("utf-8", "replace")
    except Exception:  # noqa: BLE001
        return ""


def _extract_body(payload: dict[str, Any]) -> str:
    """Walk the MIME tree, preferring text/plain."""
    mime = payload.get("mimeType", "")
    body = payload.get("body", {})
    if mime == "text/plain" and body.get("data"):
        return _decode_part(body["data"])

    plain, html = "", ""
    for part in payload.get("parts", []) or []:
        sub = _extract_body(part)
        if part.get("mimeType") == "text/plain" and sub:
            plain += sub
        elif part.get("mimeType") == "text/html" and sub:
            html += sub
        elif sub:
            plain += sub
    if plain:
        return plain
    if html:  # crude tag strip as last resort
        import re

        return re.sub(r"<[^>]+>", " ", html)
    return ""


def fetch_messages(access_token: str, max_results: int, query: str) -> list[RawEmail]:
    headers = {"Authorization": f"Bearer {access_token}"}
    with httpx.Client(timeout=30) as client:
        listing = client.get(
            f"{GMAIL_API}/messages",
            headers=headers,
            params={"maxResults": max_results, "q": query},
        )
        listing.raise_for_status()
        ids = [m["id"] for m in listing.json().get("messages", [])]

        emails: list[RawEmail] = []
        for mid in ids:
            r = client.get(
                f"{GMAIL_API}/messages/{mid}",
                headers=headers,
                params={"format": "full"},
            )
            r.raise_for_status()
            msg = r.json()
            payload = msg.get("payload", {})
            emails.append(
                RawEmail(
                    id=mid,
                    sender=_header(payload, "From"),
                    subject=_header(payload, "Subject"),
                    date=_header(payload, "Date"),
                    snippet=msg.get("snippet", ""),
                    body=_extract_body(payload),
                )
            )
        return emails
