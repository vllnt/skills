# Vstack Skills Roadmap

Current work and proposed extensions. The [catalog](llms.txt) owns the skill inventory. A source review is not a consumer execution, runtime startup test, or published release.

## Current decisions

- The public catalog exposes only workflows and mandatory principles; repository-local maintenance is separate. Internal procedures are canonical references, bundled per workflow and loaded on demand.
- Thinking, Orchestration, and Collaboration replace the single principle entry. Synchronization belongs to Orchestration.
- The workflow owns its outcome and convergence. Reference procedures return bounded evidence; current proof is reused across handoffs.
- Vstack prioritizes compatible [vllnt packages](references/vstack.md) through live discovery, not a maintained package list.
- User/project/nested rules own configuration and permissions. Public examples contain no private operational evidence.
- Keep repository-local maintenance under `.agents/` intentionally public and separate from the installable catalog.

## Current update

- Session refocusing: implemented optional `improve-session` to recover the current contract, ground consequential claims, simplify the approach, and resume the same owner's authorized work. C91–C100 instruction-following simulations, repository checks, Skills CLI discovery, and isolated copy/link failure-recovery checks passed. Independent correctness and simplicity review passed; automatic runtime loading, live continuation behavior, and speed or hallucination-rate improvements remain unverified.

- Review efficiency: allow one independent reviewer to cover correctness and critique, match delegated checks to tools and authority, and renew only affected proof. Repository checks and independent correctness/critique passed, including source scenarios C75–C78 and isolated copied-distribution checks for all workflows. Runtime behavior and timing improvements are unmeasured.

- Collaboration handoffs: replaced three closing/reporting bullets with two explicit outcome and blocker principles, without adding a skill. Local checks and independent source review/critique passed, covering successful completion, missing access, unknown causes, bounded assessments, and remaining authorized work through instruction-following simulations. Automatic runtime loading remains V02.
- Delivery pre-push gates: discover project-defined checks and require current passing local evidence before issue-delivery pushes/PR writes and repair pushes. Repository checks and independent review/critique passed, including source scenarios for missing, stale, and remote-only proof and mode boundaries; no live consumer execution is claimed.
- Evidence-led simplification: require a supported maintenance cost and concrete alternative for simplification findings; compare overlapping test protection when tests change, using the existing pruning gate and mode-preserving workflow fallbacks. C83–C90 cover justified additions, necessary boundaries, safe replacement, unknown consumers, missing proof, and read-only modes. Local checks, isolated copies, independent source review/critique, and input-only instruction-following evaluations passed. Automatic host loading, live consumer behavior, and model-speed gains remain unverified.
- Root Skills CLI discovery: mark the local maintainer internal so it does not suppress recursive public-skill discovery. Regression checks cover the original one-skill failure and the corrected public inventory; remote root discovery requires this branch to merge.

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

The shared [quality validation protocol](references/protocols/quality-validation.md) owns criteria, self-assessment, review/critique, triage, and renewed acceptance. Workflows supply domain criteria from the request, applicable rules, and principles before work. Planning validates a plan; assessment validates a report; implementation validates the changed artifact. Direct checks remain sufficient for mechanical changes.

| ID | State | Result / remaining evidence |
|---|---|---|
| F13 | Reviewed | Integrate the shared loop into 17 substantive workflows plus their issue-delivery handoff, mandatory orchestration, and skill maintenance; exercise missing proof, stale verdicts, read-only modes, and disagreement. |

## Agent-facing templates

| ID | State | Result / remaining evidence |
|---|---|---|
| F14 | Reviewed | All public skills and the local maintainer use family templates. Structural failure fixtures and independent contract, behavior, simplicity, tooling, and full-chain reviews pass; mode propagation and single-pool ownership were corrected. |

## On-demand reference distribution

| ID | State | Result / remaining evidence |
|---|---|---|
| F15 | Reviewed | Public discovery exposes workflows and mandatory skills; internal procedures are on-demand references. Conditional bundles, isolated Improve UI/Build Project copy installations, and independent composition, ownership, and tooling review pass. Automatic runtime loading remains V02. |

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

A product-analysis reference would compare intended journeys with code, configuration, and observed behavior. It would return contradictions, missing evidence, and acceptance cases; architecture, UI, and strategy retain their existing owners.

A log-analysis reference would discover service/environment bindings from consumer rules and configuration, read authorized sources within a finite time window, and return failures plus instrumentation gaps. It must keep environments separate, sanitize payloads, and expose pagination, retention, sampling, truncation, and access limits. Missing logs never prove absence of errors.

Reuse `plan-issues` for evidence-backed drafts and root-cause deduplication, and `manage-issues` for authorized hosted changes. A logs question can finish with its evidence report; product analysis and issue creation are not mandatory stages.

| IDs | State | Work / acceptance |
|---|---|---|
| L01–L02 | Proposed | Define then implement provider-neutral log discovery, identity, collection, interpretation, and bounded access. |
| L03 | Proposed | Exercise denied sources, duplicate environment names, truncation, retention gaps, empty samples, timeouts, and sensitive payloads. |
| P01–P02 | Proposed | Define then implement product coherence without duplicate architecture/UI review or invented strategy. |
| P03 | Proposed | Exercise intent/code mismatch, unclear intent, missing runtime proof, and contrasting stacks. |
| I01–I02 | Proposed | Extend issue inputs; distinguish instrumentation gaps from incidents, deduplicate existing issues, and verify selected writes. |
| I03–I04 | Proposed | Independently review the chain and update public examples/catalogs; preserve standalone use. |

## Distribution notifications

| ID | State | Result / remaining evidence |
|---|---|---|
| D01 | Deployed | Main-push and manual notification to `vllnt/stack` use a fixed event and scoped credential. Hosted source run `35645334592` delivered a real notification; Stack run `35645345833` correctly held the workflow/script changes without writing an update. The reviewed baseline was accepted through Stack PR #3. Stack owns the downstream ordinary-update, merge, and no-op evidence. |

## Maintenance

1. Preserve task IDs and actual decision history; update evidence after work, not before.
2. Keep implemented, reviewed, consumer-tested, runtime-tested, and released states distinct.
3. Proposals identify future work; they do not authorize external actions.
