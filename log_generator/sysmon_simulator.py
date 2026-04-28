"""Generates synthetic Sysmon-style attack log events for the six defined scenarios and posts them to the FastAPI ingest endpoint."""
from __future__ import annotations

SCENARIOS: list[dict] = [
    {"name": "Encoded PowerShell", "event_id": 1, "technique": "T1059.001", "tactic": "Execution"},
    {"name": "Registry Run Key", "event_id": 13, "technique": "T1547.001", "tactic": "Persistence"},
    {"name": "Suspicious C2", "event_id": 3, "technique": "T1071.001", "tactic": "Command & Control"},
    {"name": "LSASS Memory Access", "event_id": 10, "technique": "T1003.001", "tactic": "Credential Access"},
    {"name": "DLL Sideloading", "event_id": 7, "technique": "T1574.002", "tactic": "Defense Evasion"},
    {"name": "Benign IT Admin Task", "event_id": 1, "technique": None, "tactic": "False Positive"},
]


def generate_event(scenario_name: str) -> dict:
    """Build a synthetic Sysmon event payload for the named scenario. Implementation in Phase 3."""
    raise NotImplementedError


def post_to_ingest(event: dict, base_url: str) -> None:
    """POST a synthetic event to the /ingest endpoint. Implementation in Phase 3."""
    raise NotImplementedError
