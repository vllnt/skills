Load this file when scaffolding or changing what every project shares: dependency versions, TypeScript, ESLint, Prettier, git hooks, supply chain, CI, changelog, ignore files, agent files, and baseline scripts.

## Package lines

Every version below is a default range, not a fact. These tables are the one version authority for the recipes; each `pnpm add` command in a recipe must match them. The default-packages annex owns the channel and pin rules for `@vllnt/*` packages; these lines must agree with it.

### Resolve versions

1. Write `pnpm-workspace.yaml` before the first `pnpm add`: the block from [Supply chain](#supply-chain) in a single app, or the full file from [pnpm-workspace.yaml](layouts.md#pnpm-workspaceyaml) (`packages:`, `catalog:` and that block) in a monorepo.
2. Add packages by range (`pnpm add next@^16`). pnpm then picks the newest version that is at least 7 days old.
3. Do not pre-pin exact versions taken from `npm view`. The newest release may be too young, and strict mode then fails the install. The one exception is an annex-pinned `@vllnt/*` canary, which the policy exempts (see [Canary packages](#canary-packages)).
4. If a range resolves to nothing, stop and ask.
5. After installing, report the versions actually installed, read from `pnpm list --depth 0` or the lockfile.

### Check exports

Before generating `import x from "@vllnt/<pkg>/<sub>"`, run `npm view @vllnt/<pkg>@<pinned> exports --json` and confirm `./<sub>` exists. The map proves only that the subpath exists: before generating a call, confirm each named export in the installed package's `.d.ts`. Published versions often lag the source repos. Some subpaths shown in READMEs exist only on canary builds.

### Canary packages

Use stable `latest` lines. A canary (`x.y.z-canary.<sha>`) is allowed only:
- when the package has no stable release and the user picked the feature, or
- when the tables below, a surface reference, or the default-packages annex says so.

To pin one:
1. The default-packages annex is the single authority. For a package it lists, pin the annex version exactly, without a caret.
2. Run `npm view <pkg> dist-tags --json` only to detect a newer `canary` tag. If it differs from the annex pin, report both in the plan and keep the annex pin. Move the pin only with the user's approval.
3. For a package the annex does not list, pin its `canary` tag exactly. If it has no `canary` tag, stop and ask.
4. Do not pin from `latest`: it can point at an older canary (for `@vllnt/next-llms`, one without input hardening). A package with no `canary` tag (for example `@vllnt/ui-native`) still follows step 1.
5. Check exports (see above) against that exact version.
6. Report the pin in the plan, and record it under "Pinned prereleases" in the generated `AGENTS.md` (see [Agent files](#agent-files)).

### Tooling (every project)

| Package | Default line | Run-time check / note |
|---|---|---|
| Node | latest 24.x patch in `.node-version`; `"engines": { "node": ">=24 <25" }` | Some selected packages declare higher minimums (one backend feature needs `>=22.12`). 24.x satisfies all of them |
| pnpm | latest 11.x (the `latest-11` dist-tag of `pnpm`), exact, in `"packageManager": "pnpm@11.x.y"` | Supply-chain settings go in `pnpm-workspace.yaml` (pnpm 11 reads them there). Moving to a newer major is a deliberate change, made only after confirming it still honors every key in [Supply chain](#supply-chain) |
| `typescript` | `~6.0.3` | `~6.0.3` stays inside the preset peer range `>=6.0.2 <6.1`. Never install bare `typescript@latest`: it is outside that range and breaks typed linting |
| `eslint` | `^9.39.5` | Not 10.x: plugins bundled by the preset peer `eslint ^9`. `9.39.5` is the final 9.x, so install prints a deprecation warning for it. That is expected, not a failure |
| `prettier` | `^3` | Declare it explicitly. The preset peers it and runs it as a lint rule |
| `@vllnt/eslint-config` | `^2.0.0` | Flat config only. Exports in [ESLint](#exports) |
| `@vllnt/typescript` | `^2.0.0` | Presets in [TypeScript](#typescript) |
| `turbo` | `^2` | Monorepo only |
| `vitest` | latest stable major | Web unit tests and backend tests |

### Runtime (per surface)

| Package | Default line | Run-time check / note |
|---|---|---|
| `next`, `react`, `react-dom` | `next` latest 16.x; `react` and `react-dom` latest 19.x | `@types/react` and `@types/react-dom` 19.x; `@types/node` matching the Node major |
| `@vllnt/ui` | `^0.3.0` | Needs **Tailwind 3.4**, not 4. Its stylesheet uses `@tailwind` directives and its preset is a v3 JS config. 0.3.0's peer metadata `>=3.0.0` is loose: it lets Tailwind 4 install, but the CSS would not work. So always install Tailwind `^3.4.19`. Fail closed only if `peerDependencies.tailwindcss` excludes 3.4. Treat Tailwind 4 support as real only when the package README or CHANGELOG says so; until then, the rule in [UI library](web-nextjs.md#ui-library) stands |
| `@vllnt/logger` | `^0.1.2` | ESM only. Default level is `warn` |
| `@vllnt/analytics` | `^0.1.1` | 0.1.x ships TypeScript source: add `transpilePackages`. Do not caret-jump to 0.2 |
| `@vllnt/next-llms` | No stable release. Pin the annex version exactly | The `latest` tag points at an older canary without input hardening. Do not use it. See [Canary packages](#canary-packages) |
| `@vllnt/ui-native` | Experimental, opt-in. Pin the annex version exactly | Expo only, after the availability gate in [Native UI](mobile-expo.md#native-ui). It installs `@vllnt/ui-core`. See [Canary packages](#canary-packages) |
| `convex` | latest 1.x | `@vllnt/convex-*` peer `convex ^1.45.0` |
| `@vllnt/convex-helpers` | latest stable | Its `./better-auth` and `./identity` subpaths may exist only on canary. [Check exports](#check-exports) |
| `@vllnt/convex-<feature>` | latest stable; PREVIEW ones: pin the annex version exactly | See [Feature bundles](backend-convex.md#feature-bundles) |
| `expo` | latest stable SDK | Other Expo packages are aligned with `expo install` (see [mobile commands](mobile-expo.md#commands)) |

### Not offered

- `@vllnt/convex-mcp` is archived and deprecated. Use `@vllnt/convex-helpers/mcp` instead.
- `@vllnt/ui-core` is pulled in by `@vllnt/ui-native`. Never install it directly unless app code imports it.

## TypeScript

Every `tsconfig.json` you write has an `extends` that includes a `@vllnt/typescript/*.json` preset. Exports are exact file names; there is no bare `"@vllnt/typescript"` export.

| Workspace kind | `extends` |
|---|---|
| Next.js app | `@vllnt/typescript/nextjs.json` |
| Convex (`convex/tsconfig.json`) | `@vllnt/typescript/base.json` + Convex options (see [backend files](backend-convex.md#files)) |
| Expo app | `["expo/tsconfig.base", "@vllnt/typescript/base.json"]` |
| React shared package | `@vllnt/typescript/react.json` + `noEmit` |
| Pure TS shared package (source-first) | `@vllnt/typescript/base.json` + Bundler options (see [shared packages](layouts.md#shared-packages)) |
| Node service or CLI | `@vllnt/typescript/nodejs.json` + `rootDir`, `outDir` |
| Published library | `@vllnt/typescript/node-library.json` + `rootDir`, `outDir` (relative imports need `.js` extensions) |

Every preset turns on:
- `strict`
- `noUncheckedIndexedAccess`
- `noUncheckedSideEffectImports`: add `declare module "*.css";` where CSS is imported.
- `isolatedModules`
- `types: []`: each consumer lists its own ambient types.

## ESLint

Write templates that pass the presets. Generated code must pass `eslint --max-warnings 0` and `tsc --noEmit`. The presets are strict; [Traps](#traps) lists what to avoid. After writing files and installing, run `prettier --write .` and `eslint --fix .` once per workspace to settle import order, key order and formatting. Rerun `prettier --write .` after the last installer or generator, since either can rewrite files such as `package.json`. Then the [verification checks](verification.md#checks) must pass with no further fixes. If `--fix` cannot settle an error, fix the template; never disable the rule. The one exception is a narrowly scoped, version-bound compatibility override that a recipe prescribes, with its removal condition.

Generated source contains no narrative comments. The only exceptions are machine markers such as `"use client"`. Details are in [No-comments rule (upcoming)](#no-comments-rule-upcoming).

### Exports

The `@vllnt/eslint-config` `exports` map:

```json
{ ".": "./flat/index.js", "./nextjs": "./flat/nextjs.js", "./nodejs": "./flat/nodejs.js",
  "./convex": "./flat/convex.js", "./react": "./flat/react.js", "./turbo": "./flat/turbo.js",
  "./boundaries": "./flat/boundaries.js", "./package.json": "./package.json" }
```

- The barrel `.` has named exports only: `base`, `nextjs`, `nodejs`, `react`, `convex`, `turbo`, `boundaries`. It has **no default**.
- Each subpath exports its named array **and** a default of the same array.
- **There is no `config` export anywhere.**
- Use subpath named imports, such as `import { nextjs } from "@vllnt/eslint-config/nextjs"`. The barrel loads all seven presets.
- Every preset is an array: spread it, as in `export default [{ ignores }, ...nextjs]`.

| Workspace | Presets |
|---|---|
| Next.js app | `nextjs` (+ `convex` and the snake_case override when it holds `convex/`) (+ `turbo` in a monorepo) |
| Backend package | `base` + `convex` + snake_case override (+ `turbo`) |
| Expo app | `react` |
| React shared package | `react` |
| Pure TS package / Node | `nodejs` |
| Large monorepo boundaries | `boundaries`: opt-in only, needs element definitions |

Config file: `eslint.config.mjs`. It works in both ESM and CommonJS packages.

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
- At scaffold time, read the pinned `@vllnt/eslint-config` CHANGELOG and README.
  - Enable a no-comments rule only if the pinned preset documents one, exactly as documented.
  - Otherwise add nothing and report the rule as upcoming. Never copy a custom rule into the project: a copy becomes per-project maintenance.
- The preset's only comment rule in the pinned version, `write-good-comments`, checks prose quality. It is not a no-comments rule.
- Templates already contain zero comments, so turning the rule on later is free.
- The generated `AGENTS.md` states the policy.

Expected contract of the upstream rule (unpublished, unverified), so templates stay compatible:
- It reports `Line` and `Block` comments, except the machine markers above and TSDoc blocks attached to exported declarations.
- It applies to `.ts`, `.tsx`, `.js` and `.mjs` files, scripts and config files included.

## Prettier

`.prettierrc.json`:

```json
{ "proseWrap": "always", "trailingComma": "all" }
```

The rest are Prettier defaults: double quotes, semicolons, 80 columns.

`.prettierignore` lists:

```text
pnpm-lock.yaml
**/convex/_generated/
**/.next/
**/dist/
**/coverage/
**/.expo/
**/.convex/
**/AGENTS.md
**/CLAUDE.md
**/.agents/
**/.claude/skills/
**/skills-lock.json
CHANGELOG.md
```

The two agent files contain a managed block (see [backend commands](backend-convex.md#commands)). Convex `ai-files` also writes `.agents/`, `.claude/skills/` and `skills-lock.json`, so they are ignored too. If `prettier --check` flags another tool-written file, add it here.

`format:check` runs in `verify` and CI. ESLint already fails on formatting inside linted files; `format:check` covers JSON, Markdown and YAML.

## Git hooks

No hook manager. `"prepare": "git config core.hooksPath .githooks || true"` installs the hooks on `pnpm install` and tolerates checkouts without git.

`.githooks/pre-commit` stays sub-second. It holds only the checks that are hard to undo after a commit:

```sh
#!/bin/sh
set -eu
[ "${SKIP_VERIFY:-0}" = "1" ] && exit 0
if git diff --cached --name-only | grep -E '(^|/)\.env' | grep -vE '\.env\.example$'; then
  echo "pre-commit: refusing to commit env files" >&2
  exit 1
fi
git diff --cached --check
```

`.githooks/pre-push` runs the heavy checks:

```sh
#!/bin/sh
set -eu
[ "${SKIP_VERIFY:-0}" = "1" ] && exit 0
pnpm verify
```

Make both hook files executable (`chmod +x`). Pushes stay slow on purpose and commits stay fast, so nobody reaches for `--no-verify`.

## Supply chain

Enforce a 7-day minimum package age, with `@vllnt/*` exempt. Put this in `pnpm-workspace.yaml` (single app and monorepo alike):

```yaml
minimumReleaseAge: 10080
minimumReleaseAgeExclude:
  - "@vllnt/*"
trustPolicy: no-downgrade
blockExoticSubdeps: true
strictDepBuilds: true
allowBuilds:
  esbuild: false
```

What each setting does:
- `minimumReleaseAge: 10080` is 7 days, in minutes. First-party `@vllnt/*` releases are exempt: they come from provenance-signed CI, and canaries are always younger than 7 days.
- `trustPolicy: no-downgrade` refuses a version whose publish trust is weaker than earlier versions.
- `blockExoticSubdeps` blocks git and tarball dependencies deep in the tree.
- `strictDepBuilds` makes install fail when an install script has not been reviewed.

Rules for keeping it:
- When install fails on an unlisted build script, add that package to `allowBuilds`. Use `false` unless the package does not work without its script. Each entry gets a reason in `AGENTS.md`.
- Every later exception gets a reason in `AGENTS.md`: an extra exclude, an override or a patch. A patch also needs its removal condition.
- When install fails with `ERR_PNPM_NO_MATURE_MATCHING_VERSION` right after a "Skipped trust downgrades" warning, add `trustPolicyExclude: ["<pkg>@<older version>"]`, where `<older version>` is the newest mature version of `<pkg>` that the trust policy skipped. Record the reason and the removal condition in `AGENTS.md`. Never loosen `trustPolicy` or `minimumReleaseAge`.
- Do not exempt `convex` or `@convex-dev/*`. pnpm then installs the newest version that is at least 7 days old.
- Never write exact-version entries in `minimumReleaseAgeExclude`; they go stale on every bump.

No `.npmrc` is needed.

## CI

Affected-only; checks at concurrency 2, then the build at concurrency 1. CI is GitHub Actions and Dependabot is GitHub-only. If the existing remote is not on GitHub, skip `.github/` and report the skip. Write `.github/workflows/ci.yml`, with `<default-branch>` replaced by the repository's default branch (detected, or `main` for a new repository):

```yaml
name: CI
on:
  pull_request:
    branches: [<default-branch>]
  push:
    branches: [<default-branch>]
permissions:
  contents: read
concurrency:
  group: ci-${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
jobs:
  ci:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    env:
      NEXT_PUBLIC_CONVEX_URL: http://127.0.0.1:3210
      EXPO_PUBLIC_CONVEX_URL: http://127.0.0.1:3210
    steps:
      - uses: actions/checkout@<sha> # vX.Y.Z
        with:
          fetch-depth: 0
          persist-credentials: false
      - uses: pnpm/action-setup@<sha> # vX.Y.Z
      - uses: actions/setup-node@<sha> # vX.Y.Z
        with:
          node-version-file: .node-version
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm format:check
      - name: Select affected packages
        id: scope
        env:
          EVENT: ${{ github.event_name }}
          BASE: origin/${{ github.base_ref }}
        run: |
          if [ "$EVENT" != "pull_request" ] ||
             git diff --name-only "$BASE"...HEAD |
             grep -Eq '^(package\.json|pnpm-lock\.yaml|pnpm-workspace\.yaml|turbo\.json|\.node-version|\.prettierrc\.json|\.github/)'; then
            echo "filter=" >> "$GITHUB_OUTPUT"
          else
            echo "filter=--filter=...[$BASE]" >> "$GITHUB_OUTPUT"
          fi
      - env:
          FILTER: ${{ steps.scope.outputs.filter }}
        run: |
          pnpm turbo run lint typecheck test --concurrency=2 $FILTER
          pnpm turbo run build --concurrency=1 $FILTER
```

How the job selects work:
- **Affected-only:**
  - On a PR, turbo runs only the packages changed since the base, plus their dependents (`...[base]`).
  - Any change to a shared root file runs everything.
  - Pushes to the default branch run everything.
  - When selection is unclear, run more, not less.
- **Single-app form** (also for a single library or CLI): same file, but the affected-selection step and both turbo steps are replaced by one step, `run: pnpm lint && pnpm typecheck && pnpm test && pnpm build` (no `build` for a backend-only app). The commands already run one at a time, and there is one package, so every PR runs it.
- **Mobile:** when `apps/mobile` or a mobile single app exists, CI also runs `check:expo`. In a monorepo, add it to the first turbo command (`lint typecheck test check:expo`); in a single app, add `&& pnpm check:expo`.
- **Capacity:** the checks run at `--concurrency=2` and the build runs after them at `--concurrency=1`, as locally. See [Lean defaults](#lean-defaults) and [Root package.json](layouts.md#root-packagejson).
- **Superseded runs:** a newer push to the same PR cancels the older run. Runs on the default branch are never cancelled.
- **No workflow-level `paths:` filters:** they leave required checks pending.

The `env` block sets non-secret local placeholders, so builds that construct the backend client succeed without a backend (see [backend commands](backend-convex.md#commands)). Omit it when there is no backend.

### End-to-end job

Optional. Generate an `e2e` job only when the project has a web app and the [optional Playwright setup](web-nextjs.md#end-to-end-optional) of the web recipe is generated with it (dependency, config, spec and the `test:e2e` script all together).
- It repeats the setup steps (checkout, pnpm, node, frozen install), because jobs do not share `.next`.
- It copies the `ci` job's `env` block, so the build sees the same backend URL placeholder.
- It builds the web app itself: `pnpm --filter <web> build` in a monorepo, `pnpm build` in a single app.
- It installs only chromium (`pnpm --filter <web> exec playwright install --with-deps chromium`, or `pnpm exec playwright install --with-deps chromium` in a single app) and runs `test:e2e` the same way.
- `playwright.config.ts` sets `webServer.command: "pnpm start"`, `workers: process.env.CI ? 1 : 2`, and a single desktop chromium project.
- `tests/e2e/home.spec.ts` asserts that the home page renders the project name.
- The web app adds `@playwright/test` as a dev dependency. `playwright.config.ts` sets `testDir: "tests/e2e"`, and vitest's `include` never matches `tests/e2e`.

### Action pinning and Dependabot

- Pin every action to a full commit SHA, resolved at scaffold time for the latest release tag, with the tag kept as a trailing `# vX.Y.Z`.
- Resolve the SHA with `gh api repos/<owner>/<action>/commits/<tag> --jq .sha`, which returns the commit even for annotated tags.
- `.github/dependabot.yml` covers the `github-actions` and `npm` ecosystems, weekly.
  - `cooldown: { default-days: 7 }` matches the package age policy.
  - `@vllnt/*` is excluded from the cooldown, if the Dependabot version supports cooldown excludes.

### Not generated by default

- Publish workflows. Add one only for a package the user wants published: tag-driven `vX.Y.Z`, npm trusted publishing with provenance, no token, and publish concurrency set to never cancel.
- Project-specific policy workflows (the user adds them).

## Changelog

`CHANGELOG.md` uses Keep a Changelog 1.1.0 with SemVer, and starts with `## [Unreleased]` and an `### Added` line for the scaffold. It is hand-written: no changesets and no release bot.

`AGENTS.md` rule: a user-visible change adds a line under `[Unreleased]`. A release moves the lines into `## [X.Y.Z] - YYYY-MM-DD`.

## Lean defaults

- **Capacity:**
  - Parallelism is capped at 2: turbo, vitest (`maxWorkers: 2`), jest (`--maxWorkers=2`) and Playwright.
  - Builds run one at a time (`--concurrency=1`), after the checks. Run heavy steps one at a time.
  - 2 is a default, not a law: lower it when a measured run hits low free memory.
- ESLint's cache lives in `node_modules/.cache/` (`--cache-location`), out of git and out of lint scope. `tsc` build info lands in the package root as `*.tsbuildinfo`, which [Gitignore](#gitignore) covers.
- Dev servers bind to loopback (localhost) on a fixed port per app. Physical-device Expo development may opt into `--lan` or a tunnel explicitly; record the opt-in in `AGENTS.md`.
- One browser (chromium) for end-to-end tests. No Storybook, bundle analyzers or extra quality tools by default.
- No `pkg#task` turbo overrides, and no hand-listed test files: test runners find tests by glob.
- `verify` is the one command that matches CI, and the pre-push hook runs it.
- The Convex local backend runs only on demand (`convex dev`). Tests use convex-test, which needs no running backend.

## Gitignore

```text
node_modules/
.next/
out/
dist/
coverage/
.turbo/
.expo/
.convex/
playwright-report/
test-results/
*.tsbuildinfo
next-env.d.ts
.env
.env.*
!.env.example
.DS_Store
```

- `convex/_generated/` is committed, so it is not ignored.
- Codegen writes `.env.local` with backend credentials. `.env.*` ignores it; never commit it.
- `next-env.d.ts` is regenerated by `next dev` and `next build` and imports from `.next/`, so it is ignored.

## Agent files

`AGENTS.md` is the single source of truth for agent instructions. `CLAUDE.md` is a one-line import, so harnesses that read only `CLAUDE.md` see the same content:

```text
@AGENTS.md
```

It is not a symlink, because symlinks break on some checkouts. In a single app, Convex's `ai-files` command may append its managed block to both files. That is expected.

Fill the `AGENTS.md` template per project. Keep it under about 100 lines and keep project-specific policy out. Drop rows and bullets for surfaces the project does not have. Every constraint line must be a rule the scaffold sets up or a fact of the generated project, so drop a line for a feature that is absent (for example i18n or the backend). `<default-branch>` is the repository's default branch (detected, or `main` for a new repository). Fill `## Convex rules` with the bullets of [Convex rules](backend-convex.md#convex-rules), verbatim. Fill `## Layout` with the tree from [single app](layouts.md#single-app) or [monorepo](layouts.md#monorepo).

````markdown
# <name>

<one sentence: what this project is>.

## Stack

| Surface | Path | Tech |
|---|---|---|
| web | `<path>` | Next.js App Router, @vllnt/ui, next-intl |
| backend | `<path>/convex` | Convex, @vllnt/convex-* (<list>) |
| mobile | `<path>` | Expo Router |
| library | `<path>` | TypeScript library, @vllnt/typescript node-library preset |
| cli | `<path>` | Node CLI, @vllnt/logger |

Package manager: pnpm (`packageManager` pin). Node: `.node-version`.
Pinned prereleases: <package@version, reason> (or "none").

## Commands

```sh
pnpm install          # also installs git hooks
pnpm dev
pnpm verify           # format, lint, typecheck, test, build: same as CI
pnpm format
```

## Constraints

- **Verify first.** Read a file, symbol or check before making claims about it.
- **Done means verified.** Run `pnpm verify` before saying a change is done.
- **TypeScript.** No `any`, no non-null assertions, no `@ts-ignore`, no lint suppression without a reason.
- **Comments.** No narrative comments. Use names, small functions, or TSDoc on exported API.
- **Logging.** Use `@vllnt/logger` (`@vllnt/logger/convex` in the backend), never `console`. Never log headers, cookies, tokens or identity.
- **Fail closed.** A failed validation, auth or backend call must not advance state. Test the failure path.
- **Backend.** Follow the Convex rules below. Components mount only in `convex/convex.config.ts`.
- **Env.** `.env.example` holds names only. Backend secrets go on the deployment (`convex env set`).
- **i18n.** Every user-visible string lives in every catalog.
- **Dependencies.** 7-day minimum age, with `@vllnt/*` exempt. Every exception, override or patch has a reason here.
- **Changelog.** User-visible change -> a line under `[Unreleased]` in `CHANGELOG.md`.
- **Git.** Branch, PR, merge. Never push to `<default-branch>` directly or rewrite shared history.
- **Dev servers.** Localhost by default. Any LAN or tunnel use is an explicit opt-in recorded here.

## Convex rules

<the bullets of the Convex rules section, verbatim>

## Layout

<the project tree for this project's layout>
````

When a framework writes its own managed block into `AGENTS.md`, commit it once and never hand-edit it. Examples: Convex `ai-files`, or the agent-rules block that `next dev` adds. In a monorepo, `ai-files` writes into `packages/backend/`; the root `AGENTS.md` and `CLAUDE.md` stay human-owned.

### Root documents

- `README.md`: the project name, its one-sentence purpose, and the generated commands from the `AGENTS.md` Commands block.
- Public projects also get:
  - `LICENSE`: the SPDX license text for the chosen id, with the current year and the copyright holder. Ask for the holder; default to the owner.
  - `SECURITY.md`: points to the host's private vulnerability reporting. Tell the user to enable it in the repository settings.
  - `CONTRIBUTING.md`: a short pointer to the `AGENTS.md` commands.

## Baseline scripts

Every package or app defines the same script names, so agents, hooks and CI never guess:

| Script | Where | Command |
|---|---|---|
| `dev` | each app, backend | the framework's dev server, bound to localhost |
| `build` | web, mobile (`expo export`), library, CLI, root | the framework build; root `turbo run build --concurrency=1`; library and CLI `tsc -p tsconfig.build.json` |
| `lint` | every workspace | `eslint --cache --cache-location node_modules/.cache/eslint/ --max-warnings 0 .` |
| `typecheck` | every workspace | `tsc --noEmit` (+ `-p convex/tsconfig.json` where `convex/` lives inside an app) |
| `test` | every workspace | the surface's runner with 2 workers |
| `format`, `format:check` | single-app root or monorepo root | `prettier --write .` / `prettier --check .` |
| `verify` | single-app root or monorepo root | `format:check`, then lint, typecheck and test (and `check:expo` when mobile exists), then build |
| `check:expo` | mobile app | `expo install --check` |
| `codegen` | wherever `convex/` lives | `convex dev --once` |
| `prepare` | single-app root or monorepo root | `git config core.hooksPath .githooks \|\| true` |

A backend-only single app has the same set without `build`. Its `verify` is `format:check`, lint, typecheck and test.

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
