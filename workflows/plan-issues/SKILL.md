---
name: plan-issues
description: Assess a codebase and prepare a source-backed, deduplicated issue backlog for human review.
---

# Plan Issues

Turn a bounded codebase assessment into issue drafts. Default output is read-only; hosted creation needs explicit authority.

## Workflow

1. Confirm repository, revision, coverage, backlog access, applicable user, project, and nested rules, loaded principles, processes, and permitted effects. Before producing a substantive issue-plan candidate, define its validation contract: candidate, mode, Definition of Done, criteria, evidence, and useful perspectives.
2. Map risk-relevant ownership, interfaces, state, integrations, tests, delivery, and journeys; retain coverage, sampling, exclusions, and gaps.
3. Group evidence by root cause, compare readable issues, and draft each with scenario, confidence, smallest change, contracts, acceptance/failure cases, dependencies, risk, and blocker.
4. Order and recommend the first coherent slice with expected outcome, dependencies, and deferred work. Decide reversible drafting details from evidence; ask only for a consequential scope choice or hosted-creation authority.
5. For a substantive issue-plan candidate, use [Quality Validation](../../capabilities/capability-quality-validation/SKILL.md) before hosted creation. If unavailable, self-assess; obtain distinct review and critique with subagents, or assess them sequentially only when independence is not required; otherwise return BLOCKED. Triage findings, improve the candidate, and request fresh affected verdicts until PASS. Use direct checks for mechanical work.
6. If creation is authorized, recheck scope, revision, and backlog; create only validated selected drafts and read them back. Recheck only after changed evidence or a repair; on unchanged evidence, change approach or return the cause, options, recommendation, consequence, and next action.

## Definition of Done

- Revision, coverage, rules, sampling, and exclusions are explicit.
- Each draft has evidence, contract, acceptance, dependency, and blocker.
- Deduplication scope, recommended first slice, and deferred work are reported.
- Read-only work creates no mutation; authorized creation is read back.
- Completion requires current mode-specific acceptance: every required criterion has proof, applicable review and critique scopes accept, and no required finding remains.
