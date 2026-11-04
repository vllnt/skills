Load when laying out the tree, shared packages, or monorepo root files.

## Single app

```
<name>/
  app/                     Next.js routes (web) or Expo Router screens (mobile)
  components/
  lib/                     app logic (no second src/)
  convex/                  when backend selected
  tests/unit/  [tests/e2e/]
  messages/                when i18n selected
  public/                  web only
  .githooks/  .github/workflows/  scripts/verify-changed.sh
  package.json  pnpm-workspace.yaml  tsconfig.json  eslint.config.mjs
  AGENTS.md  CLAUDE.md  CHANGELOG.md  README.md  [LICENSE SECURITY.md CONTRIBUTING.md]
```

Bracketed entries are optional. `tests/e2e/` only with the web recipe's Playwright setup. `convex/` follows [backend files](backend-convex.md#files).

Single-app `pnpm-workspace.yaml` holds [supply-chain](baseline.md#supply-chain) settings only — no `packages:` key.

## Monorepo

```
<name>/
  apps/web/                @<name>/web
  apps/mobile/             @<name>/mobile
  apps/cli/                @<name>/cli
  packages/backend/        @<name>/backend   Convex under packages/backend/convex/
  packages/client/         @<name>/client    optional
  packages/shared/         @<name>/shared    optional
  packages/<lib>/          @<name>/<lib>     published library
  .githooks/ .github/  scripts/verify-changed.sh
  package.json  pnpm-workspace.yaml  turbo.json
  AGENTS.md  CLAUDE.md  CHANGELOG.md  README.md
```

Create only selected packages. Surface recipes: [web](web-nextjs.md#files), [mobile](mobile-expo.md#files), [backend](backend-convex.md#files), [library-cli](library-cli.md), [shared packages](#shared-packages).

Rules:

- One scope `@<name>/`; internal deps use `workspace:*`.
- Shared versions live in the pnpm catalog ([pnpm-workspace.yaml](#pnpm-workspaceyaml)).
- Deps one way: `apps/* → packages/client → packages/backend`; `packages/shared` is a leaf. No cycles.
- Backend + mobile only still uses this layout when monorepo is selected.
- Monorepo requires Turborepo ([turbo.json](#turbojson)).

## Shared packages

Source-first: `exports` point at TypeScript source (no consumer build step). Web apps list them in `transpilePackages`. Never put `@vllnt/ui` or `@vllnt/analytics` on a package mobile consumes.

### packages/shared

- Manifest: private ESM package; `exports` → `./src/index.ts`; scripts `lint`, `typecheck`, `test`.
- Dev deps via `catalog:`: eslint, prettier, typescript, `@vllnt/eslint-config`, `@vllnt/typescript`, vitest.
- `tsconfig` extends `@vllnt/typescript/base.json` with noEmit and `src` include; read current preset keys from the installed package.
- ESLint: nodejs + turbo presets from `@vllnt/eslint-config`.
- Vitest: unit tests under `src/**/*.test.ts`.
- Seed: one pure export + tests (e.g. blank-string helper). Do not invent APIs beyond the seed.

### packages/client

Typed data layer over the backend for web and mobile.

- Manifest: depends on `@<name>/backend` (`workspace:*`) and `convex` (`catalog:`); peer `react` (`catalog:`); `exports` → source; scripts as shared.
- `tsconfig` extends `@vllnt/typescript/react.json`; ESLint react + turbo.
- Seed: `createConvexClient(url)` that rejects blank URL; re-export generated `api` from backend. Apps supply URL helpers.

### packages/backend

- Manifest exports generated API / data-model paths that match post-codegen file names (verify after first codegen).
- Scripts: `dev`, `codegen`, `lint`, `typecheck`, `test` using Convex CLI flags from current Convex docs.
- Files: `convex/` per [backend](backend-convex.md#files); ESLint + vitest forms from that recipe plus turbo.
- `.env.local` from codegen is gitignored.

## Monorepo root

### Root package.json

Requirements (resolve exact tool versions at install):

- `private`, `packageManager` (resolved pnpm), `engines.node` matching [runtime preflight](baseline.md#runtime-preflight).
- Scripts: `prepare` (hooks path), `dev`/`build`/`lint`/`typecheck`/`test` via turbo, `format` / `format:check`, `verify:changed`, `verify` (format check → lint/typecheck/test → build). Cap check concurrency at 2 and build at 1 ([lean defaults](baseline.md#lean-defaults)).
- When mobile exists, include `check:expo` in `verify` and CI.
- Root `devDependencies` via `catalog:`: `@vllnt/eslint-config`, `@vllnt/typescript`, eslint, prettier, turbo, typescript.
- No root ESLint or tsconfig; each workspace owns its own. Every workspace ESLint appends turbo so env vars are declared in `turbo.json`.

### pnpm-workspace.yaml

- `packages:` globs for `apps/*` and `packages/*`.
- `catalog:` entries for every shared dependency — **ranges and versions resolved at execution** from registry + peers + age policy; never copy stale majors from this skill.
- Append [supply-chain](baseline.md#supply-chain) top-level keys. Write the full file before the first `pnpm add`.
- Mobile present: catalog `react` must match the exact version Expo selected (one copy across workspaces).
- Workspaces reference catalog packages as `"catalog:"`.

### turbo.json

Requirements (shape from current Turborepo schema + [task graph target](vstack/capabilities/workspace-turborepo/references/task-graph-target.md) when present):

- Declare schema URL from current Turborepo docs; `ui` = `stream` (not interactive TUI).
- `globalDependencies` / `globalEnv` cover local env files and shared env names the linted code reads.
- Tasks at minimum: `transit` (`dependsOn: ["^transit"]`), `build` (depends on `^build`, hashed public env, build outputs), `dev` (no cache, persistent), `lint` / `typecheck` / `test` (depend on `transit`), `clean` (no cache).
- Do not make lint/typecheck/test depend on `^build` for source-first packages.
- Every env var a linted file reads must appear in `globalEnv` or the task `env`, or turbo/env lint fails.
- Mobile: add `check:expo` with cache false.
- Cap concurrency in root scripts, not a root `concurrency` field.
