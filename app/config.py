"""Centralised settings loader: reads all environment variables via Pydantic BaseSettings and exposes a single Settings instance."""
from __future__ import annotations

from functools import lru_cache


class Settings:
    """Placeholder — full Pydantic BaseSettings implementation in Phase 1."""

    def __init__(self) -> None:
        pass


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached application settings. Implementation expanded in Phase 1."""
    return Settings()
