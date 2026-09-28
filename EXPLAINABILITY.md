# Explainability & Governance Statement

## Decision Architecture
GitChurnGuard evaluates renewal risk through deterministic telemetry indicators. By weighting weekly active user trajectory, support ticket sentiment, and contract days-to-renewal, the agent flags accounts entering danger zones. If health metrics decline below critical thresholds, the agent outputs recommended mitigation steps (e.g. training webinar, CSM check-in).

## Input Data Provenance
Data inputs include product telemetry logs, CRM contract records, Zendesk support ticket metrics, and Delighted NPS survey feedback.

## Operational Limits & Non-Goals
GitChurnGuard monitors platform usage and documented interactions; it cannot detect informal offline customer corporate restructuring or executive leadership departures without CRM entry.
