---
name: plan-work
description: Maintain a read-only planning session that returns an actionable plan without local or remote side effects.
---

## Goal

Return an actionable plan without local or remote side effects. Execution resumes only with explicit authority for the stated scope.

### Definition of Done

- Scope, facts, assumptions, gaps, owners, interfaces, and criteria are explicit.
- The plan has ordered work, dependencies, outcomes, future checks, risks, and recommendations.
- Review and critique converge or name the exact remaining decision or discriminating check.
- No local or remote mutation, execution, or boundary bypass occurred.
- Current validation accepts the plan; no required finding remains.

## Boundaries

- Do not write state, run unbounded-effect tools, or delegate around the read-only boundary. Agreement on a plan is not execution authority.

## Workflow

1. Inspect only safely readable evidence. Resolve outcome, scope, constraints, applicable instructions, loaded principles, and the plan validation contract.
2. Produce the simplest ordered work with dependencies, outcomes, future checks, risks, and recommendations. Decide reversible planning details from evidence.
3. For consequential unresolved choices, give options, recommendation, consequence, and the exact decision needed. Do not ask for routine confirmation.
4. For substantive plans, use `capability-quality-validation` in read-only mode. Otherwise self-assess, collect distinct review and critique, triage findings, improve the plan, and renew affected verdicts until acceptance.
5. Revise only after changed evidence or a discriminating check. On unchanged evidence, change approach or return the cause, options, recommendation, consequence, and next action.
