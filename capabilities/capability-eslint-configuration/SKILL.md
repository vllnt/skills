---
name: capability-eslint-configuration
description: Build, migrate, debug, and verify ESLint flat configs and shared presets, including typed linting, file scope, plugin composition, custom rules, and consumer packaging.
---

# Capability Eslint Configuration

Make intended rules apply to intended files. Inspect consumer rules, lockfile, scripts, flat config, exports, fixtures, and installed versions; use the existing package manager without downloading tools.

## Procedure

1. Set the consumer config, shared preset, or custom rule. Sample source, tests, configs, generated files, and framework files; inspect effective config with the installed CLI when available.
2. Use installed flat-config forms and deliberate order. Scope rules, globals, parsers, environments, and ignores precisely; ordinary source must not be hidden by generated-file exclusions.
3. Enable typed linting only for files in the correct TypeScript project. Preserve public preset names, severity, peer dependencies, and formatter behavior; narrowly justify exceptions.
4. For shared presets, test an isolated packed consumer without workspace leakage. For custom rules, test valid/invalid forms, rule IDs, false positives, and safe autofix followed by a second lint pass.
5. Prove effective configuration and behavior with expected pass/fail fixtures and affected real lint commands. For material scope, packaging, or rule-behavior questions, use independent review and critique perspectives when available; otherwise apply them sequentially. Reuse caller evidence only when config, candidate, environment, and proof remain current. After an authorized repair, rerun invalidated checks until criteria resolve. Unavailable ESLint yields unexecuted behavior and the next check. Do not retry unchanged evidence; return the unresolved criterion and next discriminating check.

## Definition of Done

- Target files, ignored boundaries, effective configuration, and compatibility constraints are recorded.
- Changed behavior has expected diagnostics and rule IDs in fixtures and real lint where executable.
- Shared presets work in an isolated packed consumer when their packaging changes.
- The result distinguishes configuration shape from observed rule application.
