---
name: deliver-issue
description: Deliver a scoped issue through a verified pull request and authorized merge to its target branch.
---

## Goal

Deliver one issue as a tested pull request and, when authorized, a confirmed target-branch merge. Deployment and publication need separate authority.

### Definition of Done

- Planning returns an implementation plan, checks, and gates without implementation, execution checks, or PR writes.
- Candidate evidence is bound to the verified revision.
- The reached endpoint is explicit: ready PR, queued, or confirmed target-branch merge.
- A reported merge includes its resulting commit.
- Current validation accepts the selected mode; missing authority or proof remains unfinished work.

## Workflow

1. Resolve issue, repository, target, candidate, criteria, proof, and edit/PR/merge authority from the request, applicable instructions, and loaded principles.
2. Inspect contracts, callers, tests, project instructions, configuration, and CI to identify required checks. Use [Code architecture](references/vstack/capabilities/code-architecture/REFERENCE.md) or [Code tests](references/vstack/capabilities/code-tests/REFERENCE.md) when those domains are in scope; use [Next.js tests](references/vstack/capabilities/nextjs-tests/REFERENCE.md) or [Convex components](references/vstack/capabilities/convex-components/REFERENCE.md) only when the consumer uses the corresponding stack and the procedure is relevant. Before implementing, use [Code review](references/vstack/capabilities/code-review/REFERENCE.md) in plan mode to select the applicable perspectives and a runnable proof for each. In planning mode, return the plan, gates, and proposed checks only. In delivery mode, implement the smallest authorized change plus any missing proof checks, and exercise success and failure behavior. When the issue adds structured logging in Node/Next.js server code, Convex actions, or CLIs, default to `@vllnt/logger` per [default packages](references/vstack/capabilities/project-alignment/references/default-packages.md), not `console` or a per-app pino setup. When the issue adds product analytics or event tracking to a web app on the @vllnt stack, default to `@vllnt/analytics`.
   For test changes, use [Test management](references/vstack/capabilities/code-test-management/REFERENCE.md).
3. Validate substantive candidates through [Quality validation](references/vstack/protocols/quality-validation.md), using Code review in review mode for medium and high tiers. Use direct checks for mechanical changes.
4. In delivery mode, before pushing commits or creating/updating a PR, require passing results for every applicable required check that can run locally on the current candidate. Missing or failing local results block that action. Require tier-matched verification acceptance for this publication step, and include the exact revision, scope, criteria, evidence, limitations, and bindings in the PR. Required remote-only checks may remain pending for publication, but block final acceptance until they pass.
5. Pass the candidate, accepted verification scope, current proof, and gaps to `deliver-pull-request` for landing; if it is unavailable, recheck head/base, requirements, approvals, and authority, merge only when accepted and authorized, and confirm the target commit and post-merge status. Self-proof suffices only at low tier; never self-verify medium or high risk. Report the reached endpoint.
