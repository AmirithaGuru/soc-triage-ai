"""Shared pytest fixtures available to all test tiers: TestClient, mock alert payloads, and (later) test database session."""
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Return a FastAPI TestClient wrapping the application."""
    return TestClient(app)
