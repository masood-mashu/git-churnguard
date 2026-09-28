# GitChurnGuard Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitChurnGuard** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitChurnGuard consumes SaaS application usage telemetry, customer license seat allocations, support ticket histories, and contract renewal schedules. These data sources include daily active user counts, feature utilization metrics, open support ticket severity ratings, and Net Promoter Score survey logs. The agent ingests these inputs in raw JSON, CSV, and CRM export format and parses them into standardized customer health vectors for downstream retention analysis. Enterprise account contract values and customer success escalation matrices are also monitored as sensitive data sources to ensure revenue retention is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When account telemetry is ingested, the agent first evaluates user adoption velocity using the usage-drop-detector tool to identify sharp weekly active user declines exceeding 30%. Next, the reasoning engine invokes the account-health-scorer tool to compute composite account health ratings across usage, tickets, and NPS dimensions. Furthermore, contract renewal urgency is assessed using the renewal-window-evaluator tool to trigger proactive interventions within 90 days of contract expiration. Finally, the agent correlates all account health factors against predefined retention playbooks to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated customer action plan.

---

## 3. Constraints, Limitations, and Known Issues

GitChurnGuard operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitChurnGuard operates under strict operational constraints to prevent preventable customer churn and contract loss across subscription businesses. The agent is deliberately limited to usage telemetry parsing and algorithmic health scoring and cannot conduct direct human negotiation with customer stakeholders. Another known issue and limitation is that customer corporate restructuring without digital platform signals may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
