# Family Templates

Replace placeholders with domain instructions. For discoverable skills, preserve frontmatter `name` and a description explaining the result and trigger. Reference procedures have no frontmatter. Omit optional sections without a concrete failure to prevent. These are authoring templates, not extra runtime instructions.

## Workflow

```markdown
---
name: verb-subject
description: [Outcome and when to use this workflow.]
---

## Goal

[Concrete result, scope, and selected mode.]

### Definition of Done

- [Observable result and its required evidence.]
- [Supported behavior or contract preserved.]
- [Mode-specific validation accepts the current result.]

## Boundaries

- [Specific intrinsic limit and permitted alternative.]

## Workflow

1. Resolve inputs and criteria from the request and applicable instructions.
2. [Inspect the relevant sources; identify material uncertainty.]
3. [Produce the smallest authorized result.]
4. [Validate with domain checks and the shared quality loop when relevant.]
5. [Repair and renew affected verdicts, or report the unmet criterion.]
```

## Reference procedure

```markdown
## Contract

- Input: [Required scope, candidate, context, and criteria.]
- Output: [Bounded result, evidence, and coverage gaps.]
- Effects: [Read-only inspection or specific supported changes.]

### Acceptance

- [The result satisfies the caller's criteria.]
- [Evidence applies to the current candidate and environment.]
- [Unverified requirements and next actions are explicit.]

## Procedure

1. Resolve inputs from the caller and inspected sources.
2. [Perform the domain operation.]
3. [Check the result at the relevant layer.]
4. Return the result, evidence, and remaining work.

## Pitfalls

- [Known false inference or failure → required check or alternative.]
```

## Mandatory

```markdown
---
name: vllnt-subject-principles
description: [Activation condition and cross-task behavior.]
---

## Principles

- [One portable decision rule with an observable effect.]
- [Another distinct rule; no task procedure or completion gate.]
```

## Authoring checks

1. Separate identity/trigger, outcome/contract, acceptance, and procedure; remove repeated titles and semantic duplication.
2. Keep decisive evidence checks in the owning skill. A missing mandatory skill or procedure reference must not silently remove a necessary check.
3. Describe specific failures and alternatives instead of generic warnings. Project permissions stay in consumer instructions; loading a skill grants no authority.
4. Exercise success, missing evidence, contradictory sources, unavailable tools, and assessment-only requests. Inspect actions as well as the answer; tests and sources must exist, not be invented.
5. Link workflow dependencies to packaged `references/vstack/...` paths with a loading condition. Canonical procedures live under `references/`; regenerate distribution copies instead of editing them.
6. Preserve a rule only when it changes a decision, action, verification, or result. Use examples and references only where they remove ambiguity.
