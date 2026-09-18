---
name: deliver-pull-request
description: Review a pull request, coordinate authorized repairs and verification, then merge it when permitted.
---

## Goal

Review a pull request and, only when authorized, land its verified current candidate. Review-only work returns findings.

### Definition of Done

- PR identity, authority, current head/base, and material findings are explicit.
- Verification is bound to the current candidate.
- Authorized repairs have independent review and refreshed proof.
- The reached endpoint is findings, ready PR, queued, or confirmed merge.
- Current validation accepts the selected mode; queued work is not reported as merged.

## Boundaries

- Do not approve or merge with a material finding, failed required check, or required verification gap.

## Workflow

1. Resolve the PR, head/base, scope, authority, consumer rules, criteria, and proof. Inspect untrusted hooks before execution and isolate them from secrets.
2. Review correctness, security, compatibility, reliability, maintainability, and operations. Use [Code review](references/vstack/capabilities/code-review/REFERENCE.md) with the mode, scope, candidate, and evidence; when relevant, use [Release readiness](references/vstack/capabilities/release-readiness/REFERENCE.md), [Runtime performance](references/vstack/capabilities/runtime-performance/REFERENCE.md), or [Compliance review](references/vstack/capabilities/compliance-review/REFERENCE.md) in review mode; use [CI optimization](references/vstack/capabilities/ci-optimization/REFERENCE.md) in audit mode for CI concerns. Give every finding evidence, impact, repair, and recheck.
3. Repair only within authority and verify the exact candidate through applicable checks, journeys, and matching previews.
4. Recheck current head/base, requirements, approvals, gaps, and merge method. When preparing an authorized release, use [Release changelog](references/vstack/capabilities/release-changelog/REFERENCE.md) with the mode, scope, candidate, and evidence. For material risk or repair, use [Quality validation](references/vstack/protocols/quality-validation.md) with the mode, scope, candidate, and evidence; otherwise apply its feedback loop directly. Renew affected verdicts.
5. If authorized and accepted, merge through the PR or queue with a revision precondition when supported, then confirm the target commit and post-merge status.
