---
name: deliver-issue
description: Deliver a scoped issue through a verified pull request and authorized merge to its target branch.
---

# Deliver Issue

Deliver one issue as a tested PR and, when authorized, a confirmed merge. Planning proposes delivery without writes or execution; deployment and publishing need separate authority.

## Workflow

1. Confirm issue, repository, target, candidate, criteria, and edit/PR/merge authority; reuse existing work when appropriate.
2. Inspect contracts, callers, tests, and configuration; implement the smallest authorized change and exercise relevant success and failure behavior.
3. Create or update the PR with the exact revision, scope, criteria, implementation and test evidence, limitations, and bindings.
4. Hand landing to `deliver-pull-request`, which owns final review, repair coordination, landing verification, and confirmed merge. If unavailable, apply that procedure directly without self-approving substantive repair.
5. If required authority, approval, or verification is missing, state the cause, viable options, recommendation, consequence, and next action. Return the reached endpoint only: ready PR, queued, or confirmed target-branch merge; queued is not merged.

## Definition of Done

- Planning returns an implementation plan, checks, and gates without implementation, validation, or PR writes.
- Candidate evidence is tied to the reviewed revision.
- Endpoint is explicit: ready PR, queued, or confirmed target-branch merge.
- A merge includes its resulting commit.
