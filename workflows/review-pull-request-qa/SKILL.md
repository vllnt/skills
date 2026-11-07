---
name: review-pull-request-qa
description: Test a pull request in a full local or preview environment and return candidate-bound backend, frontend, and end-to-end QA evidence.
---

## Goal

Assess a pull request in a representative full local or preview environment and return a reproducible QA report.

### Definition of Done

- The PR candidate, base, connected service revisions, target environment, test authority, and acceptance criteria are identified.
- Environment readiness and any isolated test-data setup are observed; unavailable or unsafe prerequisites remain explicit gaps.
- Required checks and risk-selected backend, frontend, and cross-layer journeys have actual outcomes or named coverage gaps, including relevant regressions.
- Visual and diagnostic claims cite valid screenshots, logs, or other observed evidence, not inferred success.
- The report separates case results from the candidate-and-environment QA verdict, defects, exclusions, and residual risk; neither acceptance nor a gapped assessment certifies the PR, an untested target, or the absence of regressions.

## Boundaries

- Tests may write only authorized, isolated, resettable test data. Continue safe independent checks and request a consequential decision only if the remaining required test cannot be isolated.
- Do not repair product code, deploy, approve, or merge.

## Workflow

1. Resolve the PR head/base, changed behavior, requirements, project instructions, required checks, and permitted effects. Map the real frontend, backend, workers, data stores, and external dependencies needed for affected journeys. Confirm deployed component revisions, actual cross-component bindings, and configuration against the intended compatible candidate; a live URL or green CI is not provenance.
2. Prepare the target with approved existing setup. Discover seed commands, fixtures, accounts, and reset steps; run an existing seed automatically only when its effects and destination are verified non-production, isolated, repeatable, and reversible (never against production or an ambiguous shared target), else use safe existing fixtures or minimal permitted disposable data. Verify records and cleanup. Gate testing on service health, migrations, roles, runner/browser availability, diagnostics, and a small real journey; safely repair setup within authority and recheck. If the gate fails, still run independent checks and mark dependent scenarios unverified, without asking about routine setup or treating readiness as behavioral proof.
3. Trace changed entry points through callers, contracts, shared state, and user journeys. Select changed and adjacent regression cases by likelihood and impact, using relevant boundary, role/denial, state, error, and recovery variations; state justified exclusions. Use [Code tests](references/vstack/capabilities/code-tests/REFERENCE.md) for the candidate-bound local/preview/CI ledger. For a browser flow, exercise the real browser with installed tooling and report any browser gap; use [Next.js tests](references/vstack/capabilities/nextjs-tests/REFERENCE.md) for a Next.js app.
4. In the ready environment, exercise applicable backend APIs, authorization, persistence and failure behavior; frontend rendering, interaction, accessibility-relevant states and viewports; and end-to-end UI-to-service-to-data outcomes, checking forbidden effects. For changed visuals, compare named-state screenshots at comparable viewports with a candidate-relevant baseline, inspecting differences and dynamic content; without a valid baseline, report observed appearance only. Correlate browser console, requests, and server/worker logs and traces by run/environment/time, redacting sensitive data. Diagnose failures against known-good behavior, distinguishing product defects, pre-existing issues, flaky checks, and setup faults.
5. Return a scenario ledger with expected and observed outcome, environment/component identities, evidence, and pass/fail/unverified status; rank defects by impact with reproduction and recheck steps. Give the tested candidate/environment a separate QA verdict: FAIL for an observed required defect or failed required check, UNVERIFIED when required proof is missing, otherwise PASS. After a candidate, seed, or environment change, rerun only affected checks. For a substantive report, use [Quality validation](references/vstack/protocols/quality-validation.md). Return the report and remaining risks to the caller, which owns repairs and PR readiness.
