# Vstack Skills

Opinionated, portable workflows for building and maintaining projects with **[vllnt packages](https://github.com/vllnt)** and the **[@vllnt npm ecosystem](https://www.npmjs.com/org/vllnt)**. Vstack combines the packages, reusable skills, and engineering methods; each project's rules supply its architecture, environments, and permissions.

## Install

```bash
npx skills add https://github.com/vllnt/skills/tree/main/workflows
npx skills add https://github.com/vllnt/skills/tree/main/capabilities
npx skills add https://github.com/vllnt/skills/tree/main/mandatory
```

Install from these category paths to exclude the repository-local maintainer. Use `--list` to inspect a category before installation.

Alternatively, copy an individual skill folder into your runtime's skill directory. Markdown skills have no build step. Discovery of nested folders and automatic session loading depend on the runtime; verify them in the selected host. Installation alone does not activate the Vstack profile or change global rules.

## Choose an entry point

| Folder | Purpose |
|---|---|
| `workflows/` | User tasks such as Build Project, Plan Issues, Improve UI, and Deliver Issue. |
| `capabilities/` | Internal procedures for discovery, assessment, changes, and verification. |
| `mandatory/` | Lightweight session principles: [Thinking](mandatory/vllnt-thinking-principles/SKILL.md), [Orchestration](mandatory/vllnt-orchestration-principles/SKILL.md), [Collaboration](mandatory/vllnt-collaboration-principles/SKILL.md). |

Configure the runtime's user/project instructions to read installed mandatory entries at session start and after context loss. Their descriptions express the trigger; they do not enforce loading. A standalone workflow remains useful without other skills.

## Build with Vstack

The optional [Vstack profile](references/vstack.md) prefers Next.js for web, Tauri with a compatible Next.js frontend for desktop, Expo/React Native for mobile, Convex for durable backend state, and TypeScript/Effect for CLI or stateless APIs.

1. Select the profile through applicable user/project instructions.
2. Use `build-project` for a new baseline or `improve-project` for staged alignment.
3. Shared alignment discovers relevant `@vllnt` packages, exact versions, stable/canary channels, and consumer compatibility through `capability-stack-packages`.
4. Reuse compatible foundations before custom implementations. Preserve justified project exceptions and validate actual consumer behavior.

Package inventories and versions are discovered at execution time. This collection does not hardcode which packages exist or install unused dependencies.

## Composition

The workflow owns the requested result. Capabilities return evidence that later steps reuse while valid. Useful independent work runs in parallel; another skill call does not automatically trigger another complete review team. Missing optional peers fall back to the underlying procedure.

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

### Internal capabilities

| Skill | Result |
|---|---|
| [capability-agent-tooling-review](capabilities/capability-agent-tooling-review/SKILL.md) | Assess or design a minimal agent-operable control plane with explicit authority, observable outcomes, and safe feedback loops. |
| [capability-ci-optimization](capabilities/capability-ci-optimization/SKILL.md) | Audit and optimize CI duration, reliability, runner cost, affected-job selection, and caching while preserving required checks and trust boundaries. |
| [capability-code-architecture](capabilities/capability-code-architecture/SKILL.md) | Assess architectural friction and recommend smaller modules, clear ownership, traceable dependencies, and behavior-preserving checks. |
| [capability-code-review](capabilities/capability-code-review/SKILL.md) | Assess a candidate diff for evidence-backed security, correctness, reliability, design, performance, cost, and delivery risks without repairing or approving it. |
| [capability-code-test-management](capabilities/capability-code-test-management/SKILL.md) | Create, audit, run, improve, and safely prune tests using real behavior and verified defect detection. |
| [capability-code-tests](capabilities/capability-code-tests/SKILL.md) | Execute candidate-specific local, development, preview, and CI checks and report verified behavior or remaining gaps. |
| [capability-compliance-review](capabilities/capability-compliance-review/SKILL.md) | Audit a website or web app for evidence-backed privacy, accessibility, consumer, and AI-content compliance risks without certifying compliance. |
| [capability-convex-components](capabilities/capability-convex-components/SKILL.md) | Design, implement, and test reusable Convex components with isolated state, typed client APIs, host-owned authorization, safe scheduling, and verified consumer integration. |
| [capability-eslint-configuration](capabilities/capability-eslint-configuration/SKILL.md) | Build, migrate, debug, and verify ESLint flat configs and shared presets, including typed linting, file scope, plugin composition, custom rules, and consumer packaging. |
| [capability-infrastructure-costs](capabilities/capability-infrastructure-costs/SKILL.md) | Model current and projected infrastructure costs from observed usage and verified pricing, compare equivalent options, and expose assumptions, uncertainty, and missing evidence without changing services. |
| [capability-infrastructure-review](capabilities/capability-infrastructure-review/SKILL.md) | Assess infrastructure exposure, access, isolation, dependencies, and recovery from current evidence; return prioritized findings and verification gaps without changing infrastructure. |
| [capability-nextjs-tests](capabilities/capability-nextjs-tests/SKILL.md) | Verify and diagnose Next.js pages, hydration, runtime errors, routing and user flows using repository-native tests and available browser tooling. |
| [capability-project-alignment](capabilities/capability-project-alignment/SKILL.md) | Assess a new or existing project's fit with applicable stack and package preferences; return a verified target, reusable dependencies, and staged changes without modifying the project. |
| [capability-reasoning-assumptions](capabilities/capability-reasoning-assumptions/SKILL.md) | Reduce a real subject to decision-relevant constraints, challenge inherited assumptions, and rebuild an evidence-backed design or decision. |
| [capability-release-changelog](capabilities/capability-release-changelog/SKILL.md) | Maintain accurate user-facing change history and local release notes without publishing a release. |
| [capability-release-readiness](capabilities/capability-release-readiness/SKILL.md) | Assess public-release readiness and repair authorized local documentation, metadata, and workflow gaps. |
| [capability-runtime-performance](capabilities/capability-runtime-performance/SKILL.md) | Profile and improve runtime latency, throughput, memory, I/O, query efficiency, scaling, and infrastructure cost against representative workloads and explicit budgets. |
| [capability-stack-packages](capabilities/capability-stack-packages/SKILL.md) | Discover a stack's accessible source repositories and published packages, verify latest and canary releases, and compare consumer dependencies without installing or maintaining a fixed package list. |
| [capability-typescript-configuration](capabilities/capability-typescript-configuration/SKILL.md) | Design, migrate, and verify TypeScript compiler configurations and shared presets across Node, libraries, React, and Next.js using diagnostic, emit, packaging, and consumer-build tests. |
| [capability-ui-accessibility](capabilities/capability-ui-accessibility/SKILL.md) | Build, review, and repair accessible web interfaces with applicable standards and explicit browser, keyboard, and assistive-technology evidence. |
| [capability-web-performance](capabilities/capability-web-performance/SKILL.md) | Measure and diagnose web performance, distinguish lab results from field Core Web Vitals, and verify authorized optimizations with comparable before-and-after evidence. |
| [capability-workspace-turborepo](capabilities/capability-workspace-turborepo/SKILL.md) | Audit and repair Turborepo and package-workspace boundaries, public exports, task graphs, affected builds, and cache correctness using repository conventions and measured evidence. |

## Maintaining this collection

Use the repository-local [.agents/skills/manage-skill/SKILL.md](.agents/skills/manage-skill/SKILL.md). This maintainer is intentionally public repository tooling, excluded from the installable catalog. Public `manage-skills` provides the portable lifecycle workflow.

See [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md), [roadmap.md](roadmap.md), and [RELEASING.md](RELEASING.md). Keep [CHANGELOG.md](CHANGELOG.md) current.

```bash
bash scripts/test-validate-frontmatter.sh
bash scripts/validate-frontmatter.sh
bash scripts/test-pre-commit.sh
python3 scripts/test-validate-docs.py
python3 scripts/validate-docs.py
git diff --check
```

Structural checks do not prove agent behavior. [Evaluation scenarios](references/skill-evaluations.md) distinguish source simulations, executed checks, consumer behavior, and runtime-loading evidence.

## License

[MIT](LICENSE) © 2026 vllnt
