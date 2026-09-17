---
name: capability-workspace-turborepo
description: Audit and repair Turborepo and package-workspace boundaries, public exports, task graphs, affected builds, and cache correctness using repository conventions and measured evidence.
---

# Capability Workspace Turborepo

Inspect, validate, or make authorized workspace repairs. Discover the actual package manager, workspace layout, package names, task runner/version, and repository policy. For a non-Turbo workspace, inspect manifests/native scripts and mark Turbo-only checks not applicable; do not impose a layout, scope, barrel, or naming convention.

## Procedure

1. Record mode, candidate revision, agreed base, consumers, constraints, workspace definitions, manifests/exports, lockfile, task configuration, scripts, and installed runner help. File moves, package renames, installs, export changes, remote caches, publishing, and external changes need applicable authority.
2. Resolve imports against declared package names and public export maps, including conditions/subpaths. Fix unexported deep imports through a supported entry point or deliberate API addition; do not rewrite an explicitly exported `/src/` path blindly.
3. Check declared runtime/development/peer dependencies against actual use. Hoisting cannot supply a package contract; preserve module formats, types, side effects, and consumer compatibility. Test packed contents and an isolated consumer when distribution changes.
4. Build package/task graphs from manifests and configuration. Check cycles, prerequisites, generated inputs, outputs, consumers, and long-running tasks; fix causes rather than globally forcing order or disabling validation.
5. Select work from the explicit scope or complete diff, including renames, deletions, shared config, locks, and transitive dependents. Use runner dry-run/graph help when installed, otherwise manual analysis; a dry run proves selection, not execution. Unknown mapping requires conservative targets or authorized full validation.
6. Separate dependency from result caches. Review inputs, environment hashing, outputs, toolchain/platform, invalidation, transfer/retention, and reader/writer trust. Never cache secrets or side-effectful tasks; untrusted code must not poison privileged consumers.
7. Prove unchanged reruns restore complete outputs, changed source/dependency/configuration/environment invalidates, and cached/uncached behavior agrees. Compare equivalent cold/warm measurements before calling a cache beneficial.
8. For repairs, show isolated failure then success; exercise affected consumers/tasks, public subpaths, private-import rejection, valid layouts, shared dependents, and cache behavior. Compare the current workspace with the DoD; repair authorized causes and repeat invalidated graph, task, consumer, and cache checks. For material graph, export, or cache questions, use independent review and critique perspectives when available, otherwise sequential perspectives. Reuse caller evidence only when revision, base, environment, and proof remain current. Missing runner, history, consumer, or authority evidence is incomplete with its next check.

Use installed equivalents or manifest/graph inspection when Turbo is unavailable; retry only with a new hypothesis. Return scope, findings, changes or recommendations, commands/measured results, consumer compatibility, and unverified work.

## Definition of Done

- The mode, revision/base, workspace boundaries, consumers, task graph, and available runner evidence are identified.
- Package exports, dependencies, affected work, and cache inputs/outputs have applicable source and consumer evidence.
- Authorized repairs have isolated failure/success evidence plus affected task, consumer, and cache checks.
- Turbo absence is explicit and limits runner claims; manifest inspection alone does not prove task execution or cache correctness.
