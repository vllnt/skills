## Contract

- Input: A TypeScript candidate, supported compiler and runtime consumers, build or emission ownership, and authorized change scope.
- Output: Effective configuration evidence, diagnosed contracts, authorized changes or recommendations, and compile, emit, packaging, or consumer results.
- Effects: May change authorized compiler configuration or presets. The caller owns broader migration and delivery.

### Acceptance

- Effective configurations, supported compiler or runtime consumers, and emission owner are identified.
- Each claimed preset behavior has applicable positive and negative diagnostics, resolution, and emit or no-emit evidence.
- Published or framework-facing changes have applicable isolated-consumer or framework-build evidence.
- Missing compiler execution is explicit; inspection alone does not establish compile or runtime behavior.

## Procedure

1. Inspect consumer instructions, scripts, lockfile, tsconfig inheritance, exports, compiler binaries, and fixtures. Record supported compiler, runtime, framework or bundler versions, module format, and emission owner.
2. Capture every affected effective configuration with the installed compiler's `--showConfig`. Resolve inheritance before editing a shared base; inspect compiler-API consumers such as linters or build plugins separately from CLI compilation.
3. Select settings by consumer: Node needs compatible module, resolution, and extensions; libraries need matching emitted JavaScript, declarations, and exports; bundled apps need supported JSX or resolution; framework-owned builds retain their required plugins and generated includes without competing emit.
4. Keep bases small. Make consumers own layout-specific roots, outputs, includes, and ambient types. Treat strictness, target, lib, types, paths, inherited relative paths, and array replacement as explicit contracts.
5. Identify the cause before using `skipLibCheck`, weaker strictness, or a compiler upgrade. State its tradeoff.
6. Verify changed presets with positive and negative diagnostic fixtures, representative resolution, and emit behavior. Inspect emitted JavaScript, declarations, and maps; execute relevant output or prove no artifacts for no-emit configurations.
7. For published presets, compile an isolated consumer installed from the packed package without workspace-only dependencies. Run affected framework or bundler builds, including generated types and JSX. For a fix, show isolated failure then success and rerun invalidated checks.
8. If TypeScript is unavailable, inspect manifests, configuration, fixtures, and package contents and report compile or emit as unexecuted. Send material compiler, package, or framework uncertainties and proof to the caller's Quality Validation pool; otherwise return the next check.

## Pitfalls

- `paths` does not rewrite emitted imports, and `types` does not polyfill runtime APIs. Test the emitted or consuming behavior.
- Compiler success alone does not prove framework compatibility or published package consumption.
