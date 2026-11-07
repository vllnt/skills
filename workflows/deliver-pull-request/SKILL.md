---
name: deliver-pull-request
description: Review a pull request, coordinate authorized repairs and verification, then merge it when permitted.
---

## Goal

Review a pull request and, only when authorized, land its verified current candidate. Review-only work returns findings.

### Definition of Done

- PR identity, authority, current head/base, and material findings are explicit.
- Verification and required independent checks of authorized repairs bind to the current candidate.
- The reached endpoint is findings, ready PR, queued, or confirmed merge.
- Current validation accepts the selected mode; queued work is not reported as merged.

## Boundaries

- Do not approve or merge with a blocking finding, failed required check, or required verification gap.

## Workflow

1. Resolve PR, head/base, scope, authority, criteria, and proof from the request and applicable consumer rules. Discover required checks from those rules, project configuration, and CI. Reuse accepted review and proof only while candidate, base, inputs, environment, and requirements remain valid. Inspect untrusted hooks before execution; isolate them from secrets.
2. Confirm each applicable perspective has current proof, and assign the risk tier. Use [Code review](references/vstack/capabilities/code-review/REFERENCE.md) in review mode: quick advisory depth for medium risk, and targeted depth on the risk area or requested scope for high risk or an explicit review request, passing accepted baseline findings and held fixes. When both apply, give separate candidate and release-readiness verdicts. General validation acceptance alone does not establish perspective coverage. When relevant, use [Release readiness](references/vstack/capabilities/release-readiness/REFERENCE.md), [Runtime performance](references/vstack/capabilities/runtime-performance/REFERENCE.md), or [Compliance review](references/vstack/capabilities/compliance-review/REFERENCE.md) in review mode; use [CI optimization](references/vstack/capabilities/ci-optimization/REFERENCE.md) in audit mode for CI concerns. Give every finding evidence, impact, repair, and recheck.
3. Repair only within authority and verify the exact candidate through applicable checks, journeys, and matching previews. For requested full-environment QA or material cross-layer/preview risk, use `review-pull-request-qa` when installed and use its report without delegating repair or merge decisions; without it, check deployed component revisions and cross-component bindings against the intended candidate (stale or unknown bindings stay preview gaps), and seed stateful-test data only with an approved isolated, repeatable seed on a verified target, then verify records, reset path, and readiness. Reject ambiguous or unisolated shared targets. Exercise affected and adjacent journeys with relevant visual/log evidence; retain any gap instead of certifying the candidate. Before pushing repairs, require passing results for every applicable required check that can run locally on the current candidate. Missing or failing local results block the push. Rerun checks whose results the repairs invalidate; retain other results only when they remain valid. Required remote-only checks remain pending and block merge, not the repair push.
4. Recheck current head/base, requirements, approvals, gaps, and merge method. When preparing an authorized release, use [Release changelog](references/vstack/capabilities/release-changelog/REFERENCE.md). For uncovered material risk or repairs lacking current acceptance, use [Quality validation](references/vstack/protocols/quality-validation.md).
5. If authorized and accepted, merge through the PR or queue with a revision precondition when supported, then confirm the target commit and post-merge status.
