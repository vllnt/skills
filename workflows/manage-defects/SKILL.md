---
name: manage-defects
description: Diagnose a reported failure, isolate its cause, and apply authorized repairs with regression evidence.
---

# Manage Defects

Explain a failure and repair its cause when requested. Diagnosis-only work returns evidence without repair.

## Workflow

1. Read applicable consumer rules and select a safe target. Record expected/observed behavior, revision, inputs, environment, scope, code, configuration, tests, and logs.
2. Reproduce the smallest isolated failing chain and separate defect, setup, stale artifact, and fixture causes without changing shared or production state.
3. Test competing causes with discriminating experiments; record rejected alternatives and avoid retry-until-green masking.
4. Apply the smallest authorized repair at the owning boundary, then prove failure before and success after with affected caller, denial/error, and recovery behavior.
5. Use independent review and critique only when they can test distinct causal questions; otherwise assess sequentially. Recheck only after a repair or discriminating evidence. If work remains, state the cause, options, recommendation, consequence, and next action.

## Definition of Done

- Failure chain, environment, revision, and causal evidence are recorded.
- Diagnosis-only result gives the supported cause or ranked hypotheses, recommendation, and next discriminating check without repair.
- Repair addresses the supported cause with isolated regression proof.
- Unverified seams and recovery behavior are explicit.
