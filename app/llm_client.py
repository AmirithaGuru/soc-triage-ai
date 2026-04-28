"""OpenAI GPT-4o client wrapper with timeout handling and a rule-based fallback for when the LLM is unavailable."""
from __future__ import annotations


async def analyse_alert(prompt: str) -> dict:
    """Send a sanitised prompt to GPT-4o and return a structured analysis. Implementation in Phase 2."""
    raise NotImplementedError


async def rule_based_fallback(alert_data: dict) -> dict:
    """Return a deterministic triage result when the LLM is unavailable. Implementation in Phase 2."""
    raise NotImplementedError
