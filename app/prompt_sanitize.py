"""Sanitises raw alert fields before they are embedded in LLM prompts, defending against prompt injection attacks."""
from __future__ import annotations


def sanitize(alert_data: dict) -> dict:
    """Remove or escape prompt-injection patterns from alert field values. Implementation in Phase 2."""
    raise NotImplementedError
