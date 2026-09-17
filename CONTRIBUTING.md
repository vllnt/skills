# Contributing

Report reproducible problems through the [issue templates](https://github.com/vllnt/skills/issues/new/choose). Explain the desired result, observed behavior, and relevant environment without private data.

## Structure

| Category | Contents |
|---|---|
| `workflows/verb-subject/` | Complete user task |
| `capabilities/capability-domain-function/` | Reusable internal procedure |
| `mandatory/vllnt-subject-principles/` | Lightweight session principles |

Every folder contains `SKILL.md` with flat, single-line string frontmatter `name` matching the folder and a specific description. Optional references and examples stay inside the skill and load only when relevant. Mandatory entries have no task workflow or Definition of Done; workflows and capabilities do.

Follow [AGENTS.md](AGENTS.md) for naming, ownership, concise authoring, review, and completion. Preserve independent installation: missing peers use the underlying procedure. Consumer rules supply project-specific policy.

## Change process

1. Create a branch or fork; keep the change focused on one coherent outcome.
2. Update the owning skill and affected callers, references, and navigation. Do not introduce duplicate responsibilities or copy changing inventories.
3. Run `bash scripts/test-validate-frontmatter.sh`, `bash scripts/validate-frontmatter.sh`, `bash scripts/test-pre-commit.sh`, both documentation validator scripts, and `git diff --check`.
4. Exercise relevant success, failure, and standalone cases. State which checks were executed and which were source simulations.
5. Add an entry to `CHANGELOG.md` under `Unreleased`.
6. Review the diff for personal information, secrets, invented examples, and unnecessary private context. Open a PR against `main` with changes, evidence, and remaining limits.

Markdown skills require no build step. Publication follows [RELEASING.md](RELEASING.md); a skill change does not automatically authorize a release.

Contributions follow the [Code of Conduct](CODE_OF_CONDUCT.md) and [MIT license](LICENSE). See [vllnt](https://github.com/vllnt) for the package ecosystem.
