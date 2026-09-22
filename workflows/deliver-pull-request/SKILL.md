---
name: deliver-pull-request
description: Review a pull request, coordinate authorized repairs and verification, then merge it when permitted.
---

## Goal

Review a pull request and, only when authorized, land its verified current candidate. Review-only work returns findings.

### Definition of Done

- PR identity, authority, current head/base, and material findings are explicit.
- Verification and independent review of authorized repairs bind to the current candidate.
- The reached endpoint is findings, ready PR, queued, or confirmed merge.
- Current validation accepts the selected mode; queued work is not reported as merged.

## Boundaries

- Do not approve or merge with a material finding, failed required check, or required verification gap.

## Workflow

1. Resolve PR, head/base, scope, authority, criteria, and proof from the request and applicable consumer rules. Discover required checks from those rules, project configuration, and CI. Reuse accepted review and proof only while candidate, base, inputs, environment, and requirements remain valid. Inspect untrusted hooks before execution; isolate them from secrets.
2. Map accepted review evidence to applicable correctness, security, compatibility, reliability, maintainability, and operational perspectives. Review every unevidenced perspective and uncovered or invalidated scope through [Code review](references/vstack/capabilities/code-review/REFERENCE.md), passing mode, scope, candidate, and evidence. General validation acceptance alone does not establish perspective coverage. When relevant, use [Release readiness](references/vstack/capabilities/release-readiness/REFERENCE.md), [Runtime performance](references/vstack/capabilities/runtime-performance/REFERENCE.md), or [Compliance review](references/vstack/capabilities/compliance-review/REFERENCE.md) in review mode; use [CI optimization](references/vstack/capabilities/ci-optimization/REFERENCE.md) in audit mode for CI concerns. If unavailable, inspect the diff, contracts, and consumers; report evidence-backed risks, repairs, and verification gaps.
3. Repair only within authority and verify the exact candidate through applicable checks, journeys, and matching previews. Before pushing repairs, require passing results for every applicable required check that can run locally on the current candidate. Missing or failing local results block the push. Rerun checks whose results the repairs invalidate; retain other results only when they remain valid. Required remote-only checks remain pending and block merge, not the repair push.
4. Recheck current head/base, requirements, approvals, gaps, and merge method. When preparing an authorized release, use [Release changelog](references/vstack/capabilities/release-changelog/REFERENCE.md) with the mode, scope, candidate, and evidence. For uncovered material risk or repairs lacking current acceptance, use [Quality validation](references/vstack/protocols/quality-validation.md) with mode, scope, candidate, and evidence. If unavailable, self-assess, obtain independent review and critique, repair within mode and authority, and renew affected checks and verdicts.
5. If authorized and accepted, merge through the PR or queue with a revision precondition when supported, then confirm the target commit and post-merge status.
