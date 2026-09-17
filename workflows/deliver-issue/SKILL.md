---
name: deliver-issue
description: Deliver a scoped issue through a verified pull request and authorized merge to its target branch.
---

# Deliver Issue

Deliver one issue as a tested PR and, when authorized, a confirmed merge. Planning skips implementation and hosted steps, validating only the delivery plan; deployment and publishing need separate authority.

## Workflow

1. Confirm issue, repository, target, candidate, criteria and required proof from the request, applicable instructions, and loaded principles, and edit/PR/merge authority; reuse existing work when appropriate.
2. Inspect contracts, callers, tests, and configuration; implement the smallest authorized change and exercise relevant success and failure behavior.
3. Validate the candidate or plan through `capability-quality-validation` when available; otherwise self-assess, independently review and critique substantive work, triage findings, and repair only within authority and mode until affected checks and verdicts accept. If required correction is outside authority, return REVISE with the smallest remedy and fresh required checks. Carry current proof into landing instead of repeating it. After candidate acceptance and only in delivery mode, create or update the PR with the exact revision, scope, criteria, implementation and test evidence, limitations, and bindings.
4. Hand landing to `deliver-pull-request`, which owns final review, repair coordination, landing verification, and confirmed merge. If unavailable, apply that procedure directly without self-approving substantive repair.
5. If required authority, approval, or verification is missing, state the cause, viable options, recommendation, consequence, and next action. Return the reached endpoint only: ready PR, queued, or confirmed target-branch merge; queued is not merged.

## Definition of Done

- Planning returns an implementation plan, checks, and gates without implementation, execution checks, or PR writes.
- Candidate evidence is tied to the reviewed revision.
- Endpoint is explicit: ready PR, queued, or confirmed target-branch merge.
- A merge includes its resulting commit.
- Completion requires mode-specific acceptance; missing required proof or authority remains explicit unfinished work.
