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
2. Review correctness, security, compatibility, reliability, maintainability, and operations. Give every finding evidence, impact, repair, and recheck.
3. Repair only within authority and verify the exact candidate through applicable checks, journeys, and matching previews.
4. Recheck current head/base, requirements, approvals, gaps, and merge method. For material risk or repair, use `capability-quality-validation` when available; otherwise apply its feedback loop directly. Renew affected verdicts.
5. If authorized and accepted, merge through the PR or queue with a revision precondition when supported, then confirm the target commit and post-merge status.
