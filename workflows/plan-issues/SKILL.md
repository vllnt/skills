---
name: plan-issues
description: Assess a codebase and prepare a source-backed, deduplicated issue backlog for human review.
---

## Goal

Turn a bounded codebase assessment into source-backed issue drafts. Output is read-only unless hosted creation is explicitly authorized.

### Definition of Done

- Revision, coverage, rules, sampling, exclusions, and criteria are explicit.
- Each draft has evidence, contract, acceptance, dependency, risk, and blocker.
- Deduplication scope, the recommended first slice, and deferred work are reported.
- Read-only work creates no mutation; authorized creation is read back.
- Current validation accepts the selected mode; no required finding remains.

## Workflow

1. Resolve repository, revision, coverage, backlog access, processes, permitted effects, applicable instructions, and the issue-plan validation contract.
2. Map risk-relevant ownership, interfaces, state, integrations, tests, delivery, and journeys. Retain coverage, sampling, exclusions, and gaps.
3. Group evidence by root cause, compare existing issues, and draft each issue with its scenario, confidence, smallest change, contracts, acceptance and failure cases, dependencies, risk, and blocker.
4. Order and recommend the first coherent slice with expected outcome, dependencies, and deferred work.
5. For substantive planning, use `capability-quality-validation` when available; otherwise apply its feedback loop directly before hosted creation. Triage findings, improve drafts, and renew affected verdicts. If creation is authorized, recheck scope, revision, and backlog, then create only validated selected drafts and read them back.
