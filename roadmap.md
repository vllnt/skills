# Vstack Skills Roadmap

Current work and proposed extensions. The [catalog](llms.txt) owns the skill inventory. A source review is not a consumer execution, runtime startup test, or published release.

## Current decisions

- Human workflows, internal capabilities, and mandatory principles have distinct owners.
- Thinking, Orchestration, and Collaboration replace the single principle entry. Synchronization belongs to Orchestration.
- The workflow owns its outcome and convergence. Capabilities return bounded evidence; current proof is reused across handoffs.
- Vstack prioritizes compatible [vllnt packages](references/vstack.md) through live discovery, not a maintained package list.
- User/project/nested rules own configuration and permissions. Public examples contain no private operational evidence.
- Keep repository-local maintenance under `.agents/` intentionally public and separate from the installable catalog.

## Current update

| ID | State | Result / remaining evidence |
|---|---|---|
| F01 | Implemented | Concise authoring, ownership, naming, and convergence rules. |
| F02 | Reviewed | Individual skills, references, callers, and public catalogs updated. |
| F03 | Implemented | Manage Rules covers user/project/nested scope and intentional overrides. |
| F04 | Reviewed | Independent contract, composition, behavior, ownership, simplicity, and resilience passes; required findings repaired and affected checks repeated. |
| F05 | Partial | Isolated Manage Rules and Plan Work tasks executed; remaining consumer tasks stay planned. Source scenarios are not live execution of every skill. |
| F06 | Planned | Prepare a separately authorized release after merge; use the existing release process. |
| F07 | Implemented | Build Project and Improve Project share alignment and package evidence with standalone fallback. |
| F08 | Implemented | Discover scoped source/registry inventories, latest/canary metadata, compatibility, and coverage gaps at execution time. |
| F09 | Reviewed | Infrastructure posture and cost capabilities provide bounded assessments without claiming unobserved recovery or savings. |
| F10 | Reviewed | Mode-specific DoD, requested delivery endpoint, assessment/target distinction, and bounded rechecks. |
| F11 | Reviewed | Lightweight principles and simplified annexes; preserve necessary domain proof while removing duplicate process. |
| F12 | Local checks passed | Public-content review and validator failure fixtures passed. Hosted CI and branch mergeability are checked on the PR before handoff. |

## Quality feedback loop

The shared `capability-quality-validation` owns criteria, self-assessment, review/critique, triage, and renewed acceptance. Workflows supply domain criteria from the request, applicable rules, and principles before work. Planning validates a plan; assessment validates a report; implementation validates the changed artifact. Direct checks remain sufficient for mechanical changes.

| ID | State | Result / remaining evidence |
|---|---|---|
| F13 | Reviewed | Integrate the shared loop into 17 substantive workflows plus their issue-delivery handoff, mandatory orchestration, and skill maintenance; exercise missing proof, stale verdicts, read-only modes, and disagreement. |

## Agent-facing templates

| ID | State | Result / remaining evidence |
|---|---|---|
| F14 | Reviewed | All public skills and the local maintainer use family templates. Structural failure fixtures and independent contract, behavior, simplicity, tooling, and full-chain reviews pass; mode propagation and single-pool ownership were corrected. |

## Established structure

N01–N04 established caller-based names, public category placement, canonical references, and catalog validation. N05 records the earlier source-review pass; the current candidate is evaluated under F04. Historical acceptance does not establish acceptance of later changes.

## Principles and Vstack integration

| ID | State | Next acceptance |
|---|---|---|
| V01 | Implemented | Three non-overlapping mandatory entries; concise context budget and no task workflow sections. |
| V02 | Planned | Verify automatic session loading in each selected runtime. Collection bootstrap, flat installation, and standalone skill use are separate cases; descriptions alone are not loaders. |
| V03 | Planned | Verify Vstack profile binding through Manage Rules on user/project/nested instructions without duplicating profile contents. |
| V04 | Proposed | Evaluate Deliver Package only for a distinct registry publication/channel/receipt outcome, reusing changelog and readiness. |
| V05 | Proposed | Evaluate Deliver Deployment for environment-specific rollout, recovery, and observed health. |
| V06 | Proposed | Evaluate Manage Automations for recurring-task lifecycle, deduplication, notifications, and observed runs. |
| V07 | Planned | Execute build/alignment on contrasting consumers with current package discovery, canary policy, compatibility, and preserved behavior. |

Prioritize runtime and consumer evidence over new wrapper skills. Runtime integration changes belong to an explicitly selected host configuration, not every portable skill.

## Product and log analysis — proposed, not implemented

`capability-product-analysis` would compare intended journeys with code, configuration, and observed behavior. It would return contradictions, missing evidence, and acceptance cases; architecture, UI, and strategy retain their existing owners.

`capability-log-analysis` would discover service/environment bindings from consumer rules and configuration, read authorized sources within a finite time window, and return failures plus instrumentation gaps. It must keep environments separate, sanitize payloads, and expose pagination, retention, sampling, truncation, and access limits. Missing logs never prove absence of errors.

Reuse `plan-issues` for evidence-backed drafts and root-cause deduplication, and `manage-issues` for authorized hosted changes. A logs question can finish with its evidence report; product analysis and issue creation are not mandatory stages.

| IDs | State | Work / acceptance |
|---|---|---|
| L01–L02 | Proposed | Define then implement provider-neutral log discovery, identity, collection, interpretation, and bounded access. |
| L03 | Proposed | Exercise denied sources, duplicate environment names, truncation, retention gaps, empty samples, timeouts, and sensitive payloads. |
| P01–P02 | Proposed | Define then implement product coherence without duplicate architecture/UI review or invented strategy. |
| P03 | Proposed | Exercise intent/code mismatch, unclear intent, missing runtime proof, and contrasting stacks. |
| I01–I02 | Proposed | Extend issue inputs; distinguish instrumentation gaps from incidents, deduplicate existing issues, and verify selected writes. |
| I03–I04 | Proposed | Independently review the chain and update public examples/catalogs; preserve standalone use. |

## Maintenance

1. Preserve task IDs and actual decision history; update evidence after work, not before.
2. Keep implemented, reviewed, consumer-tested, runtime-tested, and released states distinct.
3. Proposals identify future work; they do not authorize external actions.
