"""Application configuration, loaded from environment variables.

All LLM settings target an OpenAI-compatible Chat Completions endpoint so the
app works with any open-source model host: Groq, Together, OpenRouter, a
self-hosted vLLM server, or a local Ollama instance.
"""
from __future__ import annotations

import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


class Settings:
    # --- LLM (OpenAI-compatible endpoint serving an open-source model) ---
    # Examples:
    #   Groq:     base_url=https://api.groq.com/openai/v1   model=llama-3.3-70b-versatile
    #   Together: base_url=https://api.together.xyz/v1      model=meta-llama/Llama-3.3-70B-Instruct-Turbo
    #   Ollama:   base_url=http://localhost:11434/v1        model=llama3.1
    llm_base_url: str = os.getenv("LLM_BASE_URL", "https://api.groq.com/openai/v1")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")
    llm_timeout: float = float(os.getenv("LLM_TIMEOUT", "60"))

    # --- CORS ---
    # Comma-separated list of allowed origins (your Vercel URL + localhost).
    allowed_origins: list[str] = [
        o.strip()
        for o in os.getenv(
            "ALLOWED_ORIGINS",
            "http://localhost:5173,http://127.0.0.1:5173",
        ).split(",")
        if o.strip()
    ]

    @property
    def llm_enabled(self) -> bool:
        # Local runtimes like Ollama don't need a key; remote hosts do.
        return bool(self.llm_api_key) or "localhost" in self.llm_base_url or "127.0.0.1" in self.llm_base_url


@lru_cache
def get_settings() -> Settings:
    return Settings()
