---
name: improve-code
description: Simplify code and comments while preserving observable contracts and affected consumers.
---

## Goal

Reduce demonstrated maintenance cost while preserving supported behavior, or return an assessment of proposed changes and checks.

### Definition of Done

- Maintenance cost, preserved contracts, callers, and relevant failures are identified.
- Assessment returns candidates and checks without transformations or execution.
- An authorized change is minimal and has before/after caller evidence.
- Unverified transformations and remaining risk are explicit.
- Current validation accepts the selected mode; an unmet required criterion remains REVISE or BLOCKED.

## Workflow

1. Resolve the maintenance cost, contracts, callers, tests, configuration, preservation criteria, and evidence from the request, instructions, and loaded principles.
2. Establish an authorized baseline. Compare simpler ownership and regression risk, preferring deletion or existing interfaces over new layers.
3. In change mode, make the smallest authorized transformation while preserving dependency direction, validation, errors, documentation, and unique test protection.
4. In change mode, compare real callers before and after through applicable success, failure, denial, compatibility, packaging, and build evidence. In assessment mode, propose the required checks only.
5. In assessment mode, return candidates and checks only. For substantive work, use `capability-quality-validation` when available; otherwise apply its feedback loop directly. Renew affected verdicts after each authorized correction.
