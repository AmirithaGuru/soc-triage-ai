"""Queries VirusTotal and AbuseIPDB to return a combined IP reputation verdict for a given indicator."""
from __future__ import annotations


async def check_ip(ip_address: str) -> dict:
    """Return combined VirusTotal + AbuseIPDB verdict for the given IP. Implementation in Phase 2."""
    raise NotImplementedError
