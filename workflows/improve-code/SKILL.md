---
name: improve-code
description: Simplify code and comments while preserving observable contracts and affected consumers.
---

# Improve Code

Reduce demonstrated maintenance cost without changing supported behavior. Assessment skips transformation and execution steps and validates only proposed changes and checks.

## Workflow

1. Identify maintenance cost, contracts, callers, tests, configuration, relevant failures to preserve, and the mode-specific Definition of Done and proof from the request, applicable instructions, and loaded principles.
2. Establish a baseline when authorized; compare simpler ownership and regression risk, preferring deletion or existing interfaces over new layers.
3. Make the smallest authorized transformation, preserving dependency direction, validation, errors, documentation, and unique test protection.
4. Compare real callers before/after with success, failure, denial, compatibility, packaging, and build evidence.
5. Validate the transformation or assessment candidate against its mode-specific criteria. Use `capability-quality-validation` when available; otherwise self-assess, use independent review and critique for substantive work, or assess perspectives sequentially and state unavailable independence; triage findings, repair only authorized gaps, and renew affected verdicts after a change. Use direct checks for mechanical work. On REVISE, continue authorized repair or assessment revision and fresh affected verdicts until acceptance. If a required correction is outside authority, return REVISE with the remedy and required checks. Return BLOCKED only when a required criterion cannot advance, with its next action; missing proof narrows the result to the observed scope and does not justify unchanged retries.

## Definition of Done

- Maintenance cost and preserved contracts are identified.
- Assessment returns candidates and checks without execution.
- Authorized change is minimal with before/after caller evidence.
- Unverified transformations and risk are explicit.
- Completion requires current mode-specific validation acceptance; otherwise report REVISE/BLOCKED with the unmet criterion and next action.
