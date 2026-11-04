Load when path is `other`.

## Contract

- Input: confirmed plan (name, target stack, package manager, surfaces), empty target, mode (build or plan-only).
- Output: minimal baseline or plan-only notes; observed check results or explicit gaps.
- Effects: build mode may write and run checks. Plan-only writes nothing.

### Acceptance

- Target stack, package manager, and constraints come from the request or answers — not assumed.
- Build: runnable entry point, config, instructions, and at least one observed entry check and one failure-path check, or blocked/skipped with reason.
- Plan-only: setup steps and checks listed; no edits.
- Missing proof is not a pass.

## Procedure

1. Resolve rules, permitted effects, and proof needs. If the target is not empty, stop.
2. Select the smallest package and runtime matrix with evidence. When installed, use [Project alignment](vstack/capabilities/project-alignment/REFERENCE.md) and [Stack packages](vstack/capabilities/stack-packages/REFERENCE.md). Load [TypeScript configuration](vstack/capabilities/typescript-configuration/REFERENCE.md), [ESLint configuration](vstack/capabilities/eslint-configuration/REFERENCE.md), [Workspace Turborepo](vstack/capabilities/workspace-turborepo/REFERENCE.md), or [Convex components](vstack/capabilities/convex-components/REFERENCE.md) only when that stack uses them. Without a reference, inspect manifests and registry evidence directly. Prefer [default packages](vstack/capabilities/project-alignment/references/default-packages.md) when compatible; resolve versions at execution.
3. Inspect generators and install scripts before use. Record overwrite risk. Do not run unreviewed install scripts.
4. Plan-only: return setup and checks; stop.
5. Build: create the minimal entry point, config, checks, and instructions. Exercise entry, one failure path, and runnable platform paths. Use `@vllnt/logger` / `@vllnt/analytics` only when the plan selects them and the stack is compatible.
6. Report installed versions, commands run, pass/fail/skipped/blocked per check, and gaps. Renew validation after repairs ([Quality Validation](vstack/protocols/quality-validation.md) when available).

## Pitfalls

- A README or mutable tag is not install proof. Verify the selected release and exports before generating imports.
- Do not claim Convex, Turborepo, or @vllnt presets unless the plan selected them and files exist.
