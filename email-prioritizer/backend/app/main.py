"""FastAPI entrypoint — deploy to Render.

Endpoints:
  GET  /                  health/info
  GET  /api/demo          process the built-in sample inbox (no auth needed)
  POST /api/process       process a caller-supplied batch of emails
  POST /api/gmail/process fetch from Gmail with a client OAuth token, then process
"""
from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .gmail import fetch_messages
from .models import (
    GmailProcessRequest,
    ProcessRequest,
    ProcessResponse,
)
from .sample_data import SAMPLE_EMAILS
from .summarize import process_emails

settings = get_settings()
app = FastAPI(title="Email Prioritizer API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    return {
        "service": "email-prioritizer",
        "status": "ok",
        "llm_enabled": settings.llm_enabled,
        "model": settings.llm_model if settings.llm_enabled else None,
    }


@app.get("/api/demo", response_model=ProcessResponse)
def demo() -> ProcessResponse:
    processed, llm_used, model = process_emails(list(SAMPLE_EMAILS), settings)
    return ProcessResponse(emails=processed, llm_used=llm_used, model=model)


@app.post("/api/process", response_model=ProcessResponse)
def process(req: ProcessRequest) -> ProcessResponse:
    if not req.emails:
        raise HTTPException(status_code=400, detail="No emails provided.")
    processed, llm_used, model = process_emails(req.emails, settings)
    return ProcessResponse(emails=processed, llm_used=llm_used, model=model)


@app.post("/api/gmail/process", response_model=ProcessResponse)
def gmail_process(req: GmailProcessRequest) -> ProcessResponse:
    try:
        emails = fetch_messages(req.access_token, req.max_results, req.query)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=502, detail=f"Gmail fetch failed: {exc}") from exc
    if not emails:
        return ProcessResponse(emails=[], llm_used=False, model=None)
    processed, llm_used, model = process_emails(emails, settings)
    return ProcessResponse(emails=processed, llm_used=llm_used, model=model)
