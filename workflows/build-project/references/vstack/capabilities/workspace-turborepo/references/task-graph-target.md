# Turbo task graph and CI target

The target for a new Turbo workspace, or for one being aligned to it. It states requirements and pass checks only. Take configuration keys, flags, and CI syntax from the current Turbo, package manager, and CI provider documentation at run time.

## Requirements

- Every repeatable task is a Turbo task: lint, typecheck, test, build, and code generation. Package scripts keep the same names everywhere, so the root, hooks, and CI call the same tasks.
- The task graph is exact. Each task depends on what it really consumes, such as upstream builds or generated code, and on nothing else, so independent tasks run in parallel.
- Cache keys are exact. Each task declares its inputs, its outputs, and every environment variable it reads. Long-running and side-effectful tasks, such as dev servers and deploys, are never cached. Outputs that hold secrets are never cached.
- The local cache is always on. When the project runs in the cloud or in hybrid mode, a remote cache is on and shared by CI, developers, and every local worktree. Only trusted runs, such as CI on the default branch or authenticated developers, write to it; untrusted pull requests from forks only read it.
- Pull requests run only the affected packages and their dependents. When a root input changes (lockfile, workspace or Turbo configuration, shared tooling config, CI definition), they run the full graph. When the affected set cannot be determined, for example because the base is missing, they also run the full graph.
- CI runs the same `verify` contract as local work. It reuses the package store and the Turbo cache, parallelizes independent work where the measured workload gains from it (Turbo already schedules independent tasks, and extra jobs add setup time and cost), keeps required check names stable, and cancels superseded runs of the same pull request. Failed, cancelled, or unexpectedly skipped work fails the run.
- Concurrency is a setting, not a constant. CI sizes it to the runner. Local runs stay capped at two heavy tasks and one build at a time; when several worktrees share a machine, the cap applies across all of them.

## Pass checks

1. A second `verify` with no changes is a full cache hit for every cacheable task, and it restores every declared output. A changed source, dependency, configuration, or declared environment value invalidates the affected tasks, and cached and uncached results agree.
2. A change in one package runs only that package and its dependents, and a change to a root input runs the full graph.
3. A pull request with no relevant change finishes from cache in CI, and its required checks still report success. Deploys, publishing, and other side effects are never satisfied from cache.

Run [CI optimization](../../ci-optimization/REFERENCE.md) for CI measurement and protection evidence.
