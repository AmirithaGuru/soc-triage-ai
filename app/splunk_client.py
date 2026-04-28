"""Splunk REST API client for querying alert data and process history; all calls are authenticated via environment credentials."""
from __future__ import annotations


async def query_alerts(search: str) -> list[dict]:
    """Run a Splunk search and return matching events. Implementation in Phase 1."""
    raise NotImplementedError


async def get_alert_by_id(alert_id: str) -> dict | None:
    """Fetch a single alert by ID from Splunk. Implementation in Phase 1."""
    raise NotImplementedError
