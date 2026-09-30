---
name: review-pull-request-qa
description: Test a pull request in a full local or preview environment and return candidate-bound backend, frontend, and end-to-end QA evidence.
---

## Goal

Assess a pull request in a representative full local or preview environment and return a reproducible QA report without changing product code or deciding whether to merge.

### Definition of Done

- The PR candidate, base, connected service revisions, target environment, test authority, and acceptance criteria are identified.
- Environment readiness and any isolated test-data setup are observed; unavailable or unsafe prerequisites remain explicit gaps.
- Required checks and risk-selected backend, frontend, and cross-layer journeys have actual outcomes or named coverage gaps, including relevant regressions.
- Visual and diagnostic claims cite valid screenshots, logs, or other observed evidence rather than inferred success.
- The report separates case results from the candidate-and-environment QA verdict, defects, exclusions, and residual risk; report acceptance does not certify an untested target.

## Boundaries

- Tests may write only authorized, isolated, resettable test data. Never run a seed against production or an ambiguous shared target; continue safe independent checks and request a consequential decision only if the remaining required test cannot be isolated.
- Do not repair product code, deploy, approve, or merge. A completed assessment with gaps does not certify the PR or claim that all regressions are absent.

## Workflow

1. Resolve the PR head/base, changed behavior, requirements, project instructions, required checks, permitted effects, and local or preview target. Map the real frontend, backend, workers, data stores, and external dependencies needed for affected journeys. Confirm deployed component revisions, actual cross-component bindings, and configuration against the intended compatible candidate; a live URL or green CI is not provenance.
2. Prepare the target using approved existing setup. Discover seed commands, fixtures, accounts, and reset procedures; run an existing seed automatically when its effects and destination are verified as non-production, isolated, repeatable, and reversible. Otherwise use safe existing fixtures or create minimal permitted disposable data. Verify records and cleanup. Gate testing on relevant service health, migrations, roles, runner/browser availability, diagnostics, and a small real journey; safely repair setup within authority, then recheck readiness. If the gate fails, still run independent checks and mark dependent scenarios unverified rather than asking about routine setup or treating readiness as behavioral proof.
3. Trace changed entry points through callers, contracts, shared state, and user journeys. Select changed and adjacent regression cases by likelihood and impact, using relevant boundary, role/denial, state, error, and recovery variations; state justified exclusions. Run cheap independent checks in parallel where possible, but retain all applicable project-required gates. Use [Code tests](references/vstack/capabilities/code-tests/REFERENCE.md) for the candidate-bound local/preview/CI ledger; if unavailable, record those identities, commands, results, and gaps directly. For a Next.js browser flow, use [Next.js tests](references/vstack/capabilities/nextjs-tests/REFERENCE.md) when available; otherwise exercise the real browser with installed tooling and report any browser gap.
4. In the ready environment, exercise applicable backend APIs, authorization, persistence and failure behavior; frontend rendering, interaction, accessibility-relevant states and viewports; and end-to-end UI-to-service-to-data outcomes. Check forbidden effects. For changed visuals, capture named states at comparable viewports and compare screenshots with a candidate-relevant baseline, inspecting differences and dynamic content; without a valid baseline, report observed appearance, not a regression comparison. Correlate browser console, requests, server/worker logs and traces by run/environment/time, redacting sensitive data. Diagnose failures against known-good behavior and distinguish product defects, pre-existing issues, flaky checks, and setup faults.
5. Return a compact scenario ledger with expected and observed outcome, environment/component identities, evidence, and pass/fail/unverified status; rank defects by impact with reproduction and recheck steps. Give the tested candidate/environment a separate QA verdict: FAIL for an observed required defect or failed required check, UNVERIFIED when required proof is missing, and PASS only when all required evidence passes with no required defect. After a candidate, seed, or environment change, rerun affected checks and renew only invalidated evidence. For a substantive report, use [Quality validation](references/vstack/protocols/quality-validation.md) with the scope, candidate, environment, and evidence; otherwise self-assess and seek relevant critique directly. Return the report and remaining risks to the caller, which owns repairs and PR readiness.
