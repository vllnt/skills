---
name: improve-dx
description: Speed up verified work for developers and agents by improving native build, lint, script, and CI workflows without weakening checks.
---

## Goal

Help developers and agents finish work faster in authorized change mode: choose the highest-supported gain, change one bounded scope at a time, and optimize time to a verified result, not command duration alone. Agent experience (AX) means one discoverable command per task, fast deterministic checks, clear machine-readable errors, and small context.

### Definition of Done

- The revision, native tools, representative developer and agent tasks, required checks, baseline time to verified results, and requested targets are recorded.
- The selected scope has the strongest evidenced gain relative to effort and risk.
- Changed builds, lint rules, scripts, or CI still produce supported artifacts and diagnostics, propagate failures, and respect cache and permission boundaries.
- Developer and agent workflows reach verified results faster under comparable conditions, including setup, waiting, retries, and manual steps; neither shifts work to the other, and agent tasks keep AX. Unmeasured or merely simulated workflows remain unverified.
- Quality validation accepts the selected mode; achieved gain, tradeoffs, shortfall, and unverified gaps are explicit. An assessment makes no changes or test runs.

## Boundaries

- Remote workflow changes, paid infrastructure, privileged secrets, and deployments follow consumer authority. Measure locally or with authorized hosted evidence; missing provider proof stays unverified.

## Workflow

1. Resolve mode, scope, consumer rules, authority, target, and validation. Discover native tools, commands, and CI; impose no framework, runner, or provider. Baseline each representative developer and agent task separately, from defined start to verified endpoint, fixing revision, toolchain, workload, resources, cache state, units, and exclusions and separating queue from execution time and cold from warm runs. In read-only mode, run steps 1, 2, and 5.
2. Trace scripts, task prerequisites, artifacts, consumers, lint scope, CI triggers, critical path, selection, permissions, and caches. Rank opportunities by repeatable time saved to a verified result relative to effort and failure risk; if uncertain, take the cheapest discriminating measurement, or propose it in read-only mode. Use [CI optimization](references/vstack/capabilities/ci-optimization/REFERENCE.md) for CI changes, [Workspace Turborepo](references/vstack/capabilities/workspace-turborepo/REFERENCE.md) only when its runner applies, and [ESLint configuration](references/vstack/capabilities/eslint-configuration/REFERENCE.md) only for ESLint config. Without an applicable runner, inspect native scripts and required checks directly; a green run proves neither speed nor safety.
3. In change mode, apply the smallest measured fix: remove redundant setup, scripts, or interaction, fix task ordering, avoid repeated work without losing affected dependents, or improve trusted cache inputs and outputs. Preserve script interfaces, lint file scope, required CI check identities, and fail-closed behavior on failed, missing, cancelled, or unexpected skipped work. When affected work is unknown (deletion, missing base, task-graph gap), run the conservative full relevant validation. Never mask slow work by excluding files or tests, or let untrusted code poison privileged caches.
4. In change mode, re-measure each task under its baseline conditions, start to verified result. Compare cold/warm outputs, cache invalidation by changed source, locks, configuration, and environment, and deliberately failing native checks; record samples and variability. Verify CI selection and failure propagation where CI exists; otherwise use the native local path, adding no CI. Re-rank after each verified stage and continue only while another supported gain is worth its cost. Update owning configuration and documentation.
5. For substantive work, including assessments, use [Quality validation](references/vstack/protocols/quality-validation.md), with [Code review](references/vstack/capabilities/code-review/REFERENCE.md) in review mode for medium and high tiers. Report developer and agent time-to-result separately, command timings, any script-size reduction, targets missed, and remaining gaps. Stop short of any target requiring weaker required checks or diagnostics; assessment gains are projected, not achieved.
