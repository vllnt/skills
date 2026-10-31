## Contract

- Input: A workspace candidate, mode, agreed base, consumers, constraints, package manager, task runner, and authorized repair scope.
- Output: Workspace findings, supported repairs or recommendations, task or consumer evidence, cache evidence, and unverified work.
- Effects: Audit returns findings without repairs; repair mode may change the authorized workspace scope. File moves, renames, installs, export changes, remote caches, publishing, and external changes need applicable authority.

### Acceptance

- The mode, revision or base, workspace boundaries, consumers, task graph, and runner evidence are identified.
- Package exports, dependencies, affected work, and cache inputs or outputs have applicable source and consumer evidence.
- Authorized repairs have isolated failure or success evidence plus affected task, consumer, and cache checks.
- Turbo absence is explicit and limits runner claims; manifest inspection alone does not prove task execution or cache correctness.

## Procedure

1. Discover package manager, workspace layout, package names, runner or version, policy, candidate revision, base, consumers, constraints, manifests or exports, lockfile, task configuration, scripts, and installed runner help. For a non-Turbo workspace, inspect manifests and native scripts and mark Turbo-only checks not applicable.
2. Resolve imports against declared package names and public export maps, including conditions and subpaths. For authorized repair, fix unexported deep imports through a supported entry point or deliberate authorized API addition.
3. Check runtime, development, and peer dependencies against actual use. Preserve module formats, types, side effects, and consumer compatibility; test packed contents and an isolated consumer when distribution changes.
4. Build package and task graphs from manifests and configuration. Check cycles, prerequisites, generated inputs, outputs, consumers, and long-running tasks; in repair mode, fix authorized causes rather than globally forcing order or disabling validation.
5. Select work from explicit scope or complete diff, including renames, deletions, shared configuration, locks, and transitive dependents. Use runner dry-run or graph help when installed, otherwise manual analysis; choose conservative targets or authorized full validation for unknown mapping.
6. Separate dependency and result caches. Review inputs, environment hashing, outputs, toolchain or platform, invalidation, transfer or retention, and reader or writer trust. Prove unchanged reruns restore complete outputs, changed source, dependency, configuration, or environment invalidates, and cached and uncached behavior agrees.
7. For repairs, show isolated failure then success. Exercise consumers or tasks, public subpaths, private-import rejection, valid layouts, shared dependents, and cache behavior. Send material graph, export, or cache uncertainties and proof to the caller's Quality Validation pool; otherwise return the next check.

## Pitfalls

- Hoisting does not supply a package contract. Declare and test the dependency at its owning package.
- A runner dry run proves selection, not execution. Never cache secrets or side-effectful tasks, and prevent untrusted code from poisoning privileged consumers.
