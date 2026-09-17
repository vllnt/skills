---
name: capability-typescript-configuration
description: Design, migrate, and verify TypeScript compiler configurations and shared presets across Node, libraries, React, and Next.js using diagnostic, emit, packaging, and consumer-build tests.
---

# Capability Typescript Configuration

Match compiler behavior to the consumer runtime and build pipeline, then prove the supported contract with real fixtures.

## Procedure

1. Inspect consumer instructions, scripts, lockfile, tsconfig inheritance, package exports, compiler binaries, and fixtures. Record supported compiler/runtime/framework/bundler versions, module format, and whether TypeScript owns emission.
2. Capture each affected effective configuration with the installed compiler's `--showConfig`; resolve inheritance before editing a shared base. Inspect compiler-API consumers such as linters/build plugins separately from CLI compilation.
3. Choose settings by consumer: Node needs a supported module/resolution pair and runtime-compatible extensions; libraries need matching emitted JS, declarations, and exports; bundled apps need bundler-supported JSX/resolution; framework-owned builds retain required plugins/generated includes and avoid competing emit.
4. Keep bases small and consumers responsible for layout-specific roots, outputs, includes, and ambient types. Treat strictness, `target`, `lib`, `types`, `paths`, inherited relative paths, and array replacement as explicit contracts; `paths` does not rewrite emitted imports and types do not polyfill runtime APIs.
5. Do not broadly suppress diagnostics with `skipLibCheck`, weaker strictness, or a compiler upgrade without identifying the cause and tradeoff.
6. Verify each changed preset with positive and negative diagnostic fixtures, representative resolution (exports, extensions, ambient types, ESM/CommonJS), and emit behavior. Inspect emitted JS, declarations, and maps; execute relevant emitted JS, or prove no artifacts for no-emit configurations.
7. For published presets, compile an isolated consumer installed from the packed package without workspace-only dependencies. Run affected framework/bundler builds including generated types and JSX; compiler success alone does not prove framework compatibility.
8. For a fix, demonstrate isolated failure then success and rerun invalidated checks. Without TypeScript, inspect manifests, config, fixtures, and package contents and report compile/emit as unexecuted. Compare the current candidate with the DoD; repair authorized gaps and repeat diagnostics and consumer checks. For material compiler, package, or framework questions, use independent review and critique perspectives when available, otherwise sequential perspectives. Reuse caller evidence only when config, candidate, environment, and proof remain current. Missing compiler, consumer, or authority evidence is incomplete with its next check.

## Definition of Done

- The effective configurations, supported compiler/runtime consumers, and emission owner are identified.
- Each claimed preset behavior has applicable positive/negative diagnostics, resolution, and emit or no-emit evidence.
- Published or framework-facing changes have applicable isolated-consumer or framework-build evidence.
- Missing compiler execution is explicit; configuration inspection alone does not establish compile or runtime behavior.
