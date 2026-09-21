# Vstack Skills

Opinionated, portable workflows for building and maintaining projects with **[vllnt packages](https://github.com/vllnt)** and the **[@vllnt npm ecosystem](https://www.npmjs.com/org/vllnt)**. Vstack combines the packages, reusable skills, and engineering methods; each project's rules supply its architecture, environments, and permissions.

## Install

```bash
npx skills add vllnt/skills
```

Use `--list` to inspect the public skills before installation. The repository-local maintainer has `metadata.internal: true`, which excludes it from default Skills CLI discovery; this is not an access restriction. Category URLs ending in `/tree/main/workflows` or `/tree/main/mandatory` remain available for selective discovery. Remote category installation and byte-identical copied bundles have been verified with Skills CLI 1.5.26; automatic runtime loading remains host-specific.

Alternatively, copy an individual skill folder into your runtime's skill directory. Markdown skills have no build step. Discovery of nested folders and automatic session loading depend on the runtime; verify them in the selected host. Installation alone does not activate the Vstack profile or change global rules.

## Host plugin distribution

[Vstack Stack](https://github.com/vllnt/stack) packages these skills for Claude Code, Codex, and Cursor. This repository remains the canonical skill source; the distribution repository owns host manifests, adapters, and pinned generated packages.

Main updates send a notification to Stack. Its updater independently resolves the upstream commit, validates regenerated packages, and merges ordinary updates through protected PRs. Changes to principles, licensing, or packaging-related code stop for separate review. Daily and manual runs provide a fallback for missed notifications. Maintainers can resend from the **Notify Vstack distribution** workflow's manual action on `main`. An unchanged upstream pin is a no-op. A successful notification proves delivery, not a downstream merge; inspect the receiver's run and PR result separately.

Distribution synchronization is separate from marketplace publication and host runtime loading. See Stack's README for installation, compatibility evidence, and activation limits. The Skills CLI installation above remains independent of these host packages.

## Choose an entry point

| Folder | Purpose |
|---|---|
| `workflows/` | User tasks such as Build Project, Plan Issues, Improve UI, and Deliver Issue. |
| `references/` | On-demand procedures and supporting guidance; workflows load only the references relevant to the request. |
| `mandatory/` | Lightweight session principles: [Thinking](mandatory/vllnt-thinking-principles/SKILL.md), [Orchestration](mandatory/vllnt-orchestration-principles/SKILL.md), [Collaboration](mandatory/vllnt-collaboration-principles/SKILL.md). |

Configure the runtime's user/project instructions to read installed mandatory entries at session start and after context loss. Their descriptions express the trigger; they do not enforce loading. A standalone workflow remains useful without other skills.

## Build with Vstack

The optional [Vstack profile](references/vstack.md) prefers Next.js for web, Tauri with a compatible Next.js frontend for desktop, Expo/React Native for mobile, Convex for durable backend state, and TypeScript/Effect for CLI or stateless APIs.

1. Select the profile through applicable user/project instructions.
2. Use `build-project` for a new baseline or `improve-project` for staged alignment.
3. Shared alignment discovers relevant `@vllnt` packages, exact versions, stable/canary channels, and consumer compatibility through [Stack packages](references/capabilities/stack-packages/REFERENCE.md).
4. Reuse compatible foundations before custom implementations. Preserve justified project exceptions and validate actual consumer behavior.

Package inventories and versions are discovered at execution time. This collection does not hardcode which packages exist or install unused dependencies.

## Composition

The workflow owns the requested result. It loads a canonical procedure only when its condition applies, passing mode, scope, candidate, and evidence. Useful independent work runs in parallel; another reference does not automatically trigger another complete review team. Missing optional guidance falls back to the underlying procedure.

Finish at the requested endpoint. A bounded report can finish with explicit gaps; missing required verification cannot become a pass. A blocker returns its cause, options, recommendation, consequences, and next action.

## Available skills

### User workflows

| Skill | Result |
|---|---|
| [build-landing-page](workflows/build-landing-page/SKILL.md) | Draft or review framework-independent landing-page structure and conversion copy for one primary action. |
| [build-project](workflows/build-project/SKILL.md) | Establish and verify a minimal project baseline from applicable stack and package preferences. |
| [build-prototype](workflows/build-prototype/SKILL.md) | Build and iterate a focused local prototype using observed behavior and human product decisions. |
| [deliver-issue](workflows/deliver-issue/SKILL.md) | Deliver a scoped issue through a verified pull request and authorized merge to its target branch. |
| [deliver-pull-request](workflows/deliver-pull-request/SKILL.md) | Review a pull request, coordinate authorized repairs and verification, then merge it when permitted. |
| [explain-subject](workflows/explain-subject/SKILL.md) | Explain a real subject with a simple verified mental model and clear limits. |
| [explore-decisions](workflows/explore-decisions/SKILL.md) | Sharpen an artifact or decision through focused evidence-based questions and concrete alternatives. |
| [improve-code](workflows/improve-code/SKILL.md) | Simplify code and comments while preserving observable contracts and affected consumers. |
| [improve-project](workflows/improve-project/SKILL.md) | Adapt an existing repository to applicable stack preferences through small verified stages. |
| [improve-ui](workflows/improve-ui/SKILL.md) | Improve an interface’s hierarchy, consistency, responsiveness, and accessibility while preserving journeys. |
| [manage-defects](workflows/manage-defects/SKILL.md) | Diagnose a reported failure, isolate its cause, and apply authorized repairs with regression evidence. |
| [manage-issues](workflows/manage-issues/SKILL.md) | Triage GitHub issues into an evidence-backed, atomic, actionable backlog and apply authorized changes. |
| [manage-roadmap](workflows/manage-roadmap/SKILL.md) | Create, maintain, synchronize, or report a traceable roadmap that preserves direction and history. |
| [manage-rules](workflows/manage-rules/SKILL.md) | Manage user, project, and nested instructions while preserving scope, precedence, and effective behavior. |
| [manage-skills](workflows/manage-skills/SKILL.md) | Create, review, update, organize, or retire portable agent skills around a clear outcome and evidence. |
| [manage-vision](workflows/manage-vision/SKILL.md) | Create, update, locate, or audit an evidence-backed project vision anchor and decision test. |
| [plan-issues](workflows/plan-issues/SKILL.md) | Assess a codebase and prepare a source-backed, deduplicated issue backlog for human review. |
| [plan-work](workflows/plan-work/SKILL.md) | Maintain a read-only planning session that returns an actionable plan without local or remote side effects. |
| [review-ui](workflows/review-ui/SKILL.md) | Assess an interface for evidence-backed usability, responsiveness, consistency, and accessibility findings without changing it. |

## On-demand procedures

The 23 canonical procedures are [indexed in `references/`](references/README.md). They are not installable skills. The reference bundler copies the exact transitive closure linked by each workflow into that workflow’s `references/vstack/` directory; consumers do not need a runtime build step.

## Maintaining this collection

Use the repository-local [.agents/skills/manage-skill/SKILL.md](.agents/skills/manage-skill/SKILL.md). This maintainer is intentionally public repository tooling, excluded from the installable catalog. Public `manage-skills` provides the portable lifecycle workflow. Author agent-facing instructions with the [family templates](.agents/skills/manage-skill/references/templates.md); criteria precede procedures, and mandatory skills contain principles only.

See [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md), [roadmap.md](roadmap.md), and [RELEASING.md](RELEASING.md). Keep [CHANGELOG.md](CHANGELOG.md) current.

```bash
python3 scripts/bundle-references.py
bash scripts/test-validate-frontmatter.sh
bash scripts/validate-frontmatter.sh
bash scripts/test-pre-commit.sh
python3 scripts/test-validate-docs.py
python3 scripts/validate-docs.py
python3 scripts/test-bundle-references.py
python3 scripts/bundle-references.py --check
git diff --check
```

Structural checks do not prove agent behavior. [Evaluation scenarios](references/skill-evaluations.md) distinguish source simulations, executed checks, consumer behavior, and runtime-loading evidence.

## License

[MIT](LICENSE) © 2026 vllnt
