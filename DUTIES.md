# Segregation of Duties (SOD) Policy: GitChurnGuard

This document establishes the role boundaries and segregation of duties for the GitChurnGuard agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring customer retention playbooks, configuring health scoring models, and preparing automated intervention diffs.
This role cannot approve or merge its own changes into protected customer success branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming health scores, churn risk alerts, and renewal intervention schedules.
This role operates as an impartial auditor to verify compliance with enterprise revenue retention benchmarks.

### 3. Approver
The Approver role is strictly reserved for human VPs of Customer Success and Chief Revenue Officers.
Human approval is required for all executive escalation assignments, contract concession discounts, and account termination overrides.
