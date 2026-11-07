---
name: manage-issues
description: Triage GitHub issues into an evidence-backed, atomic, actionable backlog, or plan source-backed issue drafts from a codebase assessment; apply only authorized changes.
license: MIT
---

## Goal

Turn a bounded issue backlog (triage mode) or a bounded codebase assessment (plan mode) into a traceable, actionable queue without implementing its issues. Triage decides on existing issues; plan drafts new ones from source evidence. Output is read-only unless hosted writes are explicitly authorized.

### Definition of Done

- Repository, scope, mode, criteria, and inventory (plan mode: revision, coverage, rules, sampling, exclusions) are explicit.
- Triage decisions have evidence, ownership where relevant, and a recommended first slice. Each plan draft has evidence, contract, acceptance, dependency, risk, and blocker; deduplication scope, the first slice, and deferred work are reported.
- Read-only work returns a traceable proposal without hosted mutation.
- Authorized writes are selected, applied, and read back.
- Current validation accepts the selected mode; no required finding remains.

## Workflow

1. Resolve repository, scope, current inventory (plan mode: revision, coverage, backlog access, processes), permitted effects, applicable instructions, and the validation contract.
2. Triage: classify evidence-backed keep, refine, split, duplicate, realign, stale, close, and blocked decisions, recording canonical links, owner, blocker, intended effect, and next action. Plan: map risk-relevant ownership, interfaces, state, integrations, tests, delivery, and journeys. When the bounded audit includes [infrastructure](references/vstack/capabilities/infrastructure-review/REFERENCE.md), [costs](references/vstack/capabilities/infrastructure-costs/REFERENCE.md), [compliance](references/vstack/capabilities/compliance-review/REFERENCE.md), or [agent tooling](references/vstack/capabilities/agent-tooling-review/REFERENCE.md), use that reference in read-only mode, inspecting criteria and proposing checks only; retain coverage, sampling, exclusions, and gaps.
3. Plan: group evidence by root cause, compare existing issues, and draft each issue with its scenario, confidence, smallest change, contracts, acceptance and failure cases, dependencies, risk, and blocker.
4. Recommend the first coherent slice with outcome, dependencies, and deferred work. Decide reversible details from evidence; ask only for missing authority or access, an irreversible or high-risk choice, or a preference evidence cannot settle, with a recommended answer.
5. For substantive work, use [Quality validation](references/vstack/protocols/quality-validation.md) before hosted writes (plan mode: read-only).
6. Apply only the authorized validated subset. Triage: preserve context and recoverable closure, then read back changed fields. Plan: recheck scope, revision, and backlog, create only validated selected drafts, and read them back. On unchanged evidence, change approach or return the open criterion and next action.
