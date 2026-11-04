Load this file before the final verification of a scaffold, and when a check fails.

## Checks

Run the checks in order, one heavy step at a time (see [Lean defaults](baseline.md#lean-defaults)); builds come last, as in CI. Report every step as pass, fail, blocked (a needed tool is unavailable), or skipped, with a reason for each non-pass. Take each tool's commands and options from its current help.

On a failure:
- Fix the template or config. Never weaken a rule or a check.
- Rerun the checks whose evidence the repair invalidates, not just the failed one. A source edit invalidates format, lint, typecheck, test, and build. A dependency, workspace, or config edit also invalidates install, lockfile, and preset evidence.
- After any repair, also rerun the cheap final-artifact checks (1 and 2).

In a monorepo, run each check at the root unless it names a workspace; workspace checks run in the workspace that owns the file.

| # | Check | Pass condition |
|---|---|---|
| 1 | Placeholders filled | No template placeholder (`<name>`, `<owner>`, `<app>`, `<sha>`, `<path>`, `<default-branch>`, `<first>`, `<release-tag>`, image placeholders) remains in authored files. `<domain>` is exempt: it appears on purpose in the generated Convex rules |
| 2 | No secrets or hosts | Every `.env.example` line is a name with an empty value, or a comment. A secret scanner (`gitleaks` or an equivalent) finds nothing in authored files; without one, this check is blocked, not passed. Scan a copy of the authored files only: a plain directory scan also reads ignored local credentials, such as the local backend's data. Every host in authored files is `127.0.0.1`, `localhost`, or a documented public URL; a project, deployment, or analytics host fails |
| 3 | Install | `pnpm install` exits 0. A refused build script or a trust-policy skip follows the rules in [Supply chain](baseline.md#supply-chain) |
| 4 | Lockfile reproducible | A frozen-lockfile install exits 0 |
| 5 | Presets really applied | Each tsconfig's effective configuration is strict and its `extends` chain reaches a `@vllnt/typescript` preset, directly or through a local tsconfig. Each ESLint config's effective configuration includes the preset's rules, and no config imports a `config` export |
| 6 | Backend codegen | `convex/_generated/` exists, `convex/tsconfig.json` still extends the preset, and each app's `.env.local` holds the local URL (see [backend commands](backend-convex.md#commands)) |
| 7 | Format | `pnpm format:check` exits 0 |
| 8 | Lint | `pnpm lint` exits 0 with zero warnings |
| 9 | Typecheck | `pnpm typecheck` exits 0, backend included |
| 10 | Test | Every surface and package tests its generated behavior, including one failure path (for example, a CLI bad flag exits 2, and `requireConvexUrl` throws when unset); all pass. Add no helper function only to have something to test |
| 11 | Build (web) | The web build exits 0. With `@vllnt/ui`, a class only the library uses appears in the emitted CSS, which proves Tailwind scans the library under pnpm's symlinked layout |
| 12 | Build (mobile) | `check:expo` and the Expo export exit 0. If memory is short, report the export as skipped-for-capacity; `check:expo`, typecheck and test must still pass |
| 13 | Build (library/CLI) | The build exits 0, and every `exports` and `bin` target in `package.json` exists in `dist/`, also after deleting `dist/` and building again. A CLI's `--help` exits 0 and an unknown flag exits 2 |
| 14 | Agent files | Every command `AGENTS.md` lists exists as a script or an available tool (running it follows check 17's limits); `AGENTS.md` has every [required section](baseline.md#agent-files) that applies; `CLAUDE.md` is the one-line import; with a backend, Convex's AI files report a clean status |
| 15 | Hooks wired | Git's hooks path is `.githooks`, both hooks are executable, the pre-commit hook rejects a staged inert fake secret (then unstage and delete it), and the pre-commit hook runs in a second worktree |
| 16 | Parallel worktrees | `wt:new` creates two worktrees with different ports and separate local backend state; both run `pnpm dev` and `pnpm verify` at the same time with no port, state, or cache collision; `wt:rm` removes them. Capacity permitting; otherwise report it unverified |
| 17 | Lifecycle scripts | Every [lifecycle](lifecycle.md#lifecycle) script that applies exists, and each one that can run locally without outside effects passes its pass check, including its refusal case. Steps with outside effects (PR, merge, publish, deploy) are checked for presence and refusal only |
| 18 | Task graph and cache | Monorepo: every workspace is in the task graph, no package depends on an app, and there are no cycles. Pass checks 1 and 2 of the [task graph target](vstack/capabilities/workspace-turborepo/references/task-graph-target.md) hold locally. Its CI check 3 stays unverified until CI runs on a pull request |
| 19 | Feature checks | When selected: auth (see [Auth](backend-convex.md#auth)), MCP (see [MCP endpoint](backend-convex.md#mcp-endpoint)), and a valid self-hosted compose file (see [Self-hosted backend](backend-convex.md#self-hosted-backend)). A valid compose file proves syntax only: report the self-hosted runtime as unverified unless the stack starts and runs deployed code. Report client authentication as unverified unless it was exercised against the running backend |
| 20 | End-to-end smoke (web) | The [end-to-end smoke](web-nextjs.md#end-to-end-smoke) passes against the production build. Only a capacity skip is allowed, with the reason, and it leaves the scaffold unverified |
| 21 | Structure review | The rules the preset does not enforce yet hold: no deep import into another workspace's `src/` or `convex/`; no web-only package in mobile's dependency closure; the [Convex review rules](backend-convex.md#convex-rules); tests only in their [placements](backend-convex.md#tests), each test file collected by a runner and none outside one; no file and folder sharing a stem in one directory; every [mandatory primitive](baseline.md#mandatory-primitives) has its file or CI step |

### Capacity limits

- Follow [Lean defaults](baseline.md#lean-defaults): never run two builds at once.
- When free memory is low, run check 20 alone after every build has finished; skip it or the mobile export only as a last resort, and report the scaffold unverified for that row.
- Stop every local backend you started for checks 6 and 16. Its data stays in ignored local directories.

## Report

Give the user a final report with:
- The plan as built: surfaces, run location, the packages with the versions actually installed, and any prereleases with reasons.
- The checks table above with a status per row.
- The commands to start working: `task:start`, `dev`, `verify`, and how to link a real backend deployment and set its secrets.
- Anything left for the user: logins for the selected hosted targets, linking a backend deployment, store assets, an analytics vendor.

## Known failure modes

- Typed lint errors on config files or generated `.d.ts`: the ESLint ignores are missing ([web files](web-nextjs.md#files)).
- A backend hook throws at runtime: the provider is not mounted in the root layout ([web files](web-nextjs.md#files), [backend wiring](mobile-expo.md#backend-wiring)).
- Two worktrees fight over a port or a backend: a script uses a fixed port or the shared main-checkout settings ([Parallel worktrees](lifecycle.md#parallel-worktrees)).
