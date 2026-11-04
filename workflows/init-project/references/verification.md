Load this file before the final verification of a scaffold, and when a check fails.

## Checks

Run the checks in order, one heavy step at a time (see [Lean defaults](baseline.md#lean-defaults)); builds come last, as in CI. Report every step as pass, fail, blocked (a needed tool is unavailable), or skipped, with a reason for each non-pass.

On a failure:
- Fix the template or config. Never weaken a rule or a check.
- Rerun the checks whose evidence the repair invalidates, not just the failed one. A source edit invalidates format, lint, typecheck, test, and build. A dependency, workspace, or config edit also invalidates install, lockfile, and preset evidence.
- After any repair, also rerun the cheap final-artifact checks (1 and 2).

Commands below are for a single app. In a monorepo, run them at the root unless the command column names a workspace. `<web>`, `<mobile>` and `<backend>` mean `@<name>/web`, `@<name>/mobile` and `@<name>/backend`. `<pkg>` means the library or CLI package.

| # | Check | Command (single app / monorepo) | Pass condition |
|---|---|---|---|
| 1 | Placeholders filled | placeholder scan in [Scan commands](#scan-commands) | no hits |
| 2 | No secrets or hosts | every `.env.example` line matches `^[A-Z0-9_]+=$` or is a comment; secret and host scans in [Scan commands](#scan-commands); `gitleaks` over authored files when installed (see [Scan commands](#scan-commands)); plain `gitleaks dir .` also reads gitignored local credentials such as `.convex/` | `.env.example` values empty; no secret-pattern hits; every host found is `127.0.0.1`, `localhost`, or a documented public URL (schema URLs, package docs) |
| 3 | Install | `pnpm install` | exit 0. On a build-script refusal, review it and add an `allowBuilds` entry (see [Supply chain](baseline.md#supply-chain)), then re-run. `ERR_PNPM_NO_MATURE_MATCHING_VERSION` after a "Skipped trust downgrades" warning follows the trust-downgrade rule in [Supply chain](baseline.md#supply-chain) |
| 4 | Lockfile reproducible | `pnpm install --frozen-lockfile` | exit 0 |
| 5 | Presets really applied | per tsconfig: `pnpm exec tsc --showConfig -p <tsconfig>`; per ESLint config: `pnpm exec eslint --print-config <one source file>`; both run from the workspace that owns the file (monorepo: `pnpm --filter <workspace> exec ...`, because there is no root ESLint config); `grep -rn "import { config }" --include='eslint.config.*' --exclude-dir=node_modules .` | `--showConfig` shows `"noUncheckedIndexedAccess": true` and the `extends` chain reaches a `@vllnt/typescript` preset, directly or through a local tsconfig (`tsconfig.build.json` -> `./tsconfig.json` -> preset); the ESLint config contains `unicorn/filename-case`; no grep hits |
| 6 | Backend codegen | `CONVEX_AGENT_MODE=anonymous pnpm exec convex dev --once` / `CONVEX_AGENT_MODE=anonymous pnpm --filter <backend> codegen` | `convex/_generated/` exists; `convex/tsconfig.json` still extends the preset; the app `.env.local` files hold the local URL (see [backend commands](backend-convex.md#commands)) |
| 7 | Format | `pnpm format:check` | exit 0 |
| 8 | Lint | `pnpm lint` | exit 0, zero warnings |
| 9 | Typecheck | `pnpm typecheck` | exit 0, backend included |
| 10 | Test | `pnpm test` | every surface and package tests its generated behavior, including one failure path (for example a CLI bad flag exits 2, `requireConvexUrl` throws when unset); all pass. Add no helper function only to have something to test |
| 11 | Build (web) | `pnpm build` / `pnpm --filter <web> build` | exit 0. With `@vllnt/ui`: `grep -rl "bg-primary" .next/static` (under the web app) finds the emitted CSS |
| 12 | Build (mobile) | `pnpm check:expo && pnpm build` / `pnpm --filter <mobile> check:expo && pnpm --filter <mobile> build` | exit 0. If memory is short, report the export as skipped-for-capacity; `check:expo`, typecheck and test must still pass |
| 13 | Build (library/CLI) | `pnpm build` / `pnpm --filter <pkg> build` | exit 0. Every `exports` and `bin` target declared in `package.json` exists in `dist/`. For a CLI, also `node dist/cli.js --help` exits 0 and an unknown flag exits 2 (in a monorepo, run it from the package directory) |
| 14 | Hooks wired | `git config core.hooksPath`; `test -x .githooks/pre-commit && test -x .githooks/pre-push` | `.githooks`; both executable |
| 15 | Agent files | `AGENTS.md` lists only scripts that exist; `head -1 CLAUDE.md` is `@AGENTS.md`; with a backend: `pnpm exec convex ai-files status` (monorepo: `pnpm --filter <backend> exec convex ai-files status`) | all true, status clean |
| 16 | Monorepo graph | `pnpm turbo run typecheck --dry=json` | every workspace listed; no package depends on an app; no cycles |
| 17 | Feature checks | auth (see [Auth](backend-convex.md#auth)), MCP (see [MCP endpoint](backend-convex.md#mcp-endpoint)), self-hosted `docker compose config` (see [Self-hosted backend](backend-convex.md#self-hosted-backend)) | pass, when the feature is selected. `docker compose config` proves syntax only: report the self-hosted runtime as unverified unless the local stack starts and runs deployed code. Report client authentication as unverified unless it was exercised against the running backend |
| 18 | End-to-end (optional) | `pnpm exec playwright install chromium && pnpm test:e2e` / the same with `pnpm --filter <web>` | pass, or skipped-for-capacity with the reason |

### Scan commands

Authored files are the files git tracks or would track. `git grep --untracked` skips gitignored paths (`.next/`, `.convex/`, `dist/`, `node_modules/`); `scope` also excludes the generated `pnpm-lock.yaml`, `next-env.d.ts`, `_generated/`, and the files Convex `ai-files` writes (`.agents/`, `.claude/skills/`, `skills-lock.json`). `<domain>` is not scanned: it appears on purpose in the generated Convex rules.

```sh
scope=(-- . ':(exclude)pnpm-lock.yaml' ':(exclude,glob)**/next-env.d.ts' ':(exclude,glob)**/_generated/**' \
  ':(exclude,glob)**/.agents/**' ':(exclude,glob)**/.claude/skills/**' ':(exclude,glob)**/skills-lock.json')

git grep -nIF --untracked -e '<name>' -e '<lib>' -e '<owner>' -e '<app>' -e '<sha>' \
  -e '<path>' -e '<11.x.y>' -e '<latest' -e '<default-branch>' -e '<first>' \
  -e '<release-tag>' -e '<convex-backend-image>' -e '<convex-dashboard-image>' "${scope[@]}"

git grep -nIE --untracked -e '-----BEGIN [A-Z ]*PRIVATE KEY-----' -e '(AKIA|ASIA)[0-9A-Z]{16}' \
  -e 'gh[pousr]_[A-Za-z0-9]{36}' -e 'npm_[A-Za-z0-9]{36}' -e 'xox[abprs]-[A-Za-z0-9-]{10,}' \
  -e '(^|[^A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}' -e 'phc_[A-Za-z0-9]{20,}' \
  -e '[A-Za-z0-9-]+\.(convex\.(cloud|site)|vercel\.app)' "${scope[@]}"

git grep -hIEo --untracked 'https?://[^/"'"'"' )]+' "${scope[@]}" \
  | grep -vE '^https?://(127\.0\.0\.1|localhost)(:|$)' | sort -u

tmp=$(mktemp -d) && git ls-files -coz --exclude-standard | xargs -0 cp --parents -t "$tmp" \
  && gitleaks dir --no-banner "$tmp"; status=$?; rm -rf "$tmp"; (exit "$status")
```

The first two commands pass with no output. List the hosts from the third and confirm each is a documented public URL; a project, deployment, or analytics host fails the check.

### Capacity limits

- Follow [Lean defaults](baseline.md#lean-defaults): never run two builds at once.
- Skip check 18 and the mobile export when free memory is low, and say so.
- Stop the local Convex backend from check 6 afterwards. Its data stays in `.convex/` (gitignored).

## Report

Give the user a final report with:
- The plan as built: surfaces, the packages with the versions actually installed, and any pinned prereleases with reasons.
- The checks table above with a status per row.
- The commands to start working: `pnpm dev`; `convex dev` to link a real deployment; `convex env set` for secrets.
- Anything left for the user: link a backend deployment, add store assets, choose an analytics vendor.

## Known failure modes

- Typed lint errors on config files or generated `.d.ts`: the shared `ignores` block is missing ([web files](web-nextjs.md#files)).
- A backend hook throws at runtime: the provider is not mounted in the root layout ([web files](web-nextjs.md#files), [backend wiring](mobile-expo.md#backend-wiring)).
