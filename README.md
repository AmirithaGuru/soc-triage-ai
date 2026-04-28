# SOC Triage AI
### AI-Augmented Security Alert Triage · Human-in-the-Loop Pipeline

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?logo=openai&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-Serverless-FF9900?logo=awslambda&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)

---

## Overview

SOC analysts at mid-to-large organizations can receive thousands of Splunk alerts per day.
Each one ideally requires a structured investigation: identify the process that fired,
map the behavior to a known attack technique, check whether the source IP has a history
of malicious activity, and make a triage decision. Done manually, that takes 15 to 30
minutes per alert. At scale, this creates alert fatigue. Analysts get overwhelmed, start
skipping steps, and real threats get buried under false positives.

This project builds an automated enrichment and triage layer that sits between Splunk and
the analyst. When an alert fires, the system investigates it automatically and presents a
structured AI-generated report for the analyst to review. The analyst reads the reasoning
and clicks Confirm (true positive) or Dismiss (false positive).

The AI investigates. The human decides. Always.

---

## How It Works

**1. Ingestion**
A raw Sysmon-format alert arrives at POST /ingest from a Splunk webhook or the included
log simulator. Pydantic validates the payload and persists it to PostgreSQL.

**2. Enrichment**
The triage engine runs three lookups:
- MITRE ATT&CK maps the Sysmon event to a technique ID and tactic
- IP Reputation checks the source IP against VirusTotal and AbuseIPDB
- Process History queries the Splunk REST API for what the host was doing before the alert fired

**3. LLM Analysis**
Enriched context is assembled into a sanitized prompt and sent to GPT-4o, which returns a
structured JSON report: severity level, technique ID, confidence score (0 to 100),
plain-English reasoning, and a recommended analyst action.

**4. Analyst Review**
The report surfaces on a Next.js dashboard. The analyst confirms or dismisses. That decision
is logged and feeds back into the metrics endpoint, giving visibility into false positive
rates and model confidence over time.

---

## System Flow

```
Splunk / Log Simulator
        |
        v
  POST /ingest  ->  Pydantic validation  ->  PostgreSQL
        |
        v
  Triage Engine
  |- MITRE ATT&CK lookup     (local JSON)
  |- IP reputation check     (VirusTotal + AbuseIPDB)
  +- Process history query   (Splunk REST API)
        |
        v
  OpenAI GPT-4o
  -> severity, technique, confidence, reasoning, action
        |
        v
  Next.js Analyst Dashboard
  |- Confirm  ->  true positive logged
  +- Dismiss  ->  false positive logged, metrics update
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /ingest | Accept raw alert from Splunk or simulator |
| GET | /triage/{alert_id} | Return AI-generated triage report |
| GET | /alerts/pending | List alerts awaiting analyst decision |
| POST | /feedback/{alert_id} | Record analyst confirm or dismiss |
| GET | /metrics | False positive rate, avg confidence, latency |
| GET | /health | Liveness check for CI/CD and smoke tests |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend API | Python 3.12, FastAPI, Pydantic v2, Mangum |
| AI / LLM | OpenAI GPT-4o with rule-based fallback on timeout |
| Security Data | Splunk, MITRE ATT&CK, VirusTotal, AbuseIPDB |
| Database | PostgreSQL, SQLAlchemy 2.0, Supabase (production) |
| Infrastructure | Docker, AWS Lambda, ECR, SSM Parameter Store |
| CI/CD | GitHub Actions, Bandit, detect-secrets, Ruff |
| Frontend | Next.js, TypeScript, shadcn/ui, Vercel |

---

## Security Considerations

- Prompt injection defense -- alert fields are sanitized before being embedded in LLM prompts
- No plaintext secrets -- all credentials loaded from environment variables; SSM Parameter Store in production
- CI security scanning -- Bandit and detect-secrets run on every pull request
- Human-in-the-loop -- the LLM surfaces recommendations only; no automated remediation actions

---

## Local Setup

Full setup instructions will be added when the local full stack is complete.
The local environment runs entirely in Docker Compose. Splunk, PostgreSQL, and the
FastAPI app start with a single command.
