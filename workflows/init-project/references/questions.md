Load this file at the start of `init-project`, before asking anything.

## Asking

- Infer every answer you can from the request first: "a Next.js site with a Convex backend" answers Q0 (`vstack`) and Q2. A named other framework answers Q0 (`other`). Fill every other answer with its default; the answer "defaults" accepts all of them. Q14 has no default.
- Ask only a question with no safe default or an irreversible answer: Q14 when the request does not state it, the npm package name for a published library or CLI when the request does not state it, a conflict only the user can resolve (such as Q11 `npm` with `private`), or a path that writes outside the target. Ask once, in one batch, each with a recommended answer. Ask a dependent follow-up only when an answer changes which questions apply; the [forcing rules](#forcing-rules) skip or force the rest. For `other`, skip Q2–Q13.
- Use the harness's structured question tool when it has one, for example `AskUserQuestion` in Claude Code, or the equivalent in Codex or Cursor. Put the recommended default first in each option list and mark it. Respect the tool's current limits on questions per call and options per question; split the one batch across calls only as the limits require, or ask it in chat.
- Without such a tool, ask plain numbered questions in chat, each with its options and recommended default, and accept answers such as `0: vstack, 1: my-app, 2: web+backend` or "defaults".
- When the harness cannot ask at all, or the user already gave every answer, use the [non-interactive mode](#non-interactive-mode).
- After the answers, print the plan before writing anything: path, surfaces, layout, run location, package manager, packages (latest releases, resolved at install), any prereleases, the lifecycle scripts, and the files to create (the record used for any cleanup), with each inferred or default answer marked so the user can correct it. When the user answered "defaults" or gave every answer up front, the plan is informational; otherwise wait for one confirmation, with defaults filled in. On `vstack`, state that the package manager is pnpm. On `other`, state the package manager recorded from Q14.

## Questions

| # | Question | Options (first = default) | Relevant when |
|---|---|---|---|
| Q0 | Path | `vstack` (@vllnt Next.js / Convex / Expo / library / CLI), `other` (any other stack; minimal baseline) | when unknown. Infer `vstack` from those surfaces; infer `other` from a named other framework or npm/yarn/bun |
| Q1 | Project name | free text; default = target directory name | always |
| Q2 | What are you building? (multi-select) | `web` (Next.js App Router), `backend` (Convex), `mobile` (Expo / React Native), `library` (published TypeScript package), `cli` (Node command-line app) | `vstack` only. Default: `web` + `backend` |
| Q3 | Layout | `single app`, `monorepo` | `vstack`, only when not forced |
| Q4 | Shared packages (multi-select) | `none`, `client` (typed data layer over the backend, shared by apps), `shared` (pure TypeScript types and utils) | `vstack` monorepo only. Default: `client` when `backend` plus 2 or more of `web`, `mobile`; else `none` |
| Q5 | Auth | `none`, `better-auth` (Better Auth on Convex, anonymous sessions first) | `vstack` and `backend` selected |
| Q6 | UI | web: `@vllnt/ui` (component library with its own Tailwind setup), `tailwind-only` (Tailwind, no component library), `none`. Mobile: `plain` (React Native styles), `@vllnt/ui-native` (experimental) | `vstack`, per web or mobile surface. Offer `@vllnt/ui-native` only if its [availability check](mobile-expo.md#native-ui) passes |
| Q7 | i18n | `none`, `yes` + locale list (default `en`) | `vstack` and `web` or `mobile` |
| Q8 | Analytics | `none`, `consent` (`@vllnt/analytics` consent gate), `consent+metrics` (adds `@vllnt/convex-analytics`) | `vstack` and `web`. `consent+metrics` needs `backend` |
| Q9 | AI features (multi-select) | `none`, `llms.txt` (`@vllnt/next-llms`), `mcp` (admin MCP endpoint on the backend) | `vstack`. `llms.txt` needs `web`; `mcp` needs `backend` |
| Q10 | Backend features (multi-select) | `none`, plus the [feature bundles](backend-convex.md#feature-bundles) | `vstack` and `backend` |
| Q11 | Deploy target | web: `vercel`, `docker`, `none`. Backend: `convex-cloud`, `self-hosted`. Mobile: `eas`, `none`. Library and CLI: `none`, `npm` | `vstack`, per surface |
| Q12 | Visibility and license | `private` (license `UNLICENSED`), `public` (license `MIT` by default, or `Apache-2.0`) | `vstack` |
| Q13 | Where does it run? | the detected mode first, then the others: `local-only` (everything on this machine), `cloud` (hosted CI, previews, deploys), `hybrid` (local development, hosted CI, previews, deploys) | `vstack`. Detection and per-mode behavior: [Run location](lifecycle.md#run-location) |
| Q14 | Other stack | free text: framework or runtime, plus package manager | `other` only. No default — must be stated or asked. Record exactly what the user said |

Validate Q1:

- Lowercase npm name matching `^[a-z0-9][a-z0-9-]{0,213}$`, with no scope.
- Not a reserved word: `node_modules`, `src`, `dist`, `build`, `public`, `test`, `tests`.
- For mobile, derive the store id `com.<owner>.<app>`:
  - `<app>` is the name with every non-alphanumeric character removed, prefixed with `app` when it starts with a digit (`my-app` -> `myapp`, `2048` -> `app2048`).
  - Take `<owner>` from the request; otherwise use the default `example` and note in the plan, the generated `AGENTS.md`, and the report's remaining work that it must change before store publishing. Validate it against `^[a-z][a-z0-9]*$`, which is valid for both iOS and Android.
  - Every Android segment must match `[A-Za-z][A-Za-z0-9_]*`.
  - Use `<app>`, never the raw name, for the mobile `scheme`: it always starts with a letter.

On an invalid answer, say which rule failed and ask again; never rewrite the answer silently.

## Forcing rules

| Condition | Effect |
|---|---|
| Named Next.js, Convex, Expo, or an @vllnt library or CLI, without a conflicting other stack | Q0 = `vstack` |
| Named other framework, or npm, yarn, or bun required | Q0 = `other`; skip Q2–Q13; ask Q14 |
| `vstack` and two or more of `web`, `mobile`, `library`, `cli`; `library` or `cli` together with `backend`; or any shared package | Layout is forced to `monorepo` (Q3 not asked) |
| `vstack` and only `web` or only `mobile` | Q3 = `single app` |
| `vstack` and only `backend` | Backend-only single app (Q6, Q7, Q8, and Q9 `llms.txt` not asked) |
| `vstack` and only `library` or only `cli` | Single app (Q4 to Q10 not asked) |
| `better-auth`, `mcp`, `consent+metrics`, any Q10 bundle, or Q4 `client` | Requires `backend`. Add it and say so in the plan |
| `public` | Add `LICENSE`, `SECURITY.md`, and `CONTRIBUTING.md`; set `"license"` in every `package.json` |
| `private` | `"private": true` and `"license": "UNLICENSED"` in every `package.json`; no `LICENSE` file |
| Q11 web = `docker` | Standalone output and a container build ([web deploy](web-nextjs.md#deploy)) |
| Q11 backend = `self-hosted` | `docker-compose.yml` with resolved release image tags and self-hosted env names ([self-hosted backend](backend-convex.md#self-hosted-backend)) |
| Q13 = `local-only` | Q11 backend is `self-hosted`, web is `docker` or `none`, mobile is `none`, and library or CLI is `none`. No hosted CI, previews, or remote cache ([run location](lifecycle.md#run-location)) |
| Q13 = `cloud` or `hybrid` | Q11 defaults to the hosted targets: `vercel`, `convex-cloud`, `eas` |
| Q11 library or CLI = `npm` | Requires `public`. If `private` was chosen, ask the user to change one; never switch visibility silently. Adds a publish workflow ([library and CLI](library-cli.md#publish)) |

When a monorepo has only `backend` and `mobile`, it still uses the [monorepo layout](layouts.md#monorepo).

## Non-interactive mode

Accept one object of the keys below; go straight to the plan. Missing keys use defaults. `path` required when not inferable. For `path: "other"`, set `otherStack` and omit or null vstack-only keys.

| Key | Allowed values |
|---|---|
| `path` | `vstack`, `other` |
| `name` | the Q1 rules |
| `surfaces` | any of `web`, `backend`, `mobile`, `library`, `cli` |
| `layout` | `single`, `monorepo` |
| `shared` | any of `client`, `shared` |
| `auth` | `none`, `better-auth` |
| `ui.web` | `@vllnt/ui`, `tailwind-only`, `none` |
| `ui.mobile` | `plain`, `@vllnt/ui-native` |
| `i18n.enabled` | `true`, `false` |
| `i18n.locales` | non-empty list of locale codes; default `["en"]` |
| `analytics` | `none`, `consent`, `consent+metrics` |
| `ai` | any of `llms.txt`, `mcp` |
| `backendFeatures` | package names from the [feature bundles](backend-convex.md#feature-bundles) |
| `deploy.web` | `vercel`, `docker`, `none` |
| `deploy.backend` | `convex-cloud`, `self-hosted` |
| `deploy.mobile` | `eas`, `none` |
| `deploy.library` | `none`, `npm` |
| `deploy.cli` | `none`, `npm` |
| `visibility` | `private`, `public` |
| `license` | `UNLICENSED` when `private`; `MIT` or `Apache-2.0` when `public` |
| `owner` | the Q1 `<owner>` rule; used only for the mobile store id |
| `runs` | `local-only`, `cloud`, `hybrid`; default: the detected mode |
| `otherStack` | for `other`: `{ "stack": "<framework>", "packageManager": "<pm>" }`; otherwise `null` or omitted |

Reject unknown keys and unknown values with a message that lists the allowed ones. Apply the forcing rules and state each forced change in the plan. Never drop a field or switch a preset silently.

## Not offered

- Page presets such as blog, docs, dashboard, or admin. Add pages after init as ordinary work guided by the generated `AGENTS.md`.
- A package-manager choice or a skip-install option on `vstack`. pnpm only, and install is part of verification. On `other`, the package manager is Q14, recorded in the plan.
- A later "add feature" command. Features are init questions; later additions follow `AGENTS.md`.
- Editor-specific rule files or a metadata file. `AGENTS.md` records the choices, and `CLAUDE.md` imports it.
- `@vllnt/convex-mcp`, which is deprecated; the MCP endpoint uses `@vllnt/convex-helpers/mcp`.
