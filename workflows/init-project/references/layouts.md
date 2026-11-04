Load when laying out the tree, shared packages, or monorepo root files.

The layout follows what `@vllnt/eslint-config` enforces. The installed preset is the authority: read its README and the effective config ([check 5](verification.md#checks)) rather than this file when they differ, and report the difference. Rules the preset does not enforce yet are listed as review rules with a pass check; never add a custom lint rule for them, because they belong upstream.

## Naming

- Files and folders outside `convex/` are kebab-case. The preset checks the folders of non-`.tsx` files, so a dynamic route segment that holds a `.ts` file (such as a route handler) is kebab-case (`[post-id]`, not `[postId]`). `.tsx` files may use any case, and a folder that holds only `.tsx` files is not checked, so keep it kebab-case by review ([check 21](verification.md#checks)).
- Under `convex/`, files and folders are snake_case: lowercase letters, digits, and underscores, with no hyphens and no extra dots. `_generated/` is exempt, and so are `convex.config.ts`, `auth.ts`, and `auth.config.ts`. `*.test.ts` files skip the Convex rules, so the dotted [backend test names](backend-convex.md#tests) pass; their part before the first dot is still snake_case.
- Names are not abbreviated (`environment.ts`, not `env.ts`); the preset lists the allowed short forms.
- Test files are `*.test.ts` (unit and backend) and `*.spec.ts` (end-to-end). Only the presets that wire the test relaxations (Next.js and Node.js) relax them; `react` and `base` do not, and no preset relaxes `.test.tsx`. Write tests as `.ts` and confirm the effective config of one test file per workspace ([check 5](verification.md#checks)). Helpers, fixtures, page objects, and setup files get production rules, so keep test helpers inside test files until a second consumer exists. A missing relaxation is fixed upstream, not by a local override.
- Every linted file belongs to a tsconfig; config files and JavaScript outside every tsconfig are ignored by the workspace's ESLint config.

## Single app

```
<name>/
  app/                     Next.js routes (web) or Expo Router screens (mobile)
  components/
  lib/                     the one home for app logic (no second src/ folder)
  convex/                  backend, when selected (see backend Files)
  tests/unit/              *.test.ts
  tests/e2e/               *.spec.ts, web only
  messages/                i18n catalogs, when selected
  public/                  web only
  scripts/                 lifecycle and worktree scripts
  .githooks/  .github/
  package.json  pnpm-workspace.yaml  tsconfig.json  eslint.config.mjs
  AGENTS.md  CLAUDE.md  CHANGELOG.md  README.md  SECURITY.md  CONTRIBUTING.md  [LICENSE]
```

Plus the root dotfiles from the [baseline](baseline.md): Node version, ignore files, Prettier config, and `.env.example`. `LICENSE` exists when the project is public. A single app still gets a `pnpm-workspace.yaml`, holding only the [supply-chain](baseline.md#supply-chain) settings and no `packages:` key.

## Monorepo

```
<name>/
  apps/web/                @<name>/web
  apps/mobile/             @<name>/mobile
  apps/cli/                @<name>/cli       (library-cli.md)
  packages/backend/        @<name>/backend   Convex lives in packages/backend/convex/
  packages/client/         @<name>/client    optional
  packages/shared/         @<name>/shared    optional
  packages/<lib>/          @<name>/<lib>     published library (library-cli.md)
  scripts/  .githooks/  .github/       scripts/ holds verify-changed for the pre-push gate
  package.json  pnpm-workspace.yaml  turbo.json
  AGENTS.md  CLAUDE.md  CHANGELOG.md  README.md  SECURITY.md  CONTRIBUTING.md  [LICENSE]
```

Create only the packages the user selected; each follows its surface file ([web](web-nextjs.md#files), [mobile](mobile-expo.md#files), [backend](backend-convex.md#files), [library and CLI](library-cli.md)). Convex's AI files land in `packages/backend/`; the root agent files stay human-owned. A project with only `backend` and `mobile` still uses this layout when the user picks monorepo.

Rules:

- One package scope, `@<name>/`, for every workspace. Internal dependencies use the workspace protocol, and shared versions live in the pnpm `catalog:`, which pnpm resolves under the release-age policy.
- Workspace globs hold only `apps/*` and `packages/*`; root tool scripts live in `scripts/`.
- Dependencies point one way: `apps/* -> packages/client -> packages/backend`, and `packages/shared` is a leaf that imports nothing internal. Web-only packages (`@vllnt/ui`, `@vllnt/analytics`) never reach a package that mobile consumes.
- A package imports another only through its published `exports`, never a deep path into its `src/` or `convex/`.
- Turbo runs every task; the [task graph target](vstack/capabilities/workspace-turborepo/references/task-graph-target.md) owns the graph, caching, and CI selection, and `turbo.json` declares every environment variable a task reads (the preset's turbo rules fail on an undeclared one).
- No root ESLint config and no root tsconfig: each workspace owns its own, so the root runs Turbo only.

Pass checks: the task graph has no cycles and no package depends on an app ([check 18](verification.md#checks)); every internal dependency edge follows the allowed directions above, a search finds no deep import into another workspace's `src/` or `convex/`, and no web-only package is in mobile's dependency closure ([check 21](verification.md#checks)). The preset's `boundaries` option stays off until it ships element definitions upstream.

### Monorepo root

- Root `package.json`: private, `packageManager` with the resolved pnpm, `engines.node` from the [runtime preflight](baseline.md#runtime-preflight), and the [baseline scripts](baseline.md#baseline-scripts) through Turbo, including `verify:changed`. Concurrency caps live in the root scripts. With mobile, `verify` and CI include `check:expo`. Root dev dependencies are only the shared tooling, through `catalog:`.
- `pnpm-workspace.yaml`: the workspace globs, a `catalog:` entry for every shared dependency resolved at install time (with mobile, `react` matches the version Expo selects, so one copy exists), and the [supply-chain](baseline.md#supply-chain) keys, written before the first `pnpm add`.
- `turbo.json` follows the [task graph target](vstack/capabilities/workspace-turborepo/references/task-graph-target.md): stream output instead of the interactive UI, global inputs for env files, every environment variable a task reads declared, `dev` persistent and uncached, and lint, typecheck, and test of source-first packages not waiting on upstream builds.

## Shared packages

Shared packages are **source-first**: `exports` point at TypeScript source, they do not emit, and consumers compile them (Next.js through its transpile list; Metro on its own). Each has `src/index.ts`, colocated `src/*.test.ts`, a tsconfig that includes `src`, and the [baseline scripts](baseline.md#baseline-scripts).

- `packages/shared`: pure TypeScript types and utilities, on the base preset with bundler resolution and the Node.js ESLint preset. It starts with one pure function and its test.
- `packages/client`: the typed data layer over the backend, shared by web and mobile, on the React presets, with `react` as a peer. It exports a client factory that rejects a blank backend URL (tested without constructing a client) and re-exports the backend's generated API, so apps have one import point. Domain hooks and services go here as the product grows.
- `packages/backend`: exports the generated API and data model to the other workspaces through `exports`; confirm the generated file names after the first codegen. Its `dev`, `codegen`, `lint`, `typecheck`, and `test` scripts run in the package.

An emitting package (a published library or a CLI) has two tsconfigs, one with tests for lint and typecheck and one without tests for the build (see [library-cli.md](library-cli.md#library)).
