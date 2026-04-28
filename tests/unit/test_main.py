"""Unit tests for app/main.py: health endpoint response shape, stub route registration, and application startup."""
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Return a TestClient scoped to this module."""
    return TestClient(app)


def test_health_returns_200(client: TestClient) -> None:
    """GET /health must return HTTP 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_body_status_ok(client: TestClient) -> None:
    """GET /health body must contain status: ok."""
    response = client.get("/health")
    assert response.json()["status"] == "ok"


def test_health_body_service_name(client: TestClient) -> None:
    """GET /health body must contain the service name."""
    response = client.get("/health")
    assert response.json()["service"] == "soc-triage-ai"
