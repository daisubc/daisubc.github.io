"""Pydantic request/response schemas."""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

Priority = Literal["high", "medium", "low"]


class RawEmail(BaseModel):
    """An email as received from a client or the Gmail API, before processing."""

    id: str
    sender: str = ""
    subject: str = ""
    date: str = ""
    snippet: str = ""
    body: str = ""


class ProcessedEmail(BaseModel):
    """An email enriched with an LLM-generated summary and priority."""

    id: str
    sender: str
    subject: str
    date: str
    summary: str
    priority: Priority
    priority_score: int = Field(ge=0, le=100)
    category: str
    action_required: bool
    reason: str


class ProcessRequest(BaseModel):
    """Generic request: summarize/prioritize a batch of caller-provided emails."""

    emails: list[RawEmail]


class GmailProcessRequest(BaseModel):
    """Fetch from Gmail (using a client-obtained OAuth access token) then process."""

    access_token: str
    max_results: int = Field(default=15, ge=1, le=50)
    query: str = "in:inbox"


class ProcessResponse(BaseModel):
    emails: list[ProcessedEmail]
    llm_used: bool
    model: Optional[str] = None
