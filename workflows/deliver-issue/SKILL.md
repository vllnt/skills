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

1. Resolve issue, repository, target, candidate, criteria, proof, and edit/PR/merge authority from the request and applicable instructions.
2. Inspect contracts, callers, tests, project instructions, configuration, and CI to identify required checks. When relevant, use [Code architecture](references/vstack/capabilities/code-architecture/REFERENCE.md), [Code tests](references/vstack/capabilities/code-tests/REFERENCE.md), [Next.js tests](references/vstack/capabilities/nextjs-tests/REFERENCE.md), or [Convex components](references/vstack/capabilities/convex-components/REFERENCE.md) with the mode, scope, candidate, and evidence; in planning mode, return the plan, gates, and proposed checks only. In delivery mode, implement the smallest authorized change and exercise success and failure behavior.
3. Validate substantive candidates through [Quality validation](references/vstack/protocols/quality-validation.md), passing mode, scope, candidate, and evidence. If unavailable, self-assess, obtain independent review and critique, repair within mode and authority, and renew affected checks and verdicts. Use direct checks for mechanical changes.
4. In delivery mode, before pushing commits or creating/updating a PR, require passing results for every applicable required check that can run locally on the current candidate. Missing or failing local results block that action. Require review acceptance for this publication step, and include the exact revision, scope, criteria, evidence, limitations, and bindings in the PR. Required remote-only checks may remain pending for publication, but block final acceptance until they pass.
5. Pass the candidate, accepted review scope, current proof, and gaps to `deliver-pull-request` for landing. If unavailable, recheck head/base, requirements, approvals, gaps, and authority; merge only when accepted and authorized, then confirm the target commit and post-merge status. Never self-approve substantive repairs. Report the reached endpoint.
