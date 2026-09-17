---
name: capability-eslint-configuration
description: Build, migrate, debug, and verify ESLint flat configs and shared presets, including typed linting, file scope, plugin composition, custom rules, and consumer packaging.
---

## Contract

- Input: Consumer config, shared preset or custom rule, lockfile, scripts, flat config, exports, fixtures, and installed versions.
- Output: Effective configuration, expected diagnostics, packaging evidence, and unexecuted behavior or remaining gaps.
- Effects: Authorized configuration or rule changes using the existing package manager. It does not download tools.

### Acceptance

- Target files, ignored boundaries, effective configuration, and compatibility constraints are recorded.
- Changed behavior has expected diagnostics and rule IDs in fixtures and real lint where executable.
- Shared presets work in an isolated packed consumer when packaging changes.
- Configuration shape remains distinct from observed rule application.

## Procedure

1. Set the consumer config, shared preset, or custom rule. Sample source, tests, configs, generated files, and framework files; inspect effective configuration with the installed CLI when available.
2. Use installed flat-config forms and deliberate order. Scope rules, globals, parsers, environments, and ignores precisely; keep ordinary source outside generated-file exclusions.
3. Enable typed linting only for files in the correct TypeScript project. Preserve public preset names, severity, peer dependencies, and formatter behavior; narrowly justify exceptions.
4. For shared presets, test an isolated packed consumer. For custom rules, test valid/invalid forms, rule IDs, false positives, and safe autofix followed by a second lint pass.
5. Prove effective configuration and behavior with expected pass/fail fixtures and affected real lint commands.
6. Return material scope, packaging, or rule-behavior uncertainties and current evidence to the caller's quality validation. When standalone, return unexecuted behavior and the next check. After an authorized repair, rerun invalidated checks.

## Pitfalls

- A flat config that parses does not prove it applies; inspect the effective config and run a pass/fail fixture.
- A generated-file ignore can hide ordinary source; sample both intended exclusions and normal source paths.
