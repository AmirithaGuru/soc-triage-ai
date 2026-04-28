"""Orchestrates the full triage pipeline: enrichment → prompt sanitisation → LLM analysis → structured report assembly."""
from __future__ import annotations


async def run_triage(alert_id: str) -> dict:
    """Run the full triage pipeline for the given alert ID. Implementation in Phase 2."""
    raise NotImplementedError


async def enrich_alert(alert_data: dict) -> dict:
    """Enrich alert with MITRE, IP reputation, and process history. Implementation in Phase 2."""
    raise NotImplementedError


async def assemble_report(enriched: dict, llm_output: dict) -> dict:
    """Assemble the structured triage report from enriched data and LLM output. Implementation in Phase 2."""
    raise NotImplementedError
