"""SQLAlchemy 2.0 engine, session factory, and declarative Base used by all ORM models in this project."""
from __future__ import annotations

from collections.abc import Generator
from typing import Any

# Replaced with a real DeclarativeBase subclass in Phase 1.
Base: Any = None


def get_session() -> Generator[Any, None, None]:
    """Yield a SQLAlchemy 2.0 Session bound to the configured engine. Full implementation in Phase 1."""
    raise NotImplementedError
