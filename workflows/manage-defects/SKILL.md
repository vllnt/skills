---
name: manage-defects
description: Diagnose a reported failure, isolate its cause, and apply authorized repairs with regression evidence.
---

## Goal

Explain a reported failure and, when authorized, repair its supported cause.

### Definition of Done

- The failure chain, environment, revision, and causal evidence are recorded.
- Diagnosis-only work returns a supported cause or ranked hypotheses, recommendation, and next discriminating check without repair.
- A repair addresses the supported cause with isolated failure-before and success-after regression evidence.
- Unverified seams and recovery behavior are explicit.
- Current validation accepts the selected mode; no required finding remains.

## Boundaries

- Reproduce and experiment without changing shared or production state. Do not retry until green to mask a cause.

## Workflow

1. Resolve expected and observed behavior, revision, inputs, environment, scope, instructions, candidate, and acceptance criteria.
2. Reproduce the smallest isolated failing chain. Separate defect, setup, stale artifact, and fixture causes.
3. Test competing causes with discriminating experiments and record rejected alternatives.
4. In repair mode, apply the smallest authorized change at the owning boundary, then prove failure before and success after through affected caller, denial/error, and recovery behavior.
5. For substantive diagnosis or repair, use `capability-quality-validation` when available; otherwise apply its feedback loop directly. Triage evidence-backed findings, repair only within authority, and renew affected verdicts after each correction.
