---
name: improve-project
description: Adapt an existing repository to applicable stack preferences through small verified stages.
---

# Improve Project

Realign an established project in small stages; use `improve-code` for local behavior-preserving simplification. Assessment/planning skips implementation and execution steps and validates only the proposed stages.

## Workflow

1. Confirm target alignment, rules, authority, current state, preserved contracts, replacement scope, and the mode-specific Definition of Done and proof from the request, applicable instructions, and loaded principles.
2. Use `capability-project-alignment` when available for target decisions and its `capability-stack-packages` composition for current evidence; otherwise perform those checks directly. Compare needed packages and runtimes against consumer evidence, exports, peers, data owners, and compatibility; define the smallest staged plan.
3. Capture an authorized baseline, then apply one authorized stage with exact dependency/configuration checks.
4. For data/backend work, verify mapping, authorization, reconciliation, recovery, and cutover ownership in isolation before dependent work.
5. Verify affected consumers, entry points, platforms, failures, and data invariants. Validate the stage or plan against its mode-specific criteria. Use `capability-quality-validation` when available; otherwise self-assess, use independent review and critique for substantive work, or assess perspectives sequentially and state unavailable independence; triage findings, repair only authorized gaps, and renew affected verdicts after a change. Use direct checks for mechanical work. On REVISE, continue authorized repair or plan revision and fresh affected verdicts until acceptance. If a required correction is outside authority, return REVISE with the remedy and required checks. Return BLOCKED only when a required criterion cannot advance, with its next action; report only the observed partial stage as verified and do not retry unchanged evidence.

## Definition of Done

- Alignment, contracts, package/runtime decisions, and stage boundary are explicit.
- Planning returns stages, acceptance, recovery, and gaps without execution or data changes.
- Authorized stage has configuration and behavior evidence or labeled platform gap.
- Data transitions have required recovery and authorization evidence.
- Completion requires current mode-specific validation acceptance; otherwise report REVISE/BLOCKED with the unmet criterion and next action.
