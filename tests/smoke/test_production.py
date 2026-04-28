"""Smoke tests that run against a live deployment URL (skipped unless BASE_URL environment variable is set)."""
from __future__ import annotations

import os

import httpx
import pytest

BASE_URL: str = os.getenv("BASE_URL", "")


@pytest.mark.smoke
@pytest.mark.skipif(not BASE_URL, reason="BASE_URL not set — skipping smoke tests against live deployment")
def test_health_smoke() -> None:
    """GET /health must return HTTP 200 on the live deployment."""
    response = httpx.get(f"{BASE_URL}/health", timeout=10)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
