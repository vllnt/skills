Load this file when scaffolding or changing what every project shares: package versions, TypeScript, ESLint, Prettier, git hooks, supply chain, changelog, ignore files, agent files, and baseline scripts. [Lifecycle](lifecycle.md) owns run location, CI, pull requests, releases, deploys, and parallel worktrees.

This file states requirements. Take configuration keys, flags, and file formats from each tool's current official documentation.

## Package lines

No version is written in this skill. Resolve every package at install time from the registry. For a package outside `@vllnt/*`, prefer the newest non-prerelease at least 7 days old; `@vllnt/*` is exempt from that age gate. The [default packages](vstack/capabilities/project-alignment/references/default-packages.md) annex names preferred packages only — never channels or versions.

### Resolve versions

1. Write the [supply-chain policy](#supply-chain) before the first `pnpm add`: in `pnpm-workspace.yaml` for a single app, and in the full workspace file (`packages:`, `catalog:` and that policy, see [Monorepo](layouts.md#monorepo)) for a monorepo.
2. Add packages by name, without a version (`pnpm add next`). Under the release-age policy, pnpm installs the newest release that is old enough and records a range.
3. Respect published peer ranges. When a selected package peers a dependency (for example, the `@vllnt` presets peer `typescript`, `eslint`, and `prettier`), read the range from the registry at run time and add the newest version inside it. Never let a newer major break a preset's peer range.
4. Do not pre-pin exact versions read from the registry: the newest release may be too young, and the install then fails. The exceptions are prereleases (see [Resolve release](#resolve-release)) and tools that need an exact version, such as `packageManager`.
5. If a package resolves to nothing, stop and ask.
6. After installing, report the versions actually installed, read from the lockfile or the installed package list.

### Runtime preflight

- Node: `.node-version` holds the newest Node release at least 7 days old, read from the official Node.js release index. It must also satisfy every selected package's `engines.node`. Workspace `engines.node` sets that major as the minimum.
- pnpm: `packageManager` holds the exact newest pnpm release at least 7 days old. Before installing, confirm from the current pnpm documentation that this version supports every [supply-chain](#supply-chain) setting; if one is unsupported, stop and report.
- The installed Node major and pnpm version must match. On a mismatch, report it and stop with recovery options: activate the resolved versions (for pnpm through Corepack, with a writable cache directory when the default is read-only), or have the user choose an installed version that still meets every requirement above. Never silently use another version.

### Check exports

Before generating an import from a package subpath, read the published `exports` map of the version you install and confirm `./<sub>` exists. The map proves only that the subpath exists: before generating a call, confirm each named export in the installed package's `.d.ts`. Published versions often lag the source repositories, and some subpaths shown in READMEs exist only on canary builds.

### Resolve release

At execution, query the registry (dist-tags, version list, publish times). Prefer the newest non-prerelease / LTS that satisfies peers and policy. If none exists and the user selected the feature, install the newest usable prerelease as an exact version. Do not invent "stable" or "canary-only" from this skill. Compare publish times; do not trust `latest` alone. Check exports against the chosen version. Report any prerelease and its reason under "Prereleases" in the generated `AGENTS.md` (see [Agent files](#agent-files)).


### Not offered

- `@vllnt/convex-mcp` is deprecated. Use the MCP subpath of `@vllnt/convex-helpers` instead.
- `@vllnt/ui-core` is pulled in by `@vllnt/ui-native`. Never install it directly unless app code imports it.

## TypeScript

Every `tsconfig.json` you write extends a `@vllnt/typescript` preset, chosen by the workspace's role. Confirm the exact preset file names in the installed package's `exports`; there is no bare package export.

| Workspace role | Preset |
|---|---|
| Next.js app | Next.js preset |
| Convex (`convex/tsconfig.json`) | base preset, plus the options Convex documents |
| Expo app | Expo preset if exported; otherwise Expo's base config, then the base preset (later wins) |
| React shared package | React preset, no emit |
| Pure TS shared package (source-first) | base preset, with bundler resolution |
| Node service or CLI | Node.js preset, with source and output directories |
| Published library | Node library preset, with source and output directories |

The presets are strict, including unchecked indexed access and side-effect import checks (so CSS imports need a module declaration), and they list no ambient types: each consumer lists its own.

## ESLint

Write templates that pass the presets. Generated code must pass ESLint with zero warnings and `tsc` with no emit. After writing files and installing, run Prettier and ESLint's fix mode once per workspace to settle import order, key order and formatting, and rerun Prettier after the last installer or generator, since either can rewrite files such as `package.json`. Then the [verification checks](verification.md#checks) must pass with no further fixes. If an error remains, fix the template; never disable the rule. The one exception is a narrowly scoped compatibility override that a recipe prescribes, with its removal condition.

Generated source contains no narrative comments. The only exceptions are machine markers such as `"use client"`. Details are in [No-comments rule (upcoming)](#no-comments-rule-upcoming).

### Presets

Every ESLint config is `eslint.config.mjs`, spreads named preset arrays from `@vllnt/eslint-config` subpaths, and never imports a `config` export. Confirm the preset names in the installed package's `exports` and README.

| Workspace | Presets |
|---|---|
| Next.js app | `nextjs` (+ `convex` and the backend override when it holds `convex/`) (+ `turbo` in a monorepo) |
| Backend package | `nodejs` + `convex` + the backend override (+ `turbo`); `base` wires no test relaxations |
| Expo app | a React Native preset if exported, otherwise `react` |
| React shared package | `react` |
| Pure TS package / Node | `nodejs` |
| Large monorepo boundaries | `boundaries`: opt-in only, needs element definitions |

### Lint-derived rules

The presets set every rule to an error, and the installed preset is the authority: read its README and the effective config rather than restating its rules. The ones that shape every template:

- File, folder, and identifier names, abbreviations, and test-file suffixes follow [Naming](layouts.md#naming).
- Type aliases instead of interfaces, no enums, and no `null` outside `.tsx`.
- Small functions with few parameters and shallow nesting, and no loop statements; tests follow the same rules except the function-size limit.
- Sorted imports, exports, and object keys, and Prettier formatting, all as lint errors.
- Next.js API route files export only HTTP-verb handlers.
- A flat-config override replaces a rule's options rather than merging them, so override only what a recipe prescribes.

### No-comments rule (upcoming)

Status: upcoming. The no-comments lint rule is **not published** in `@vllnt/eslint-config`. The policy below applies now to everything you generate; the enforcement does not exist yet.

Policy:
- No narrative comments, whether `//` or `/* */`.
- Explain with names and small functions, or with TSDoc `/** ... */` on exported API when a name cannot carry the meaning.
- Machine markers are allowed: `eslint-*` directives with a reason, `@ts-expect-error` with a reason, `prettier-ignore`, `/// <reference ... />`, `#__PURE__`.

Enforcement:
- At scaffold time, read the installed `@vllnt/eslint-config` CHANGELOG and README.
  - Enable a no-comments rule only if the installed preset documents one, exactly as documented. A rule that checks comment prose quality is not a no-comments rule.
  - Otherwise add nothing and report the rule as upcoming. Never copy a custom rule into the project: a copy becomes per-project maintenance.
- Templates already contain zero comments, so turning the rule on later is free.
- The generated `AGENTS.md` states the policy.

Expected contract of the upstream rule (unpublished, unverified), so templates stay compatible:
- It reports `Line` and `Block` comments, except the machine markers above and TSDoc blocks attached to exported declarations.
- It applies to `.ts`, `.tsx`, `.js` and `.mjs` files, scripts and config files included.

## Prettier

- Prettier defaults, plus prose wrapping always on and trailing commas everywhere.
- The ignore file covers the lockfile, generated code, build output and caches, `AGENTS.md` and `CLAUDE.md` (they hold tool-managed blocks), the AI and skill files that Convex's `ai-files` command writes, and `CHANGELOG.md`. If the format check flags another tool-written file, add it.
- `format:check` runs in `verify` and CI. ESLint already fails on formatting inside linted files; `format:check` covers JSON, Markdown and YAML.

## Git hooks

Local verification is the gate of record. CI only confirms; it is not the first place to learn about lint, type, or test failures.

- No hook manager. A `prepare` script points git's hooks path at the tracked `.githooks/` on install, and tolerates checkouts without git. Hooks work in every worktree (shared repo config; [check 15](verification.md#checks)).
- `pre-commit` stays ~1s and holds only irreversible checks: refuse env files other than `.env.example`, whitespace errors in the staged diff, secret scan of staged changes (`gitleaks` or equivalent). Scanner is a documented prerequisite; missing → fail closed / gate blocked. Never put `verify`, lint, typecheck, test, or build here.
- `pre-push` runs the local gate: monorepo → `pnpm verify:changed` (affected from merge-base of the push; full graph when the base is missing or a root input changed — same rules as [task graph](vstack/capabilities/workspace-turborepo/references/task-graph-target.md)); single app → `pnpm verify`. Fail closed. Do not push with a red local gate.
- Both hooks honor one emergency opt-out variable and are executable. Commits stay fast; pushes carry the proof so CI can stay thin.

## Supply chain

Enforce, in `pnpm-workspace.yaml` (single app and monorepo alike), with the setting names from the current pnpm documentation:

- A 7-day minimum release age, with `@vllnt/*` exempt. First-party `@vllnt/*` releases come from provenance-signed CI, and their canaries are usually younger than 7 days.
- Refuse versions whose publish trust is weaker than earlier versions.
- Block git and tarball dependencies deep in the tree.
- Fail the install when a dependency's install script has not been reviewed, and keep an explicit allow or deny list of reviewed build scripts.

Rules for keeping it:
- When install fails on an unreviewed build script, review it and add the package to the build-script list, denied unless the package does not work without its script. Each entry gets a reason in `AGENTS.md`.
- Every later exception gets a reason in `AGENTS.md`: an extra exclude, an override or a patch. A patch also needs its removal condition.
- When the trust policy skips a downgraded version and no mature version remains, exclude only that package's newest mature skipped version from the trust check, with the reason and removal condition in `AGENTS.md`. Never loosen the trust policy or the release-age gate.
- Do not exempt `convex` or `@convex-dev/*`: pnpm then installs the newest version that is at least 7 days old.
- Never write exact versions into the release-age exclude list; they go stale on every bump.
- No `.npmrc` is needed.

## Mandatory primitives

Cheap at creation and costly later, so every project gets them. Each has an owner section and a pass check.

| Primitive | Requirement | Owner | Pass check |
|---|---|---|---|
| Typed configuration | Each app validates every variable it needs at start-up and names the first missing or invalid one. The backend reads variables through one typed module inside handlers, and `health` and `deploy` refuse when a required deployment variable is unset | [web](web-nextjs.md#files), [mobile](mobile-expo.md#backend-wiring), [Convex rules](backend-convex.md#convex-rules) | Starting an app, or running `deploy` or `health`, with a required variable unset fails and names it |
| Input boundaries | Route handlers, server actions, and parsers of outside responses validate input with a schema; backend functions use Convex validators | [web](web-nextjs.md#files), [Convex rules](backend-convex.md#convex-rules) | A test sends invalid input and gets a client error |
| Structured logging | `@vllnt/logger` everywhere and `console` banned by every workspace's lint config. The logger does not redact, so one wrapper logs only allowlisted fields and drops headers, cookies, tokens, bodies, and identity | [web logging](web-nextjs.md#logging), [Convex rules](backend-convex.md#convex-rules) | Lint fails on `console`; a test logs an event carrying a fake token and cookie and shows a line with level and fields but neither value |
| Error path | Error page, not-found page, global error boundary, and one pluggable error sink for each deployed surface | [web](web-nextjs.md#files) | A test forces an error and asserts a fake sink received it; the [end-to-end smoke](web-nextjs.md#end-to-end-smoke) shows the pages |
| Security headers | CSP, framing restriction, `nosniff`, referrer policy on every web response | [web](web-nextjs.md#files) | The end-to-end smoke |
| Health | A health query and route; a container image declares a health check on it, and the self-hosted stack declares one per service | [Lifecycle](lifecycle.md#lifecycle), [web deploy](web-nextjs.md#deploy), [self-hosted](backend-convex.md#self-hosted-backend) | `health` exits 0 against the running stack; the image and compose file declare the checks |
| Accessibility | The presets' accessibility lint in UI workspaces, plus an automated page check | [web](web-nextjs.md#end-to-end-smoke) | The end-to-end smoke reports no critical violations |
| Secret scanning | Pre-commit scan, a CI scan with the same scanner and rules, and the host's push protection when it offers one | [Git hooks](#git-hooks), [CI](lifecycle.md#ci) | The hook rejects a planted inert credential ([check 15](verification.md#checks)), and the CI step runs that scanner and configuration |
| Vulnerability gate | CI fails on high-severity advisories in production dependencies, and fails when the audit cannot run | [CI](lifecycle.md#ci) | Locally the gate exits 0 on the scaffold; in a scratch copy, a dependency release with a known high advisory makes it fail (capacity permitting, otherwise unverified) |
| Change hygiene | PR template; changelog entry required by CI for source changes; branch protection with required review and checks | [Lifecycle](lifecycle.md#lifecycle), [CI](lifecycle.md#ci) | CI fails a source change without a changelog line; the host shows the protection once applied |
| Community files | README, SECURITY.md, and CONTRIBUTING.md always; LICENSE when public; CODEOWNERS when there is more than one maintainer | [Root documents](#root-documents) | The files exist with the required content, and every command they name is a real script |
| Schema migrations | Expand, migrate, contract, with a tested backfill | [Convex rules](backend-convex.md#convex-rules) | Review: no required field is added to an existing table in one release |

## CI

[Lifecycle](lifecycle.md#ci) owns the CI requirements.

### End-to-end job

With a web app, the [end-to-end smoke](web-nextjs.md#end-to-end-smoke) is generated with its dependency, config, specs, `test:e2e`, and CI job together. The CI job repeats the setup steps (jobs do not share build output), uses the primary job's placeholder environment except the backend URL, which points at the backend the smoke requires, builds the web app, installs one browser, and runs `test:e2e`. The smoke's spec files are `tests/e2e/*.spec.ts` in both layouts, and the unit test runner never includes them. It stays outside the default pre-push gate ([Tests](#tests), [CI](lifecycle.md#ci)).

## Changelog

`CHANGELOG.md` follows the current Keep a Changelog format with SemVer, and starts with an `[Unreleased]` section and an `Added` line for the scaffold. Lines are written by hand; the [release step](lifecycle.md#lifecycle) moves them under a version heading with the release date. No changesets and no release bot.

`AGENTS.md` rule: a user-visible change adds a line under `[Unreleased]`.

## Tests

Goal-oriented. Agents choose runner config from the surface’s current docs; this section states outcomes, not file recipes.

### Goal

Every package and app has its own test setup. Tests sit close to the code they protect. Scaffolded and owned public behavior has strong coverage, including failure paths. Agents extend by copying nearby examples — not by inventing a parallel test layout.

### Definition of Done

- Each workspace that ships code has a working `test` script; root `verify` / `verify:changed` runs those tests.
- Discovery is by glob (no hand-listed files). Layout is consistent inside a package so the next test has an obvious neighbor to copy.
- Every seeded public behavior has at least one success case and one failure/denial/edge case that would catch a real regression.
- New public exports or handlers land with tests in the same change. Untested public surface is a gap, not done.
- Coverage is maximized for owned behavior within capacity (≤2 workers). If the stack’s coverage tool is wired, treat regressions in coverage of owned code as fail; unlabeled drops are not allowed. Missing coverage tooling is an evidence gap, not permission to skip tests.
- `pnpm test` (or turbo `test`) is green on day one and before push.

### Rules

- **Per package:** own runner config + scripts; do not rely on a sibling’s tests.
- **Colocate:** unit/examples next to the module or in that domain’s `tests/` folder (backend domains under `convex/<domain>/tests/`). App-level pure helpers: `*.test.ts` beside the helper or under the package’s agreed unit glob — pick one pattern per package and keep it.
- **Examples first:** scaffold ships small real examples agents (and humans) copy; do not add helpers only to inflate coverage.
- **Fail closed:** auth, env, validation, and CLI errors need negative tests. Flakes get diagnosed, not silenced.
- **No theater:** do not add dead code or test-only production routes for coverage.
- **Surface runners:** web/shared/library → Vitest (current docs); backend → Vitest + convex-test, no live backend; mobile → Expo’s test stack from `expo install`. The web [end-to-end smoke](web-nextjs.md#end-to-end-smoke) is required but outside the default pre-push gate ([lifecycle CI](lifecycle.md#ci)).
- **Capacity:** max 2 test workers; backend tests need no running Convex process.

## Lean defaults

- **Capacity:** heavy parallelism capped at 2 (task runner and test workers); builds one at a time after checks; caps are machine-wide across worktrees. Lower when free memory is low.
- Lint/compiler caches stay inside the worktree (see [Gitignore](#gitignore)).
- Dev servers bind to loopback on the worktree’s ports. Physical-device Expo may opt into LAN/tunnel; record opt-in in `AGENTS.md`.
- One browser for e2e when that recipe exists. No Storybook, bundle analyzers, or extra quality tools by default.
- Local gate of record: `verify` / `verify:changed` before push and before `pr`. CI confirms via the same scripts + cache, plus its [CI-only gates](lifecycle.md#ci); it is not the first lint/type/test loop.
- No per-package task overrides, and no hand-listed test files: test runners find tests by glob.
- Convex local backend on demand only.

## Gitignore

Ignore dependencies, build and framework output, caches and test reports, compiler build info, generated framework declarations, local backend data, every `.env` file except `.env.example`, worktree-local settings, an in-repository worktree directory when used, and OS metadata.

- `convex/_generated/` is committed, so it is not ignored.
- Codegen writes `.env.local` with backend credentials. It stays ignored; never commit it.

## Agent files

`AGENTS.md` is the single source of truth for agent instructions. `CLAUDE.md` is a one-line import of it (`@AGENTS.md`), so harnesses that read only `CLAUDE.md` see the same content. It is not a symlink, because symlinks break on some checkouts.

`AGENTS.md` is generated for every project, kept under about 120 lines, and accurate: every command it lists exists ([check 14](verification.md#checks)), and every constraint is a rule the scaffold sets up or a fact of the generated project. Drop rows and lines for surfaces and features the project does not have. It contains, in order:

1. The project name and one sentence on what it is.
2. **Stack:** one row per surface with its path and technology; the package manager and Node version files; **Prereleases:** each exact prerelease with its reason, or "none".
3. **Commands:** prerequisites (the secret scanner the pre-commit hook needs), install (which also installs the hooks), `dev`, `verify` and `verify:changed` (what CI runs, plus its CI-only gates), `format`, and the [lifecycle scripts](lifecycle.md#lifecycle).
4. **Constraints:** local verify first (pre-push / `pr`); done means the local gate passed — CI is not the first lint/type/test signal; tests per [Tests](#tests) (per-package setup, colocated examples, maximize owned coverage, failure paths required); strict TypeScript with no escape hatches or unexplained suppressions; no narrative comments (with the [upcoming rule](#no-comments-rule-upcoming) status); `@vllnt/logger` through the allowlisting wrapper instead of `console`, never logging headers, cookies, tokens or identity; fail closed, with the failure path tested; backend rules, components only in `convex.config.ts`; `.env.example` names only; every user-visible string in every catalog; 7-day release-age gate with `@vllnt/*` exempt and reasons for exceptions; changelog line for every user-visible change; branch, PR, merge — never push default branch or rewrite shared history; localhost dev servers unless an opt-in is recorded.
5. **Lifecycle:** the steps from [Lifecycle](lifecycle.md#lifecycle), one line each, with the run location.
6. **Parallel work:** one agent per worktree; never edit the main checkout; create and remove worktrees only with `wt:new` and `wt:rm`; rebase on the default branch before opening a PR; remove the worktree after merge; heavy work stays under the shared machine-wide cap.
7. **Convex rules:** the bullets of [Convex rules](backend-convex.md#convex-rules), verbatim.
8. **Layout:** the project tree from [single app](layouts.md#single-app) or [monorepo](layouts.md#monorepo).

When a framework writes its own managed block into `AGENTS.md`, commit it once and never hand-edit it. Examples: Convex `ai-files`, or an agent-rules block that the Next.js dev server adds. In a monorepo, `ai-files` writes into `packages/backend/`; the root `AGENTS.md` and `CLAUDE.md` stay human-owned.

### Root documents

- `README.md`: the project name, its one-sentence purpose, and setup, run, verify, and deploy sections whose commands are real scripts.
- `SECURITY.md`: a private reporting channel (the host's private vulnerability reporting when public; the owner's chosen contact when private) and a response time. Tell the user to enable private reporting in the repository settings.
- `CONTRIBUTING.md`: the verify command, the lifecycle from task start to merge, and the review rule.
- `LICENSE` when public: the SPDX license text for the chosen id, with the current year and the copyright holder, matching the manifest's license field. Ask for the holder; default to the owner.
- `CODEOWNERS` when the user names more than one maintainer, covering at least the workflow and security files.

## Baseline scripts

Every package or app defines the same script names, so agents, hooks and CI never guess:

| Script | Where | Does |
|---|---|---|
| `dev` | each app, backend | the framework's dev server, bound to localhost on the worktree's port |
| `build` | web, mobile (Expo export), library, CLI, root | the framework build; at the root, through Turbo one build at a time; library and CLI from the build tsconfig |
| `lint` | every workspace | ESLint with zero warnings, its cache inside the worktree |
| `typecheck` | every workspace | `tsc` with no emit, covering every tsconfig in the workspace |
| `test` | every workspace | the surface's test runner with at most 2 workers |
| `format`, `format:check` | single-app root or monorepo root | Prettier write / check |
| `verify` | single-app root or monorepo root | `format:check`, then lint, typecheck and test (and `check:expo` when mobile exists), then build |
| `verify:changed` | monorepo root | same contract as `verify`, but Turbo-affected from merge-base (full graph on missing base or root-input change); used by pre-push |
| `check:expo` | mobile app | Expo's dependency alignment check |
| `codegen` | wherever `convex/` lives | one-shot Convex code generation |
| `prepare` | single-app root or monorepo root | points git at `.githooks/` |

A backend-only single app has the same set without `build`. Its `verify` is `format:check`, lint, typecheck and test. The root also defines the [lifecycle scripts](lifecycle.md#lifecycle). In a monorepo, every task runs through Turbo as the [task graph target](vstack/capabilities/workspace-turborepo/references/task-graph-target.md) requires.

The library and CLI recipes are in [library-cli.md](library-cli.md).

## Why these defaults

- Root tool scripts live in `scripts/`, never in a workspace glob, so a script folder is never mistaken for a package.
- One package scope keeps imports and Turbo filters consistent.
- Every file under `convex/` deploys as a module, so domain code lives in `convex/<domain>/` and test-only code stays in test files or outside `convex/`.
- A file and a folder with the same stem make the module path ambiguous.
- Each dependency is declared in the package that imports it, because pnpm's isolated layout does not share a sibling's dependencies.
- `.env.example` per app with names only, and typed start-up validation of every variable, so misconfiguration fails at start, naming the variable.
- Secret split: backend secrets live on the backend deployment, each deploy key only in the host's settings per environment, and backend URLs come from the public environment, never hard-coded.
- No staging tier by default: the tiers are `dev`, `preview`, and `production`.
- Nothing environment-specific in committed config: hostnames, project ids, and analytics keys stay out of committed files.
- Tests follow [Tests](#tests): per-package setup, colocated examples, owned behavior + failure paths covered, `pnpm test` green on day one.
- Public variables are read by their full literal name: Next.js and Expo inline only direct references, so a dynamic lookup returns nothing.
