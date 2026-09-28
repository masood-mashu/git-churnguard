# Separation of Duties for GitChurnGuard

## Maker Role: CustomerSuccessAnalyst
CustomerSuccessAnalyst who analyzes product adoption telemetries and license utilization trends.

## Checker Role: VPofCustomerSuccess
VPofCustomerSuccess who authorizes retention playbooks, outreach programs, and renewal terms.

## Dual-Control Verification Pipeline
1. Ingest daily active user (DAU) telemetry and seat license allocation data.
2. Calculate 30-day usage velocity variance against historical cohort averages.
3. Compute unified account health composite score (0 to 100).
4. Generate proactive retention action plans and executive intervention summaries.
