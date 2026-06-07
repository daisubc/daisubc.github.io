"""FastAPI entrypoint.

Can run two ways:
  * API only (separate Vite dev server / Vercel)         — endpoints below.
  * Single-origin: also serves the built frontend at "/" — best for using the
    app from another device (e.g. an iPad) through one secure link.

Endpoints:
  GET  /api/health        health/info
  GET  /api/demo          process the built-in sample inbox (no auth needed)
  POST /api/process       process a caller-supplied batch of emails
  POST /api/gmail/process fetch from Gmail with a client OAuth token, then process
  GET  /                  the web app, if frontend/dist has been built
"""
from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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


@app.get("/api/health")
def health() -> dict:
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


# Serve the built frontend from the same origin, if it has been built.
# (API routes above are registered first, so they always take precedence.)
_FRONTEND_DIST = Path(__file__).resolve().parents[2] / "frontend" / "dist"
if _FRONTEND_DIST.is_dir():
    app.mount("/", StaticFiles(directory=str(_FRONTEND_DIST), html=True), name="web")
