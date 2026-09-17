---
name: manage-defects
description: Diagnose a reported failure, isolate its cause, and apply authorized repairs with regression evidence.
---

# Manage Defects

Explain a failure and repair its cause when requested. Diagnosis-only work skips repair and validates only its evidence report; experiments stay within the permitted observation scope.

## Workflow

1. Read applicable user, project, and nested rules and loaded principles, then select a safe target. Before producing a substantive diagnosis or repair, define its validation contract: candidate, mode, Definition of Done, criteria, evidence, and useful perspectives. Record expected/observed behavior, revision, inputs, environment, scope, code, configuration, tests, and logs.
2. Reproduce the smallest isolated failing chain and separate defect, setup, stale artifact, and fixture causes without changing shared or production state.
3. Test competing causes with discriminating experiments; record rejected alternatives and avoid retry-until-green masking.
4. Apply the smallest authorized repair at the owning boundary, then prove failure before and success after with affected caller, denial/error, and recovery behavior.
5. For a substantive diagnosis or repair, use [Quality Validation](../../capabilities/capability-quality-validation/SKILL.md) before delivery. If unavailable, self-assess; obtain distinct review and critique with subagents, or assess them sequentially only when independence is not required; otherwise return BLOCKED. Triage findings, repair authorized defects, and request fresh affected verdicts until PASS. Use direct checks for mechanical work. Recheck only after a repair or discriminating evidence; on unchanged evidence, change approach or report the cause, options, recommendation, consequence, and next action.

## Definition of Done

- Failure chain, environment, revision, and causal evidence are recorded.
- Diagnosis-only result gives the supported cause or ranked hypotheses, recommendation, and next discriminating check without repair.
- Repair addresses the supported cause with isolated regression proof.
- Unverified seams and recovery behavior are explicit.
- Completion requires current mode-specific acceptance: every required criterion has proof, applicable review and critique scopes accept, and no required finding remains.
