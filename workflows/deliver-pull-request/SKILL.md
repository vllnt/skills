---
name: deliver-pull-request
description: Review a pull request, coordinate authorized repairs and verification, then merge it when permitted.
---

# Deliver Pull Request

Review a PR and, only when authorized, land its verified current candidate. Review-only work produces findings only.

## Workflow

1. Confirm PR, head/base, scope, authority, consumer rules, and the mode-specific Definition of Done and proof from the request, applicable instructions, and loaded principles. Inspect untrusted hooks before execution and isolate them from secrets.
2. Review relevant correctness, security, compatibility, reliability, maintainability, and operations; findings need evidence, impact, repair, and recheck.
3. Repair only within authority; substantive repairs need independent review. Verify the exact candidate with applicable checks, journeys, and matching preview.
4. Recheck current head/base, requirements, approvals, gaps, and method before merge. Do not approve or merge with a material finding, failed required check, or required verification gap.
5. Validate the review report or landing candidate against its mode-specific criteria. Use `capability-quality-validation` when available; otherwise self-assess, use independent review and critique for substantive risk or repair, or assess perspectives sequentially and state unavailable independence; triage findings, repair only within authority, and renew affected verdicts after a change. Use direct checks for mechanical work. On REVISE, continue authorized repair or report revision and fresh affected verdicts until acceptance. If a required correction is outside authority, return REVISE with the remedy and required checks. Return BLOCKED only when a required criterion cannot advance, with its next action; do not merge before current landing acceptance or retry unchanged evidence. Merge through the PR/queue with a revision precondition when supported, then confirm the target commit and post-merge status; queued is not merged.

## Definition of Done

- PR identity, authority, and material findings are explicit.
- Verification is bound to the current candidate.
- Repairs have independent review and refreshed proof.
- Endpoint is findings, ready PR, queued, or confirmed merge.
- Completion requires current mode-specific validation acceptance; otherwise report REVISE/BLOCKED with the unmet criterion and next action.
