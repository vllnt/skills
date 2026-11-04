Load this file when scaffolding or changing what every project shares: package versions, TypeScript, ESLint, Prettier, git hooks, supply chain, changelog, ignore files, agent files, and baseline scripts. [Lifecycle](lifecycle.md) owns run location, CI, pull requests, releases, deploys, and parallel worktrees.

This file states requirements. Take configuration keys, flags, and file formats from each tool's current official documentation.

## Package lines

No version is written in this skill. Resolve every package at install time from the registry. For a package outside `@vllnt/*`, prefer the newest non-prerelease at least 7 days old; `@vllnt/*` is exempt from that age gate. The [default packages](vstack/capabilities/project-alignment/references/default-packages.md) annex names preferred packages only — never channels or versions.

### Resolve versions

1. Write the [supply-chain policy](#supply-chain) before the first `pnpm add`: in `pnpm-workspace.yaml` for a single app, and in the full workspace file (`packages:`, `catalog:` and that policy, see [pnpm-workspace.yaml](layouts.md#pnpm-workspaceyaml)) for a monorepo.
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

Before generating `import x from "@vllnt/<pkg>/<sub>"`, read the published `exports` map of the version you install and confirm `./<sub>` exists. The map proves only that the subpath exists: before generating a call, confirm each named export in the installed package's `.d.ts`. Published versions often lag the source repositories, and some subpaths shown in READMEs exist only on canary builds.

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
| Backend package | `base` + `convex` + the backend override (+ `turbo`) |
| Expo app | a React Native preset if exported, otherwise `react` |
| React shared package | `react` |
| Pure TS package / Node | `nodejs` |
| Large monorepo boundaries | `boundaries`: opt-in only, needs element definitions |

### Traps

The presets set every rule to `error`. Templates must stay inside these limits:
- **File and identifier names:**
  - `unicorn/filename-case` wants kebab-case outside `.tsx` files.
  - `unicorn/prevent-abbreviations` rejects `env.ts`, `util.ts` and an identifier named `args`. Write `environment.ts`, `utils.ts` and destructured parameters instead.
- **Type style:** `type` aliases only (no `interface`), no `enum`, no `null` outside `.tsx`.
- **Size limits:** at most 3 parameters, nesting depth 3, and functions of at most 30 lines (70 in `.tsx`).
- **Loops:** no loop statements; use array methods.
- **Ordering:** imports are sorted by `simple-import-sort` groups, and object keys are sorted naturally.
- **Formatting:** Prettier is a lint error, using the repo's `.prettierrc.json`.
- **Next.js API routes:** route files under `app/api/**` may export only `GET`, `POST`, `PUT` and `DELETE` functions.
- **Flat-config overrides:** an override block *replaces* a rule's options rather than merging them. Do not override `no-restricted-syntax` or `@typescript-eslint/naming-convention` casually.

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

- No hook manager. A `prepare` script points git's hooks path at the tracked `.githooks/` on install, and tolerates checkouts without git. Hooks work in every worktree, because worktrees share the repository configuration ([check 15](verification.md#checks) proves it).
- `pre-commit` stays fast (about a second) and holds only checks that are hard to undo after a commit: refuse env files other than `.env.example`, check whitespace errors in the staged diff, and scan the staged changes for secrets with `gitleaks` or an equivalent scanner. The scanner is a documented prerequisite in `AGENTS.md`; when it is missing, the hook fails closed with the reason, and the scaffold reports the gate blocked rather than passed.
- `pre-push` runs `pnpm verify`.
- Both hooks honor one explicit opt-out variable for emergencies, and both are executable. Pushes stay slow on purpose and commits stay fast, so nobody reaches for the bypass flag.

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

## CI

[Lifecycle](lifecycle.md#ci) owns the CI requirements.

### End-to-end job

Optional. Generate an `e2e` job only when the project has a web app and the [optional Playwright setup](web-nextjs.md#end-to-end-optional) of the web recipe is generated with it (dependency, config, spec and the `test:e2e` script all together).
- It repeats the setup steps (checkout, pnpm, node, frozen install), because jobs do not share `.next`.
- It copies the `ci` job's `env` block, so the build sees the same backend URL placeholder.
- It builds the web app itself: `pnpm --filter <web> build` in a monorepo, `pnpm build` in a single app.
- It installs only chromium (`pnpm --filter <web> exec playwright install --with-deps chromium`, or `pnpm exec playwright install --with-deps chromium` in a single app) and runs `test:e2e` the same way.
- `playwright.config.ts` sets `webServer.command: "pnpm start"`, `workers: process.env.CI ? 1 : 2`, and a single desktop chromium project.
- `tests/e2e/home.spec.ts` asserts that the home page renders the project name.
- The web app adds `@playwright/test` as a dev dependency. `playwright.config.ts` sets `testDir: "tests/e2e"`, and vitest's `include` never matches `tests/e2e`.

## Changelog

`CHANGELOG.md` follows the current Keep a Changelog format with SemVer, and starts with an `[Unreleased]` section and an `Added` line for the scaffold. Lines are written by hand; the [release step](lifecycle.md#lifecycle) moves them under a version heading with the release date. No changesets and no release bot.

`AGENTS.md` rule: a user-visible change adds a line under `[Unreleased]`.

## Lean defaults

- **Capacity:**
  - Heavy parallelism is capped at 2 (task runner and test workers), and builds run one at a time, after the checks. The caps hold across every worktree on the machine (see [Parallel worktrees](lifecycle.md#parallel-worktrees)).
  - 2 is a default, not a law: lower it when a measured run hits low free memory.
- Lint and compiler caches stay inside the worktree, out of git and out of lint scope; [Gitignore](#gitignore) covers them.
- Dev servers bind to loopback (localhost) on the worktree's ports. Physical-device Expo development may opt into LAN or a tunnel explicitly; record the opt-in in `AGENTS.md`.
- One browser for end-to-end tests. No Storybook, bundle analyzers or extra quality tools by default.
- No per-package task overrides, and no hand-listed test files: test runners find tests by glob.
- `verify` is the one command that matches CI, and the pre-push hook runs it.
- The Convex local backend runs only on demand. Tests use convex-test, which needs no running backend.

## Gitignore

Ignore dependencies, build and framework output, caches and test reports, compiler build info, generated framework declarations, local backend data, every `.env` file except `.env.example`, worktree-local settings, an in-repository worktree directory when used, and OS metadata.

- `convex/_generated/` is committed, so it is not ignored.
- Codegen writes `.env.local` with backend credentials. It stays ignored; never commit it.

## Agent files

`AGENTS.md` is the single source of truth for agent instructions. `CLAUDE.md` is a one-line import of it (`@AGENTS.md`), so harnesses that read only `CLAUDE.md` see the same content. It is not a symlink, because symlinks break on some checkouts.

`AGENTS.md` is generated for every project, kept under about 120 lines, and accurate: every command it lists exists ([check 14](verification.md#checks)), and every constraint is a rule the scaffold sets up or a fact of the generated project. Drop rows and lines for surfaces and features the project does not have. It contains, in order:

1. The project name and one sentence on what it is.
2. **Stack:** one row per surface with its path and technology; the package manager and Node version files; **Prereleases:** each exact prerelease with its reason, or "none".
3. **Commands:** prerequisites (the secret scanner the pre-commit hook needs), install (which also installs the hooks), `dev`, `verify` (same as CI), `format`, and the [lifecycle scripts](lifecycle.md#lifecycle).
4. **Constraints:** verify first; done means `pnpm verify` passed; strict TypeScript with no escape hatches or unexplained suppressions; no narrative comments (with the [upcoming rule](#no-comments-rule-upcoming) status); `@vllnt/logger` instead of `console`, never logging headers, cookies, tokens or identity; fail closed, with the failure path tested; backend rules, with components mounted only in `convex.config.ts`; `.env.example` holds names only and backend secrets live on the deployment; every user-visible string in every catalog; the 7-day release-age gate with `@vllnt/*` exempt and a reason for every exception; a changelog line for every user-visible change; branch, PR, merge, never pushing to the default branch or rewriting shared history; localhost dev servers unless an opt-in is recorded.
5. **Lifecycle:** the steps from [Lifecycle](lifecycle.md#lifecycle), one line each, with the run location.
6. **Parallel work:** one agent per worktree; never edit the main checkout; create and remove worktrees only with `wt:new` and `wt:rm`; rebase on the default branch before opening a PR; remove the worktree after merge; heavy work stays under the shared machine-wide cap.
7. **Convex rules:** the bullets of [Convex rules](backend-convex.md#convex-rules), verbatim.
8. **Layout:** the project tree from [single app](layouts.md#single-app) or [monorepo](layouts.md#monorepo).

When a framework writes its own managed block into `AGENTS.md`, commit it once and never hand-edit it. Examples: Convex `ai-files`, or an agent-rules block that the Next.js dev server adds. In a monorepo, `ai-files` writes into `packages/backend/`; the root `AGENTS.md` and `CLAUDE.md` stay human-owned.

### Root documents

- `README.md`: the project name, its one-sentence purpose, and the commands from `AGENTS.md`.
- Public projects also get:
  - `LICENSE`: the SPDX license text for the chosen id, with the current year and the copyright holder. Ask for the holder; default to the owner.
  - `SECURITY.md`: points to the host's private vulnerability reporting. Tell the user to enable it in the repository settings.
  - `CONTRIBUTING.md`: a short pointer to the `AGENTS.md` commands and lifecycle.

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
| `check:expo` | mobile app | Expo's dependency alignment check |
| `codegen` | wherever `convex/` lives | one-shot Convex code generation |
| `prepare` | single-app root or monorepo root | points git at `.githooks/` |

A backend-only single app has the same set without `build`. Its `verify` is `format:check`, lint, typecheck and test. The root also defines the [lifecycle scripts](lifecycle.md#lifecycle). In a monorepo, every task runs through Turbo as the [task graph target](vstack/capabilities/workspace-turborepo/references/task-graph-target.md) requires.

The library and CLI recipes are in [library-cli.md](library-cli.md).

## Why these defaults

Each default below gives the reason for a rule in this file or in a surface reference.

- Workspace globs hold only `apps/*` and `packages/*`. Tool scripts live in `scripts/` or `tools/` at the root, so a script folder is never mistaken for a package.
- One package scope for every workspace package: mixed scoped and unscoped names make imports and turbo filters inconsistent.
- Every file under `convex/` deploys as a module, so domain code lives in `convex/<domain>/`, and test-only helpers stay in `*.test.ts` files or outside `convex/`.
- Never give a file and a folder the same stem (`users.ts` next to `users/`): the module path becomes ambiguous.
- Declare each dependency in the package that imports it, and keep shared versions in `catalog:`. pnpm's isolated layout does not share a sibling's dependencies.
- `.env.example` per app, names only: without it, misconfiguration shows up only at runtime.
- Read public variables by their full literal name (`process.env.NEXT_PUBLIC_CONVEX_URL`): Next.js and Expo inline only direct references, so a dynamic lookup returns `undefined`. A small typed `environment.ts` per app reads those literals and throws a clear error on the first missing value; no env library is needed.
- Secret split: backend secrets live on the backend deployment, the deploy key lives only in the hosting dashboard per environment, and the backend URL comes from `NEXT_PUBLIC_CONVEX_URL` or `EXPO_PUBLIC_CONVEX_URL`, never hard-coded.
- No staging tier by default: the tiers are `dev`, `preview` and `production`, carried in `CONVEX_ENV`.
- Nothing environment-specific in committed config: hostnames, project ids and analytics keys stay out of files such as `eas.json` and `.env.example` comments.
- Every surface ships with passing tests of its generated behavior, including one failure path, so `pnpm test` is green on day one.
