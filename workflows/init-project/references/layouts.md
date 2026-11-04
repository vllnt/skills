Load this file when you lay out the project tree, and again when you create shared packages or the root files of a monorepo.

## Single app

```
<name>/
  app/                     Next.js routes (web) or Expo Router screens (mobile)
  components/
  lib/                     the one home for app logic (no second src/ folder)
  convex/                  backend, when selected
  tests/unit/  [tests/e2e/]
  messages/                i18n catalogs, when selected
  public/                  web only
  .githooks/  .github/workflows/ci.yml  .github/dependabot.yml
  .node-version  .gitignore  .prettierrc.json  .prettierignore  .env.example
  package.json  pnpm-workspace.yaml  tsconfig.json  eslint.config.mjs
  AGENTS.md  CLAUDE.md  CHANGELOG.md  README.md  [LICENSE SECURITY.md CONTRIBUTING.md]
```

Bracketed entries are optional. `tests/e2e/` exists only with the optional Playwright setup of the web recipe. The `convex/` folder follows the [Convex backend files](backend-convex.md#files).

A single app still gets a `pnpm-workspace.yaml`, used only for pnpm settings from the [supply-chain block](baseline.md#supply-chain). It has no `packages:` key.

## Monorepo

```
<name>/
  apps/web/                @<name>/web
  apps/mobile/             @<name>/mobile
  apps/cli/                @<name>/cli       command-line app (library-cli.md)
  packages/backend/        @<name>/backend   Convex lives in packages/backend/convex/
    AGENTS.md  CLAUDE.md  .agents/  .claude/  skills-lock.json   written there by Convex ai-files
  packages/client/         @<name>/client    optional
  packages/shared/         @<name>/shared    optional
  packages/<lib>/          @<name>/<lib>     published library (library-cli.md)
  .githooks/ .github/  .node-version  .gitignore  .prettierrc.json  .prettierignore
  package.json  pnpm-workspace.yaml  turbo.json
  AGENTS.md  CLAUDE.md  CHANGELOG.md  README.md      human-owned; ai-files never writes them
```

Create only the packages the user selected. Each package follows its surface file:

- `apps/web`: [web recipe](web-nextjs.md#files).
- `apps/mobile`: [mobile recipe](mobile-expo.md#files).
- `packages/backend`: [Convex backend](backend-convex.md#files). Convex lives in `packages/backend/convex/`.
- `packages/client` and `packages/shared`: [shared packages](#shared-packages).
- `apps/cli` and `packages/<lib>`: both are optional rows. Create them only when the user picks a command-line app or a published library, and follow [library-cli.md](library-cli.md).

The monorepo follows four rules:

- Every workspace package uses the one scope `@<name>/`.
- Internal dependencies use `workspace:*`.
- Shared versions live in the pnpm `catalog:` (see [pnpm-workspace.yaml](#pnpm-workspaceyaml)).
- Dependencies point one way: `apps/* -> packages/client -> packages/backend`, and `packages/shared` is a leaf. No cycles; turbo rejects cyclic workspace dependencies.

A project with only `backend` and `mobile` (no `web`) still uses this layout when the user picks monorepo.

## Shared packages

Shared packages are **source-first**:

- `exports` point at TypeScript source, so consumers need no build step and the turbo config stays small.
- Next.js apps list each one in `transpilePackages`. Metro compiles workspace TypeScript on its own.
- `@vllnt/ui` and `@vllnt/analytics` are web-only: never make them dependencies of a package that mobile consumes.

### packages/shared

`packages/shared/package.json`:

```json
{
  "name": "@<name>/shared",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "sideEffects": false,
  "exports": { ".": "./src/index.ts" },
  "scripts": {
    "lint": "eslint --cache --cache-location node_modules/.cache/eslint/ --max-warnings 0 .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run"
  }
}
```

Dev dependencies: `eslint`, `prettier`, `typescript`, `@vllnt/eslint-config`, `@vllnt/typescript` and `vitest`, all `catalog:`.

Its config files:

- `tsconfig.json` extends `@vllnt/typescript/base.json` and adds `"module": "ESNext"`, `"moduleResolution": "Bundler"`, `"lib": ["ES2024"]`, `"noEmit": true`, `"types": []` and `"include": ["src"]`.
- `eslint.config.mjs` is `[{ ignores: ["coverage/**", "node_modules/**", "*.config.{js,mjs,cjs,ts}"] }, ...nodejs, ...turbo]`, with `nodejs` from `@vllnt/eslint-config/nodejs` and `turbo` from `@vllnt/eslint-config/turbo`.
- `vitest.config.ts` is `defineConfig({ test: { include: ["src/**/*.test.ts"], maxWorkers: 2 } })`.

Its source files:

- `src/index.ts` exports one pure function, `isBlank(value: string): boolean`, which returns `value.trim().length === 0`.
- `src/index.test.ts` asserts `isBlank("  ")` is `true` and `isBlank("a")` is `false`.

### packages/client

`packages/client` is the typed data layer over the backend, shared by web and mobile.

`package.json`:

```json
{
  "name": "@<name>/client",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "sideEffects": false,
  "exports": { ".": "./src/index.ts" },
  "dependencies": { "@<name>/backend": "workspace:*", "convex": "catalog:" },
  "peerDependencies": { "react": "catalog:" },
  "scripts": {
    "lint": "eslint --cache --cache-location node_modules/.cache/eslint/ --max-warnings 0 .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run"
  }
}
```

Dev dependencies: the shared set, plus `react` and `@types/react`.

Its config files:

- `tsconfig.json` extends `@vllnt/typescript/react.json` with `"noEmit": true`, `"types": ["react"]` and `"include": ["src"]`.
- ESLint uses `react` + `turbo`.
- Vitest is configured as for `shared`.

`src/index.ts` exports `createConvexClient(url: string): ConvexReactClient`. It throws `Error("Convex URL is required")` when `url` is blank, and otherwise returns `new ConvexReactClient(url)`. It also re-exports `api` from `@<name>/backend/api`, so the dependency is used and apps have one import point for the client and the typed API.

`src/index.test.ts` asserts that a blank URL throws, without ever constructing a client.

Apps call `createConvexClient(requireConvexUrl())` with their own `requireConvexUrl()` and import `api` from `@<name>/client`. Add hooks and services for each domain here as the product grows.

### packages/backend

`packages/backend/package.json` exports the generated API to apps:

```json
{
  "name": "@<name>/backend",
  "private": true,
  "type": "module",
  "exports": {
    "./api": { "types": "./convex/_generated/api.d.ts", "default": "./convex/_generated/api.js" },
    "./data-model": { "types": "./convex/_generated/dataModel.d.ts" }
  },
  "scripts": {
    "dev": "convex dev",
    "codegen": "convex dev --once",
    "lint": "eslint --cache --cache-location node_modules/.cache/eslint/ --max-warnings 0 .",
    "typecheck": "tsc --noEmit -p convex/tsconfig.json",
    "test": "vitest run"
  }
}
```

After the first codegen, confirm the generated file names match these export targets.

The backend package contains these files:

- `convex/`, as in the [Convex backend files](backend-convex.md#files).
- `eslint.config.mjs`, in the standalone form from the [Convex ESLint section](backend-convex.md#eslint) plus `...turbo`.
- `vitest.config.ts`, in the backend-only form from the [Convex tests section](backend-convex.md#tests).

Its `.env.local` comes from codegen and is gitignored.

## Monorepo root

### Root package.json

```json
{
  "name": "<name>",
  "private": true,
  "packageManager": "pnpm@<11.x.y>",
  "engines": { "node": ">=24 <25" },
  "scripts": {
    "prepare": "git config core.hooksPath .githooks || true",
    "dev": "turbo run dev",
    "build": "turbo run build --concurrency=1",
    "lint": "turbo run lint --concurrency=2",
    "typecheck": "turbo run typecheck --concurrency=2",
    "test": "turbo run test --concurrency=2",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "verify": "pnpm format:check && turbo run lint typecheck test --concurrency=2 && turbo run build --concurrency=1"
  },
  "devDependencies": {
    "@vllnt/eslint-config": "catalog:",
    "@vllnt/typescript": "catalog:",
    "eslint": "catalog:",
    "prettier": "catalog:",
    "turbo": "catalog:",
    "typescript": "catalog:"
  }
}
```

Two capacity rules shape these scripts (see [Lean defaults](baseline.md#lean-defaults)):

- Builds run one at a time (`--concurrency=1`), so a web build and a mobile export never overlap.
- `verify` runs the cheap checks first, then the builds. [CI](baseline.md#ci) does the same.

When `apps/mobile` exists, add `check:expo` to the first turbo command in `verify` (`turbo run lint typecheck test check:expo --concurrency=2`) and to CI, so the Expo SDK alignment check is not lost with the app's own `verify`.

There is no root `eslint.config`. Each workspace owns its config, and the root runs turbo. Every workspace config appends `...turbo` from `@vllnt/eslint-config/turbo`, so any environment variable a workspace reads must be declared in `turbo.json` (see [turbo.json](#turbojson)).

There is no root `tsconfig.json`. Each workspace owns its own, and editors use the nearest one. An empty root config would fail `tsc --showConfig` (TS18002) in [check 5](verification.md#checks).

### pnpm-workspace.yaml

```yaml
packages:
  - "apps/*"
  - "packages/*"

catalog:
  "@vllnt/eslint-config": ^2.0.0
  "@vllnt/typescript": ^2.0.0
  eslint: ^9.39.5
  prettier: ^3
  turbo: ^2
  typescript: ~6.0.3
  vitest: ^<latest stable major>
  react: ^19
  "@types/react": ^19
  convex: ^1
```

Then append the [supply-chain block](baseline.md#supply-chain) as top-level keys. Write the complete file (`packages:`, `catalog:` and that block) before the first `pnpm add`.

When the monorepo has a mobile app, the Expo SDK owns the `react` version: set the catalog `react` entry to the exact version `expo install` chose, so web and mobile share one copy (unverified in a full monorepo install; check `pnpm why react` shows a single version).

Every workspace references these packages as `"catalog:"`. pnpm resolves each range under the age policy. Add a package to the catalog when a second workspace needs it.

### turbo.json

```json
{
  "globalDependencies": ["**/.env.*local"],
  "globalEnv": ["NODE_ENV", "LOG_LEVEL", "CONVEX_ENV"],
  "tasks": {
    "transit": { "dependsOn": ["^transit"] },
    "build": {
      "dependsOn": ["^build"],
      "env": ["NEXT_PUBLIC_*", "EXPO_PUBLIC_*"],
      "inputs": ["$TURBO_DEFAULT$", ".env*"],
      "outputs": [".next/**", "!.next/cache/**", "dist/**"]
    },
    "dev": { "cache": false, "persistent": true },
    "lint": { "dependsOn": ["transit"] },
    "typecheck": { "dependsOn": ["transit"] },
    "test": { "dependsOn": ["transit"], "outputs": ["coverage/**"] },
    "clean": { "cache": false }
  }
}
```

The `transit` task makes lint, typecheck and test re-run when a dependency's source changes, while the tasks still run in parallel. A plain task with no `dependsOn` would serve stale cache hits.

Rules for environment variables:

- Every variable that generated code reads must appear in `globalEnv` or in a task's `env`. Otherwise `turbo/no-undeclared-env-vars` fails lint, and turbo serves builds made with other values.
- `NEXT_PUBLIC_*` and `EXPO_PUBLIC_*` are hashed into `build` because they are inlined at build time.
- When a feature reads a new variable, add it in the same change.
- Add the optional `$schema` key from the turbo docs if wanted.

When `apps/mobile` exists, add `"check:expo": { "cache": false }`: its result depends on the network, not on file inputs.

Other choices in this file:

- Leave `ui` unset; the interactive terminal UI is poor in CI logs.
- Add a per-package `pkg#task` override only for a measured need.
