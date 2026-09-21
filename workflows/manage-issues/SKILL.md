---
name: manage-issues
description: Triage GitHub issues into an evidence-backed, atomic, actionable backlog and apply authorized changes.
license: MIT
---

## Goal

Turn a bounded issue backlog into a traceable, actionable queue without implementing its issues.

### Definition of Done

- Repository, scope, inventory, mode, and criteria are identified.
- Decisions have evidence, ownership where relevant, and a recommended first slice.
- Read-only work returns a traceable proposal without hosted mutation.
- Authorized writes are selected, applied, and read back.
- Current validation accepts the selected mode; no required finding remains.

## Workflow

1. Resolve repository, scope, current inventory, permitted effects, applicable instructions, and the triage validation contract.
2. Classify evidence-backed keep, refine, split, duplicate, realign, stale, close, and blocked decisions. Record canonical links, owner, blocker, intended effect, and next action.
3. Recommend the first coherent slice with outcome and dependencies. Decide reversible triage details from evidence; ask only for a consequential choice or missing authority.
4. For substantive triage, use [Quality validation](references/vstack/protocols/quality-validation.md) with the mode, scope, candidate, and evidence; otherwise apply its feedback loop directly before hosted writes. Triage findings, improve the candidate, and renew affected verdicts until acceptance.
5. Apply only the authorized validated subset, preserve context and recoverable closure, then read back changed fields. On unchanged evidence, change approach or return the open criterion and next action.
