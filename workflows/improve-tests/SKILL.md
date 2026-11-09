---
name: improve-tests
description: Improve a whole test suite by consolidating cross-file duplication and reducing execution cost while preserving coverage and defect detection.
---

## Goal

Improve the requested test suite as a whole, not one test: compare opportunities across files, then change the strongest supported scope. A scope is one coherent batch, possibly spanning many files. Preserve meaningful protection; a smaller suite is not better if defects become invisible.

### Definition of Done

- The suite's inventory, contracts, discovery gaps, fixed overall baseline, and cross-file opportunities are recorded.
- The selected batch has the strongest evidenced suite-level gain relative to effort and risk, and each change is verified before the next.
- Removed tests have retained assertions and representative defect detection or an authorized retired contract; unique boundary, denial, integration, recovery, and diagnostic protection remains.
- Comparable suite-wide results against the fixed baseline support the reported change; fixtures and configured CI wiring match retained tests.
- Quality validation accepts the selected mode; achieved reduction, shortfall, and unverified gaps are explicit. An assessment makes no changes or test runs.

## Workflow

1. Resolve mode, authority, consumer rules, contracts, and the requested unit (test cases, test source lines, or suite runtime). Discover the repository's languages, test commands, discovery rules, and coverage tools; impose no framework. Default to the whole repository suite unless narrowed. Freeze that suite's baseline revision, unit, denominator, exclusions, discovery configuration, and coverage instrumentation before editing, and never reset the overall baseline per batch. Newly skipped, undiscovered, or excluded tests are not savings. In read-only mode, run steps 1, 2, and 5.
2. Inventory the suite across directories, packages, and configured runners, reconciling native discovery with repository test files and recording ignored, skipped, generated, or undiscovered cases. Compare files, assertions, fixtures, helpers, mocks, and setup for duplicate protection and repeated cost, reading contracts, inputs, environments, failures, and diagnostic value first; similar names or line coverage alone do not establish redundancy. Inspect suite-level coverage gaps, shared-state flakiness, and runtime hotspots. Use [Code test management](references/vstack/capabilities/code-test-management/REFERENCE.md) to compare keep, improve, merge, replace, or remove. Rank opportunities by observed cost, overlapping protection, defect risk, effort, and reach; when uncertain, take a cheap discriminating check (change mode) or propose it (read-only).
3. In change mode, select one coherent batch (duplicate files, repeated fixture setup, or an overlapping family of cases). Trace imports, configuration, and runner consumers before consolidating or deleting files, helpers, or fixtures. For preserved contracts, run retained replacements and a representative fault or negative control before deleting cases; for an approved retired contract, verify the retirement and remaining consumers without inventing replacement coverage. Diagnose flaky tests rather than silencing them. Keep a recoverable diff; preserve unrelated work.
4. In change mode, run affected and dependent tests after each batch, then compare the suite against its fixed baseline for discovery, skips, coverage, detection, runtime, and diagnostics. Missing suite-wide execution or coverage evidence (including tooling) is a gap: it cannot support a whole-suite preservation claim or weaker protection. Where CI is configured, confirm it runs the retained checks and catches a plausible regression; otherwise prove detection through the native local runner without adding CI. Re-rank after each verified stage and continue only while a supported gain is worth its cost. Update only the owning test contract or fixture docs needed.
5. For substantive work, including assessments, use [Quality validation](references/vstack/protocols/quality-validation.md), with [Code review](references/vstack/capabilities/code-review/REFERENCE.md) in review mode for medium and high tiers. Report `(baseline - current) / baseline × 100` against the original suite size, comparable runtime results, consolidated files and retained-protection mappings, target shortfall, and discovery or execution gaps. Assessment savings are projected, not achieved.
