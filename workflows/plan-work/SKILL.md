---
name: plan-work
description: Maintain a read-only planning session that returns an actionable plan without local or remote side effects.
---

## Goal

Return an actionable plan without local or remote side effects. Execution resumes only with explicit authority for the stated scope.

### Definition of Done

- Scope, facts, assumptions, gaps, owners, interfaces, and criteria are explicit.
- The plan is proportional, not exhaustive: ordered work, dependencies, outcomes, future checks, risks, and recommendations, with detail only for the first verifiable steps and their proof.
- Reversible choices are decided and noted; other open forks are settled by a discriminating check, or the exact remaining decision is named with a recommended answer.
- No local or remote mutation, execution, or boundary bypass occurred.
- Current validation accepts the plan; no required finding remains.

## Boundaries

- Do not write state, run unbounded-effect tools, or delegate around the read-only boundary. Agreement on a plan is not execution authority.

## Workflow

1. Inspect only safely readable evidence. Resolve outcome, scope, constraints, applicable instructions, loaded principles, and the plan validation contract.
2. Produce the simplest ordered work with dependencies, outcomes, future checks, risks, and recommendations. Plan only as deep as the next decision needs: detail the first verifiable steps and their proof, outline the rest, and stop when the next step and its proof are clear. For code work, use [Code review](references/vstack/capabilities/code-review/REFERENCE.md) in plan mode to name the applicable perspectives, the runnable proof for each, and any missing proof script or check to add; if unavailable, name them directly. Tag each baseline row universal, conditional, or optional with its source. Trace each planned topology to its files, commands, and verification target. Decide each reversible choice by lowest lifetime cost (fastest verified delivery, simplest long-term maintenance, best developer and agent experience) and note it; skip option matrices for them.
3. For a consequential choice that evidence or a discriminating check cannot settle and that needs the user (missing authority, access, irreversible or high-risk effect, or preference), return one batched question set with options, a recommended answer, the consequence, and the exact decision needed. Do not ask for routine confirmation.
4. For substantive plans, use [Quality validation](references/vstack/protocols/quality-validation.md) in read-only mode with the scope, candidate, and evidence. If unavailable, self-assess against evidence, settle open questions with a permitted read-only discriminating check, and report missing independence; name any prototype or check to run once execution is authorized.
5. Revise only after changed evidence or a discriminating check. On unchanged evidence, change approach or return the cause, options, recommendation, consequence, and next action.
