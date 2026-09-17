---
name: deliver-pull-request
description: Review a pull request, coordinate authorized repairs and verification, then merge it when permitted.
---

# Deliver Pull Request

Review a PR and, only when authorized, land its verified current candidate. Review-only work produces findings only.

## Workflow

1. Confirm PR, head/base, criteria, scope, authority, and consumer rules. Inspect untrusted hooks before execution and isolate them from secrets.
2. Review relevant correctness, security, compatibility, reliability, maintainability, and operations; findings need evidence, impact, repair, and recheck.
3. Repair only within authority; substantive repairs need independent review. Verify the exact candidate with applicable checks, journeys, and matching preview.
4. Recheck current head/base, requirements, approvals, gaps, and method before merge. Do not approve or merge with a material finding, failed required check, or required verification gap.
5. Use distinct review or critique perspectives when they add evidence proportional to the PR’s risk or repair scope; otherwise assess sequentially. Repair permitted findings and rerun affected proof. Merge through the PR/queue with a revision precondition when supported, then confirm the target commit and post-merge status. If blocked, state the cause, viable options, recommendation, consequence, and next action; queued is not merged.

## Definition of Done

- PR identity, authority, and material findings are explicit.
- Verification is bound to the current candidate.
- Repairs have independent review and refreshed proof.
- Endpoint is findings, ready PR, queued, or confirmed merge.
