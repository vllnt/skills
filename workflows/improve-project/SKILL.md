---
name: improve-project
description: Adapt an existing repository to applicable stack preferences through small verified stages.
---

# Improve Project

Realign an established project in small stages; use `improve-code` for local behavior-preserving simplification. Assessment/planning only inspects and proposes.

## Workflow

1. Confirm target alignment, rules, authority, current state, preserved contracts, and whether package/config adoption differs from framework/backend replacement.
2. Use `capability-project-alignment` when available for target decisions and its `capability-stack-packages` composition for current evidence; otherwise perform those checks directly. Compare needed packages and runtimes against consumer evidence, exports, peers, data owners, and compatibility; define the smallest staged plan.
3. Capture an authorized baseline, then apply one authorized stage with exact dependency/configuration checks.
4. For data/backend work, verify mapping, authorization, reconciliation, recovery, and cutover ownership in isolation before dependent work.
5. Verify affected consumers, entry points, platforms, failures, and data invariants. Use distinct review or critique perspectives when they add evidence proportional to the stage; otherwise assess sequentially. Repair permitted gaps and rerun affected proof. Stop unchanged retries. If blocked, state the cause, viable options, recommendation, consequence, and next action; report only the observed partial stage as verified.

## Definition of Done

- Alignment, contracts, package/runtime decisions, and stage boundary are explicit.
- Planning returns stages, acceptance, recovery, and gaps without execution or data changes.
- Authorized stage has configuration and behavior evidence or labeled platform gap.
- Data transitions have required recovery and authorization evidence.
