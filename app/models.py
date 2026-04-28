"""Pydantic v2 request/response schemas for all six API endpoints — the contract between clients and the SOC Triage AI service."""
from __future__ import annotations

from pydantic import BaseModel


class AlertIngest(BaseModel):
    """Incoming alert payload from Splunk or the simulator. Fields expanded in Phase 1."""


class TriageReport(BaseModel):
    """Enriched triage report returned to the analyst. Fields expanded in Phase 2."""


class AnalystFeedback(BaseModel):
    """Analyst confirm/dismiss decision payload. Fields expanded in Phase 1."""


class MetricsResponse(BaseModel):
    """Aggregated triage metrics response. Fields expanded in Phase 1."""
