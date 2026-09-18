# Contributing

Report reproducible problems through the [issue templates](https://github.com/vllnt/skills/issues/new/choose). Explain the desired result, observed behavior, and relevant environment without private data.

## Structure

| Category | Contents |
|---|---|
| `workflows/verb-subject/` | Complete user task |
| `mandatory/vllnt-subject-principles/` | Lightweight session principles |
| `references/capabilities/<subject>/REFERENCE.md` | Canonical on-demand procedure |

The public catalog includes workflows and mandatory entries, each with a `SKILL.md` file with flat, single-line string frontmatter whose `name` matches the folder and whose description is specific. The repository-local `.agents/skills/manage-skill/SKILL.md` is outside that public catalog but may be discovered by repository-aware hosts. Canonical procedures have no skill metadata; they use Contract, Acceptance, Procedure, and targeted Pitfalls where needed. Optional references and examples load only when relevant. Workflows place Goal and Definition of Done before Workflow; mandatory entries contain Principles only. Do not repeat a skill name as a body title.

Follow [AGENTS.md](AGENTS.md) for naming, ownership, concise authoring, review, and completion. Preserve independent installation: missing peers use the underlying procedure. Consumer rules supply project-specific policy.

## Change process

1. Create a branch or fork; keep the change focused on one coherent outcome.
2. Update the owning skill and affected callers, references, and navigation. Do not introduce duplicate responsibilities or copy changing inventories.
3. Run `bash scripts/test-validate-frontmatter.sh`, `bash scripts/test-pre-commit.sh`, `python3 scripts/test-validate-docs.py`, `python3 scripts/validate-docs.py`, `python3 scripts/test-bundle-references.py`, `python3 scripts/bundle-references.py`, `python3 scripts/bundle-references.py --check`, and `git diff --check`.
4. Exercise relevant success, failure, and standalone cases. State which checks were executed and which were source simulations.
5. Add an entry to `CHANGELOG.md` under `Unreleased`.
6. Review the diff for personal information, secrets, invented examples, and unnecessary private context. Open a PR against `main` with changes, evidence, and remaining limits.

Markdown skills require no build step. Publication follows [RELEASING.md](RELEASING.md); a skill change does not automatically authorize a release.

Contributions follow the [Code of Conduct](CODE_OF_CONDUCT.md) and [MIT license](LICENSE). See [vllnt](https://github.com/vllnt) for the package ecosystem.
