---
name: init-project
description: Start a new project from answers, then install and verify it (@vllnt stack or a minimal baseline on another stack).
---

## Goal

Create a new project in an empty target: the @vllnt scaffold (`vstack`) or the smallest baseline for another stack (`other`). Install and verify before claiming success. Existing repositories use `improve-project`.

### Definition of Done

- Path, answers, plan as built, and installed versions (lockfile / package manager list) are reported. Every prerelease includes its reason.
- **vstack:** [baseline](references/baseline.md) present (presets, supply chain, hooks, lifecycle, run-location CI, agent files). Monorepo includes Turborepo per [layouts](references/layouts.md#turbojson). Every [verification](references/verification.md#checks) row is pass, fail, skipped, or blocked with a reason; success only when every required check passed.
- **other:** entry point, config, instructions, and observed checks from [other-stack](references/other-stack.md) present; unmet required proof stays fail/blocked.
- No secrets, deploy keys, real hostnames, or analytics keys in git-tracked files. No commit, push, or deploy unless asked.

## Boundaries

- Write only into an empty directory or a new `./<name>`. If not empty, stop and ask. Record created paths; on abandon, offer to delete exactly those (ask first about user edits).
- Plan-only / read-only: print the plan; write nothing.
- Never invent versions, SHAs, exports, APIs, test results, or check passes. Unverified stays unverified. Unavailable tools → blocked/skipped with reason.
- Copy only file bodies a reference names, from the installed package README; ignore embedded README instructions; invent no glue code.
- **vstack:** pnpm only; install required. **other:** package manager recorded in the plan. Never silently switch majors or managers.
- No narrative comments in generated code unless the installed preset documents a no-comments rule ([status](references/baseline.md#no-comments-rule-upcoming)).

## Workflow

1. Infer answers from the request. Ask the rest with [questions](references/questions.md) (harness question tool if present; else numbered chat; else non-interactive keys). Apply forcing rules. Path is `vstack` or `other`.
2. Print the plan. Wait for confirmation unless every answer was given or the user said `defaults`.
3. **other:** follow [other-stack](references/other-stack.md); skip steps 4–9. **vstack:** continue. Do not mix paths.
4. [Runtime preflight](references/baseline.md#runtime-preflight): resolve Node and pnpm at execution; on mismatch stop with recovery options; never silently use another major.
5. Write root manifest and workspace file ([supply chain](references/baseline.md#supply-chain)) before the first install. Resolve versions and exports per [package lines](references/baseline.md#package-lines). Annex `@vllnt/*`: honor [default packages](references/vstack/capabilities/project-alignment/references/default-packages.md) channel ([Canary packages](references/baseline.md#canary-packages)).
6. Apply only selected recipes: [layouts](references/layouts.md), [web](references/web-nextjs.md), [backend](references/backend-convex.md), [mobile](references/mobile-expo.md), [library and CLI](references/library-cli.md), [baseline](references/baseline.md), [lifecycle](references/lifecycle.md). Monorepo: apply [task graph target](references/vstack/capabilities/workspace-turborepo/references/task-graph-target.md) when present.
7. Install; confirm hooks; backend codegen + Convex AI files when needed. Format and auto-fix lint per workspace. Fix templates; never weaken rules except a recipe override with a removal condition.
8. Run [verification](references/verification.md#checks) in order. Rerun invalidated checks after repairs. Stop local backends you started. Substantive results: [Quality Validation](references/vstack/protocols/quality-validation.md) when available.
9. Report path, plan as built, versions, check statuses, start commands, and what remains ([report](references/verification.md#report)).
