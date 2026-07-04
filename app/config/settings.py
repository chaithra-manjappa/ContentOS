"""Application settings."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Application configuration."""

    groq_api_key: str
    groq_model: str

    @classmethod
    def from_environment(cls) -> "Settings":
        return cls(
            groq_api_key=os.getenv("GROQ_API_KEY", ""),
            groq_model=os.getenv(
                "GROQ_MODEL",
                "llama-3.3-70b-versatile",
            ),
        )