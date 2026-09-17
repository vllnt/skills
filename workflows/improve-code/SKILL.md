---
name: improve-code
description: Simplify code and comments while preserving observable contracts and affected consumers.
---

# Improve Code

Reduce demonstrated maintenance cost without changing supported behavior. Assessment-only work proposes changes and checks without writes or execution.

## Workflow

1. Identify maintenance cost, contracts, callers, tests, configuration, and relevant failures to preserve.
2. Establish a baseline when authorized; compare simpler ownership and regression risk, preferring deletion or existing interfaces over new layers.
3. Make the smallest authorized transformation, preserving dependency direction, validation, errors, documentation, and unique test protection.
4. Compare real callers before/after with success, failure, denial, compatibility, packaging, and build evidence.
5. Use distinct review or critique perspectives when they add evidence proportional to the transformation; otherwise assess sequentially. Repair permitted gaps and rerun affected checks. If blocked, state the cause, viable options, recommendation, consequence, and next action; missing proof narrows the result to the observed scope.

## Definition of Done

- Maintenance cost and preserved contracts are identified.
- Assessment returns candidates and checks without execution.
- Authorized change is minimal with before/after caller evidence.
- Unverified transformations and risk are explicit.
