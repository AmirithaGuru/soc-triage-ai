"""Locust load test targeting the ingest and triage endpoints to measure throughput and latency under concurrent load."""
from locust import HttpUser, between, task


class SOCTriageUser(HttpUser):
    """Simulates a concurrent analyst or Splunk forwarding agent hitting the SOC Triage AI service."""

    wait_time = between(1, 3)

    @task
    def health_check(self) -> None:
        """Baseline task: hit /health to verify the service stays responsive under load."""
        self.client.get("/health")
