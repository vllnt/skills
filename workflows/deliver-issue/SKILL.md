---
name: deliver-issue
description: Deliver a scoped issue through a verified pull request and authorized merge to its target branch.
---

## Goal

Deliver one issue as a tested pull request and, when authorized, a confirmed target-branch merge. Deployment and publication need separate authority.

### Definition of Done

- Planning returns an implementation plan, checks, and gates without implementation, execution checks, or PR writes.
- Candidate evidence is bound to the reviewed revision.
- The reached endpoint is explicit: ready PR, queued, or confirmed target-branch merge.
- A reported merge includes its resulting commit.
- Current validation accepts the selected mode; missing authority or proof remains unfinished work.

## Workflow

1. Resolve the issue, repository, target, candidate, criteria, required proof, and edit, PR, and merge authority from the request, instructions, and loaded principles.
2. Inspect contracts, callers, tests, and configuration. When the scope warrants it, use [Code architecture](references/vstack/capabilities/code-architecture/REFERENCE.md), [Code tests](references/vstack/capabilities/code-tests/REFERENCE.md), [Next.js tests](references/vstack/capabilities/nextjs-tests/REFERENCE.md), or [Convex components](references/vstack/capabilities/convex-components/REFERENCE.md) with the mode, scope, candidate, and evidence; in planning mode, inspect criteria and propose checks only. Return the implementation plan, gates, and proposed checks only in planning mode. In delivery mode, implement the smallest authorized change and exercise relevant success and failure behavior.
3. For a substantive candidate, use [Quality validation](references/vstack/protocols/quality-validation.md) with the mode, scope, candidate, and evidence; otherwise apply its feedback loop directly. Triage evidence-backed findings, repair only within authority and mode, and renew affected checks and verdicts.
4. In delivery mode, create or update the PR only after candidate acceptance, with its exact revision, scope, criteria, evidence, limitations, and bindings.
5. Hand final review, repair coordination, landing verification, and authorized merge to `deliver-pull-request`. If it is unavailable, apply the same landing procedure without self-approving a substantive repair. Return the reached endpoint and any unmet criterion.
