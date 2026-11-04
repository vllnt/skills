Load this file when the answers select `library` or `cli`. The [baseline](baseline.md) applies as for every workspace.

## Layout

- Single library or single CLI: the package is the repository root, with the root files from the [single-app layout](layouts.md#single-app) and no `app/`, `components/`, `public/`, or `messages/`. Code lives in `src/`, with tests next to it (`src/*.test.ts`).
- Monorepo: a library lives in `packages/<lib>` as `@<name>/<lib>`, and a CLI in `apps/cli` as `@<name>/cli`. Dev dependencies use `catalog:`, the ESLint config appends `...turbo` from `@vllnt/eslint-config/turbo`, and `format`, `format:check`, `verify`, and `prepare` live only at the [monorepo root](layouts.md#monorepo-root).

```
<name>/
  src/index.ts  src/index.test.ts          library
  src/cli.ts  src/run.ts  src/run.test.ts  CLI
  package.json  tsconfig.json  tsconfig.build.json  eslint.config.mjs  vitest.config.ts
```

## Commands

Run in the package directory:

```sh
pnpm add -D typescript@~6.0.3 @types/node@^24 eslint@^9.39.5 prettier@^3 \
  @vllnt/eslint-config@^2.0.0 @vllnt/typescript@^2.0.0 vitest
```

A CLI also runs `pnpm add @vllnt/logger@^0.1.2` for diagnostics.

## Library

`package.json`:

```json
{
  "name": "<name>",
  "version": "0.1.0",
  "private": true,
  "license": "UNLICENSED",
  "type": "module",
  "sideEffects": false,
  "exports": { ".": { "types": "./dist/index.d.ts", "default": "./dist/index.js" } },
  "files": ["dist"],
  "engines": { "node": ">=24" },
  "scripts": {
    "build": "tsc -p tsconfig.build.json",
    "lint": "eslint --cache --cache-location node_modules/.cache/eslint/ --max-warnings 0 .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "prepack": "pnpm build"
  }
}
```

`"private": true` and `"license": "UNLICENSED"` are the private-visibility defaults. `public` replaces the license with the chosen one, and publishing to npm also removes `private` (see [Publish](#publish)). A published library or CLI keeps `engines` open-ended, because an upper bound would block consumers on newer Node majors; the development pins are `.node-version` and `packageManager`. Add the root scripts from [baseline scripts](baseline.md#baseline-scripts) in a single-package repository.

`tsconfig.json` type-checks source and tests:

```json
{
  "extends": "@vllnt/typescript/node-library.json",
  "compilerOptions": { "noEmit": true, "types": ["node"] },
  "include": ["src"]
}
```

`tsconfig.build.json` emits JavaScript and declarations without tests; it inherits the preset through `tsconfig.json`:

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "incremental": false,
    "noEmit": false,
    "outDir": "dist",
    "rootDir": "src"
  },
  "exclude": ["src/**/*.test.ts"]
}
```

`incremental: false` matters for the CLI: its preset enables `incremental`, and the resulting `tsconfig.build.tsbuildinfo` lands in the package root, outside `dist`. After `dist` is deleted, `tsc` then sees an up-to-date cache and emits nothing, so `pnpm build` and `prepack` silently produce an empty package.

The preset uses `NodeNext` resolution, so relative imports carry the `.js` extension: `import { isBlank } from "./index.js"`.

`eslint.config.mjs`:

```js
import { nodejs } from "@vllnt/eslint-config/nodejs";

export default [
  {
    ignores: [
      "coverage/**",
      "dist/**",
      "node_modules/**",
      "*.config.{js,mjs,cjs,ts}",
    ],
  },
  ...nodejs,
];
```

`vitest.config.ts`:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: { include: ["src/**/*.test.ts"], maxWorkers: 2 },
});
```

`src/index.ts` exports one pure function, `isBlank(value: string): boolean`, which returns `value.trim().length === 0`. `src/index.test.ts` asserts that `isBlank("  ")` is `true` and `isBlank("a")` is `false`.

## CLI

The stack profile prefers Effect for CLIs. This minimal recipe uses `node:util` `parseArgs` to start with no runtime dependency beyond the logger; adopt Effect when the CLI grows commands or services.

The CLI uses the library's `tsconfig.build.json`, `eslint.config.mjs`, and `vitest.config.ts` unchanged. Its `tsconfig.json` extends `@vllnt/typescript/nodejs.json` instead, with the same `compilerOptions` and `include`.

`package.json` differs from the library's:

- `"bin": { "<name>": "./dist/cli.js" }` replaces `exports` and `sideEffects`.
- `"start": "node dist/cli.js"` is added to the scripts.

`src/run.ts` holds the logic as a pure function, so tests never spawn a process:

```ts
import { parseArgs } from "node:util";

export type RunResult = { readonly exitCode: number; readonly output: string };

const usage = "Usage: <name> [--help] [--name <value>]";

export function run(argv: readonly string[]): RunResult {
  try {
    const { values } = parseArgs({
      args: [...argv],
      options: {
        help: { short: "h", type: "boolean" },
        name: { type: "string" },
      },
      strict: true,
    });
    if (values.help === true) {
      return { exitCode: 0, output: usage };
    }
    return { exitCode: 0, output: `Hello, ${values.name ?? "world"}` };
  } catch (error) {
    const reason = error instanceof Error ? error.message : "invalid arguments";
    return { exitCode: 2, output: `${reason}\n${usage}` };
  }
}
```

`src/cli.ts` is the only file with side effects:

```ts
#!/usr/bin/env node
import { createBackendLogger } from "@vllnt/logger";

import { run } from "./run.js";

const logger = createBackendLogger("cli");

try {
  const { exitCode, output } = run(process.argv.slice(2));
  (exitCode === 0 ? process.stdout : process.stderr).write(`${output}\n`);
  process.exitCode = exitCode;
} catch (error) {
  logger.error("cli_error", {
    errorName: error instanceof Error ? error.name : "unknown",
  });
  process.exitCode = 1;
}
```

Command output goes to `process.stdout` and `process.stderr`; diagnostics go through `@vllnt/logger`, never `console`. An unknown flag fails closed with exit code 2 and the usage text.

`src/run.test.ts` covers `--help` (exit 0, usage text), the default greeting, and an unknown flag (exit 2 with the usage text).

## Publish

Only when Q11 is `npm`, which requires `public`:

- Ask for the npm package name. It must be a name or scope the user controls on npm; `@<name>/` is only a workspace scope.
- Remove `"private": true` from the published package, and keep `files` limited to `dist`.
- Add `.github/workflows/publish.yml`: triggered by `v*.*.*` tags, npm trusted publishing with provenance (`id-token: write`) and no token secret, publish `concurrency` with `cancel-in-progress: false`, and actions pinned to commit SHAs as in [CI](baseline.md#ci). Take the publish steps from npm's trusted-publishing documentation for the pinned action versions; do not invent them.
- Tell the user to register the repository as a trusted publisher on npm before the first tag.

Verification adds the library and CLI [build check](verification.md#checks).
