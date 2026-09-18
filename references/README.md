# Repository references

Canonical procedures are on-demand guidance, not discoverable skills. A workflow loads only the procedure relevant to its condition, passing its mode, scope, candidate, and evidence. Planning and assessment use effectful procedures only for their read-only criteria and proposed checks.

## Procedures

| Procedure | Canonical reference |
|---|---|
| Agent tooling review | [REFERENCE.md](capabilities/agent-tooling-review/REFERENCE.md) |
| CI optimization | [REFERENCE.md](capabilities/ci-optimization/REFERENCE.md) |
| Code architecture | [REFERENCE.md](capabilities/code-architecture/REFERENCE.md) |
| Code review | [REFERENCE.md](capabilities/code-review/REFERENCE.md) |
| Code test management | [REFERENCE.md](capabilities/code-test-management/REFERENCE.md) |
| Code tests | [REFERENCE.md](capabilities/code-tests/REFERENCE.md) |
| Compliance review | [REFERENCE.md](capabilities/compliance-review/REFERENCE.md) |
| Convex components | [REFERENCE.md](capabilities/convex-components/REFERENCE.md) |
| ESLint configuration | [REFERENCE.md](capabilities/eslint-configuration/REFERENCE.md) |
| Infrastructure costs | [REFERENCE.md](capabilities/infrastructure-costs/REFERENCE.md) |
| Infrastructure review | [REFERENCE.md](capabilities/infrastructure-review/REFERENCE.md) |
| Next.js tests | [REFERENCE.md](capabilities/nextjs-tests/REFERENCE.md) |
| Project alignment | [REFERENCE.md](capabilities/project-alignment/REFERENCE.md) |
| Quality validation | [quality-validation.md](protocols/quality-validation.md) |
| Reasoning assumptions | [REFERENCE.md](capabilities/reasoning-assumptions/REFERENCE.md) |
| Release changelog | [REFERENCE.md](capabilities/release-changelog/REFERENCE.md) |
| Release readiness | [REFERENCE.md](capabilities/release-readiness/REFERENCE.md) |
| Runtime performance | [REFERENCE.md](capabilities/runtime-performance/REFERENCE.md) |
| Stack packages | [REFERENCE.md](capabilities/stack-packages/REFERENCE.md) |
| TypeScript configuration | [REFERENCE.md](capabilities/typescript-configuration/REFERENCE.md) |
| UI accessibility | [REFERENCE.md](capabilities/ui-accessibility/REFERENCE.md) |
| Web performance | [REFERENCE.md](capabilities/web-performance/REFERENCE.md) |
| Workspace Turborepo | [REFERENCE.md](capabilities/workspace-turborepo/REFERENCE.md) |

Maintainers run `python3 scripts/bundle-references.py` after changing a canonical reference or a workflow link, then `python3 scripts/bundle-references.py --check`. The generated `workflows/*/references/vstack/` copies travel with each workflow; they require no runtime build step.

Other repository guidance:

- [Vstack](vstack.md) — user-selected stack and package reuse rules for consumer projects.
- [Skill behavior evaluations](skill-evaluations.md) — isolated scenarios, structural checks, and evidence reporting.

Keep contributor rules in the root `AGENTS.md`. Keep workflow-specific guidance in that workflow’s own `references/` folder. Load reference material only when relevant; this directory is not a required shared instruction layer.
