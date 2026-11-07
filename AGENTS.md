# Vstack Skills — repository instructions

Vstack combines reusable packages, skills, and engineering methods from [vllnt](https://github.com/vllnt). This repository owns the portable skills. Consumer instructions own project architecture, commands, environments, permissions, and delivery policy.

## Session principles

At session start, read the installed `mandatory/*/SKILL.md` entries (thinking, orchestration, collaboration) before task-specific skills. Reuse them in context; reload after changes or context loss.

A description declares a trigger, not a loader; configure and verify loading in each consuming runtime. A standalone workflow must still work without these entries. Each mandatory entry keeps one concern in a `Principles` section of about 100–150 words, with no goal or completion checklist.

## Ownership

- `mandatory/`: shared thinking, orchestration, and collaboration principles. `workflows/`: complete user outcomes, named `verb-subject`.
- `references/capabilities/`: canonical internal procedures named by domain and function, with `REFERENCE.md` and focused annexes. `references/protocols/`: shared coordination procedures such as quality validation.
- `workflows/*/references/vstack/`: generated copies of only the linked canonical dependencies; never edit them. Each skill owns its `SKILL.md` and handwritten local references; a shared reference has one canonical owner; load only the needed procedure.
- [README.md](README.md) owns human navigation, [llms.txt](llms.txt) is the link index, and [roadmap.md](roadmap.md) tracks decisions and work.
- The [Vstack profile](references/vstack.md) owns stack preferences and package sources; apply it to Vstack project requests; install no frameworks in this Markdown repository.
- [.agents/skills/manage-skill/SKILL.md](.agents/skills/manage-skill/SKILL.md) maintains this collection (repository-local, excluded from the public catalog); public `manage-skills` is the portable lifecycle workflow.
- Contracts and durable decisions live in their owning artifacts; version control keeps history. No chat-only state or duplicate catalogs.

## Skill naming

Workflow verbs: `build`, `deliver`, `explain`, `explore`, `improve`, `init`, `manage`, `plan`, `review`; reuse them before adding one. `init` is reserved for interactive creation of a new project from scratch. Reference domain and function are nouns; internal procedures have no `SKILL.md`, routing name, or description metadata. Mandatory entries use `vllnt-<subject>-principles`. Names match folders and are unique across public categories, including flat installations, with no obsolete aliases. Prefixes describe intended use; they do not hide skills from a runtime.

## Authoring

- Start with one result, intrinsic effects, and the smallest useful procedure; extend an existing owner before creating another skill.
- Write for agents: direct US English, numbered sequences, parallel criteria as bullets. Keep the name in frontmatter, not as a body title.
- Workflows, including the local maintainer: `Goal` → nested `Definition of Done` → optional `Boundaries` → `Workflow`. Canonical procedures: `Contract` with Input/Output/Effects → nested `Acceptance` → `Procedure` → optional `Pitfalls`.
- Use three to five observable completion criteria; domain evidence sits beside the outcome and the procedure says how to obtain it. A complete assessment may describe an unverified target.
- Keep optional boundaries and pitfalls only for specific errors: name the failure and the permitted alternative or decisive check. Omit empty sections, generic warnings, and copied project policy. Use the [authoring templates](.agents/skills/manage-skill/references/templates.md).
- Size budgets are limits in `scripts/validate-docs.py`; stay under them rather than raising them.
- Discover consumer rules and configuration; embed no project permissions, labels, deadlines, thresholds, or provider bindings in portable procedures.
- Preserve intrinsic modes: an assessment inspects; a change workflow changes within the request. In planning mode, subagents inherit the same read-only boundary.
- Workflows link directly to packaged references with a specific loading condition. Every reference call passes the caller's mode, scope, candidate or environment, constraints, and evidence; name a mode only where it changes behavior. Bundled references need no fallback; keep a concise one only for non-bundled dependencies (sibling workflows, optional external tools). Never fetch or install skills at load time.
- Public files stay portable: no private project context, machine paths, credentials, or personal research inventories; examples are synthetic.

## Decision and completion

The caller owns the requested outcome and convergence. A reference is a bounded procedure and starts no extra review process.

1. Before producing a candidate, define the mode, endpoint, owner, and validation contract. Keep planning proportional: a small reversible task goes straight to implementation, when authorized, with a stated proof; otherwise plan only until the first verifiable step and its proof are clear.
2. The caller assigns the risk tier and proof as [Quality Validation](references/protocols/quality-validation.md) defines, covering applicable perspectives without a fixed agent count. Domain procedures return evidence to that one pool, not new review teams. Validate proposals before dependent writes and read back effects afterward; apply the same protocol when maintaining skills, without recursive pools.
3. Finish when the requested endpoint and required checks hold. Missing required proof is never a pass, and a ready or queued PR is not a completed merge. An assessment may complete with bounded coverage gaps when its contract permits; the uncovered target stays unverified. Evaluate DoD criteria only for the selected mode. Do not reopen a settled decision without material new evidence.

## Future-proof discovery

Retrieve changing package, service, repository, version, and pricing data from authoritative sources at execution time; hardcode no evolving catalogs or versions as scope. Bound discovery to the request and exhaust pagination within it. Reconcile sources, registries, and consumers, deduplicate identities, and distinguish denied access from empty results.

The [default packages](references/capabilities/project-alignment/references/default-packages.md) annex names preferred packages only (no versions, majors, or channel labels); agents query the registry at run time for the newest stable release past the 7-day age gate (`@vllnt/*` exempt). Dated findings are evidence, not future authority. Verify exact versions and compatibility before dependent actions; test additions, removals, partial access, and multiple pages.

## Context and distribution

- The public catalog exposes only workflows and mandatory skills; hosts that scan `.agents/` still discover the local maintainer. Keep the library index out of session startup; preload nothing merely because it is installed.
- Link from workflows to `references/vstack/...` only when relevant, with inline Markdown links (no reference-style definitions or nested parentheses in paths); the bundle assembler follows those links and their local dependencies from canonical `references/` sources.
- Run `python3 scripts/bundle-references.py` after changing canonical sources or workflow links, and commit the generated files; the assembler uses only the Python standard library, and users install complete folders with no build step or extra dependency; maintenance scripts stay independently testable. Copies stay byte-identical, portable, and free of sibling-repository paths or symlinks.
- Subagents receive their bounded task, criteria, current evidence, and needed reference paths, in an isolated context when supported, not the full conversation or catalog.
- A library rename changes links and bundles, not authority or mode. Validate isolated installations; reject stale copies, missing dependencies, loading cycles, and hidden `SKILL.md` files.

## Repository checks

1. Maintain valid flat, single-line string frontmatter: `name` matches the folder and `description` is specific (at least 20 characters). Only the local maintainer adds nested `metadata: { internal: true }` (a YAML block), keeping it out of default Skills CLI discovery.
2. Run `bash scripts/test-validate-frontmatter.sh`, `bash scripts/validate-frontmatter.sh`, `bash scripts/test-pre-commit.sh`, `python3 scripts/test-validate-docs.py`, `python3 scripts/validate-docs.py`, `python3 scripts/test-bundle-references.py`, `python3 scripts/bundle-references.py --check`, and `git diff --check`.
3. Check changed references, catalogs, standalone behavior, and relevant success and failure scenarios; distinguish source simulations from executed consumer tests and actual runtime loading.
4. Update [CHANGELOG.md](CHANGELOG.md) under `Unreleased` for each PR (`scripts/changelog-add.sh`) and record current status in the roadmap. A proposal is not execution or publication authority.

## Delivery

`main` is protected: work on a branch and open a PR, never push directly to `main`. Preserve unrelated work; review public content before upload. Follow [RELEASING.md](RELEASING.md) for separately authorized release preparation and publication; this collection's policy does not transfer to consumer projects.
