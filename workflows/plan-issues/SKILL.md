---
name: plan-issues
description: Assess a codebase and prepare a source-backed, deduplicated issue backlog for human review.
---

# Plan Issues

Turn a bounded codebase assessment into issue drafts. Default output is read-only; hosted creation needs explicit authority.

## Workflow

1. Confirm repository, revision, coverage, backlog access, rules, processes, and permitted effects.
2. Map risk-relevant ownership, interfaces, state, integrations, tests, delivery, and journeys; retain coverage, sampling, exclusions, and gaps.
3. Group evidence by root cause, compare readable issues, and draft each with scenario, confidence, smallest change, contracts, acceptance/failure cases, dependencies, risk, and blocker.
4. Order and recommend the first coherent slice with expected outcome, dependencies, and deferred work. Decide reversible drafting details from evidence; ask only for a consequential scope choice or hosted-creation authority.
5. If creation is authorized, recheck scope, revision, and backlog; create selected drafts and read them back.
6. Use independent proposal/challenge or review/critique only for distinct material questions. Recheck after changed evidence or a repair. If blocked, return the cause, options, recommendation, consequence, and next action.

## Definition of Done

- Revision, coverage, rules, sampling, and exclusions are explicit.
- Each draft has evidence, contract, acceptance, dependency, and blocker.
- Deduplication scope, recommended first slice, and deferred work are reported.
- Read-only work creates no mutation; authorized creation is read back.
