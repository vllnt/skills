Load this file when the answers select `library` or `cli`. The [baseline](baseline.md) applies as for every workspace.

This file states what a library or CLI must satisfy. Take configuration keys and APIs from the official TypeScript, Node.js, and npm documentation and from each package's README for the installed version.

## Layout

- Single library or single CLI: the package is the repository root, with the root files from the [single-app layout](layouts.md#single-app) and no `app/`, `components/`, `public/`, or `messages/`. Code lives in `src/`, with tests next to it (`src/*.test.ts`).
- Monorepo: a library lives in `packages/<lib>` as `@<name>/<lib>`, and a CLI in `apps/cli` as `@<name>/cli`. Dev dependencies use `catalog:`, the ESLint config appends the Turbo preset, and `format`, `format:check`, `verify:changed`, `verify`, and `prepare` live only at the [monorepo root](layouts.md#monorepo).

```
<name>/
  src/index.ts  src/index.test.ts          library
  src/cli.ts  src/run.ts  src/run.test.ts  CLI
  package.json  tsconfig.json  tsconfig.build.json  eslint.config.mjs  vitest.config.ts
```

## Commands

Run in the package directory. Add by name, without versions (see [Resolve versions](baseline.md#resolve-versions)): `typescript`, `@types/node`, `eslint`, `prettier`, `@vllnt/eslint-config`, `@vllnt/typescript`, `vitest` as development dependencies. A CLI also adds `@vllnt/logger` for diagnostics.

## Library

- `package.json`: ESM, side-effect free, an `exports` map whose types and default entries point into `dist/`, `files` limited to `dist`, the [baseline scripts](baseline.md#baseline-scripts) plus a `build` from the build tsconfig and a `prepack` that builds. Private visibility keeps `private` and `UNLICENSED`; `public` sets the chosen license, and publishing to npm also removes `private` (see [Publish](#publish)).
- A published library or CLI keeps `engines` open-ended, because an upper bound would block consumers on newer Node versions. The project's own Node and pnpm versions live in `.node-version` and `packageManager`.
- `tsconfig.json` extends the `@vllnt/typescript` library preset and type-checks source and tests without emitting.
- `tsconfig.build.json` extends `tsconfig.json`, emits JavaScript and declarations from `src` into `dist`, excludes tests, and sets `incremental: false`. That setting is a temporary workaround until the `@vllnt/typescript` fix ships: the preset enables `incremental`, and the build info file lands outside `dist`, so after `dist` is deleted `tsc` sees an up-to-date cache and emits nothing, and `pnpm build` and `prepack` silently produce an empty package. Remove it once the installed preset no longer causes this; [check 13](verification.md#checks) catches a regression.
- The preset uses Node's ESM resolution, so relative imports carry the `.js` extension.
- `eslint.config.mjs` spreads the `@vllnt/eslint-config` Node.js preset and ignores coverage, `dist`, and config files.
- `vitest.config.ts` includes `src/**/*.test.ts` with at most 2 workers.
- `src/index.ts` exports one small pure function, and `src/index.test.ts` covers one passing and one failing input.

## CLI

The stack profile prefers Effect for CLIs. Start with Node's built-in argument parser and no runtime dependency beyond the logger; adopt Effect when the CLI grows commands or services.

- It shares the library's build tsconfig, ESLint, and vitest config. Its `tsconfig.json` extends the `@vllnt/typescript` Node.js preset instead.
- `package.json` declares `bin` pointing at `dist/cli.js` instead of `exports` and `sideEffects`, and adds a `start` script.
- `src/run.ts` holds the logic as a pure function from arguments to an exit code and output, so tests never spawn a process. Parsing is strict.
- `src/cli.ts` is the only file with side effects: it writes command output to stdout or stderr, sets the exit code, and logs unexpected errors through `@vllnt/logger`, never `console`.
- `--help` exits 0 with the usage text. An unknown flag fails closed with exit code 2 and the usage text. An unexpected error exits 1.
- `src/run.test.ts` covers `--help`, the default output, and an unknown flag.

## Publish

Only when Q11 is `npm`, which requires `public`:

- Ask for the npm package name. It must be a name or scope the user controls on npm; `@<name>/` is only a workspace scope.
- Remove `private` from the published package, and keep `files` limited to `dist`.
- Add a publish workflow triggered only by release tags (see [Release](lifecycle.md#lifecycle)): npm trusted publishing with provenance and no token secret, publishing never cancelled midway, and actions pinned as in [CI](baseline.md#ci). Take the steps from npm's current trusted-publishing documentation; do not invent them.
- Tell the user to register the repository as a trusted publisher on npm before the first tag.

Verification adds the library and CLI [build check](verification.md#checks).
