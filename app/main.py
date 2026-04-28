"""FastAPI application instance, route definitions, and Mangum Lambda handler for the SOC Triage AI service."""
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="SOC Triage AI", version="0.1.0")
handler = Mangum(app)


@app.get("/health", tags=["ops"])
async def health() -> dict[str, str]:
    """Return service liveness status."""
    return {"status": "ok", "service": "soc-triage-ai"}


# ---------------------------------------------------------------------------
# Stub route registrations — implementations land in later phases
# POST   /ingest               → receives alert from Splunk or simulator
# GET    /triage/{alert_id}    → returns enriched triage report
# GET    /alerts/pending       → lists alerts awaiting analyst decision
# POST   /feedback/{alert_id}  → analyst submits confirm or dismiss
# GET    /metrics              → false positive rate, confidence, latency
# ---------------------------------------------------------------------------
