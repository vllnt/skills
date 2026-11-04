Load this file when planning and scaffolding a project's run location, development lifecycle, CI, and parallel worktrees.

This file states requirements and pass checks. Generate scripts and workflow files from the current documentation of the tools involved (git, the Git host and its CLI, the CI provider, Turbo, Convex, the web host, EAS). Generating the automation is part of the scaffold. Running a step with outside effects (opening or merging a PR, publishing, deploying) happens only when the user asks.

## Run location

Detect the setup before asking [Q13](questions.md#questions), and offer the detected mode as the default. Probe only what the selected surfaces need:

- Git: an existing remote and its host, and whether the host's CLI is authenticated.
- Docker, when a backend is selected (self-hosted backend in local-only mode).
- The login state of the CLI for each selected hosted target only: Convex for a backend, the web host for a web deploy, EAS for mobile.

Default: `cloud` when the Git host and every selected hosted target are authenticated; `local-only` when none are; `hybrid` otherwise. Report what each mode would still need, such as a login or Docker. Never log in, create a remote, or create a hosted project without the user's request.

| Mode | Behavior |
|---|---|
| `local-only` | Nothing leaves the machine. The backend is self-hosted in Docker, the hooks and `pnpm verify` are the gate, `preview` serves a local production build, and `deploy` runs the self-hosted stack. No hosted CI, previews, or remote cache are generated. |
| `cloud` | Hosted CI on the Git host, a preview deploy per PR (web host preview plus a backend preview deployment), hosted production deploys from release tags, EAS for mobile, and a remote task cache. |
| `hybrid` | Local development with local backends in every worktree, plus the `cloud` CI, previews, production, and remote cache. |

## Lifecycle

Every step has one script at the project root, so humans, agents, hooks, and CI call the same names. Each script fails closed: on any failed precondition it exits non-zero and changes nothing.

| Step | Script | Requirement | Pass check |
|---|---|---|---|
| Start a task | `task:start <slug>` | Creates a worktree and branch for the task from the up-to-date default branch, through `wt:new`; accepts an optional issue reference for the branch and PR | Creates the branch and worktree; refuses an existing slug or a dirty main checkout |
| Develop | `dev` | Starts the dev servers on the worktree's ports, bound to localhost | Responds on the worktree's port |
| Test | `test` | Runs the test suites (see [Baseline scripts](baseline.md#baseline-scripts)) | Exit 0 on the scaffold |
| Verify | `verify` | The same contract CI runs | Exit 0 on the scaffold |
| Open a PR | `pr` | Runs `verify`, pushes the branch, and opens a draft PR from the PR template, linking the issue. Issue and PR templates exist when the Git host supports them | Refuses on a failing `verify` or the default branch |
| Preview | `preview` | `local-only`: builds and serves a production build locally on the worktree's port. `cloud`/`hybrid`: CI deploys a preview per PR and reports its URL on the PR | Local preview serves; preview job exists in CI |
| Review | none | Multi-angle review before merge: correctness, security, tests, and UX and accessibility when there is a UI, by reviewers independent of the author; findings are resolved or rejected with a reason | `AGENTS.md` states the rule |
| Merge | `pr:merge` | Squash-merges only after required checks and review pass, then deletes the branch | Refuses while checks are pending or failing |
| Release | `release` | From the default branch: chooses the next SemVer version from the changelog, moves `[Unreleased]` under that version and date, bumps versions, and creates the tag. Publishing and production deploys run only from a release tag | Refuses off the default branch or with an empty `[Unreleased]` |
| Deploy | `deploy` | `cloud`/`hybrid`: CI deploys production from the release tag. `local-only`: rebuilds and restarts the self-hosted stack | Deploy job runs only on tags |
| Health | `health` | Checks the running app and backend (a backend health query and the web root) and fails on an error. Server code logs structured events through `@vllnt/logger` | Exit 0 against a running local stack |
| Roll back | none | `docs/rollback.md` documents redeploying the previous release tag per surface, and that backend schema changes stay backward-compatible so a rollback never needs a data migration | The document exists |
| Clean up | `wt:rm <slug>` | Removes a merged task's worktree and local branch | Refuses with uncommitted or unpushed work |

Surfaces without a step drop it: no `deploy` or `health` for a library, and `release` publishes to npm only when Q11 is `npm` (see [Publish](library-cli.md#publish)).

## CI

Applies to `cloud` and `hybrid`. CI runs on the Git host's CI; for GitHub, GitHub Actions and Dependabot. If the remote is on another host, generate nothing host-specific and report the skip.

- Triggers: pull requests to the default branch and pushes to it. Least-privilege permissions (read-only contents unless a job needs more) and a timeout on every job.
- Superseded runs of the same PR are cancelled. Default-branch runs are never cancelled. No workflow-level path filters: they leave required checks pending.
- Each run checks formatting, then runs the same contract as `verify`. In a monorepo, task selection, caching, and concurrency follow the [task graph target](vstack/capabilities/workspace-turborepo/references/task-graph-target.md). A single app or single package runs everything.
- With mobile, CI also runs `check:expo`.
- With a backend, the job sets a non-secret loopback placeholder for each public backend URL, so builds that construct the client succeed without a backend.
- Pin every action to the full commit SHA of its latest release, resolved through the Git host's API at scaffold time, with the tag as a trailing comment. Never guess a SHA.
- Dependency updates for actions and npm run weekly through Dependabot (or Renovate), with a 7-day cooldown that matches the release-age gate and `@vllnt/*` exempt where the tool supports it.
- Preview and production deploy keys live only in the host's settings, one per environment.
- A release workflow runs only on release tags. Publishing never cancels midway.

## Parallel worktrees

Several agents work on one machine at the same time, one per worktree. The scaffold makes that safe:

- `wt:new <slug>` creates a worktree on a new branch from the default branch, in a sibling `../<name>.worktrees/<slug>` directory by default, or in an ignored `.worktrees/` directory inside the repository. `wt:rm <slug>` removes it.
- Every dev process gets non-colliding ports per worktree (app, local backend, end-to-end base URL, Metro), stable for that worktree and stored in an ignored worktree-local settings file that the scripts read.
- Local state is isolated per worktree: its own local backend deployment and data directory, and framework, lint, and task caches inside the worktree. The package store is shared.
- A new worktree gets fresh worktree-specific settings, plus only the selected local values from the main checkout, such as non-secret developer defaults. Copying everything can point two worktrees at the same backend. Copied or generated env files stay untracked.
- Heavy work is capped across every worktree on the machine: at most one build and two heavy check or test runs at a time. A script waits for a free slot instead of failing.
- Git hooks run in every worktree.
- `AGENTS.md` carries the [parallel-work rules](baseline.md#agent-files).

Pass check ([check 16](verification.md#checks)): two worktrees run `pnpm dev` and `pnpm verify` at the same time with no port, backend state, or cache collision.
