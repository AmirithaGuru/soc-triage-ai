"""Local MITRE ATT&CK technique lookup: maps Sysmon event IDs and technique IDs to tactic and description strings."""
from __future__ import annotations


def lookup_technique(technique_id: str) -> dict | None:
    """Return tactic and description for the given ATT&CK technique ID, or None if unknown. Implementation in Phase 2."""
    raise NotImplementedError
