Load this file at the start of `init-project`, before asking anything.

## Asking

- Infer every answer you can from the request first: "a Next.js site with a Convex backend" answers Q2. Ask only what is still open.
- Ask in two logical stages: Q2 alone when it is unknown, then every other relevant question, grouped by topic. Within a stage, make as many tool calls as the tool's limits require. Ask a dependent follow-up when an answer changes which questions apply. Every question has a default, and the answer "defaults" accepts all of them.
- Ask a question only when earlier answers make it relevant; the [forcing rules](#forcing-rules) skip or force answers.
- Use the harness's structured question tool when it has one, for example `AskUserQuestion` in Claude Code, or the equivalent in Codex or Cursor. Put the default first in each option list and mark it as the default. Respect the tool's limits on questions per call and options per question (Claude Code: up to 4 questions per call, 2 to 4 options each, plus a free-text "Other"). Split a long list into related topic groups, or ask it in chat.
- Without such a tool, ask plain numbered questions in chat, each with its options and default, and accept answers such as `1: my-app, 2: web+backend` or "defaults".
- When the harness cannot ask at all, or the user already gave every answer, use the [non-interactive mode](#non-interactive-mode).
- After the answers, print the plan before writing anything: surfaces, layout, package lines, pinned prereleases, and the files to create (the record used for any cleanup). When the user answered "defaults" or gave every answer up front, the plan is informational; otherwise wait for one confirmation. State that the package manager is pnpm.

## Questions

| # | Question | Options (first = default) | Asked when |
|---|---|---|---|
| Q1 | Project name | free text; default = target directory name | always |
| Q2 | What are you building? (multi-select) | `web` (Next.js App Router), `backend` (Convex), `mobile` (Expo / React Native), `library` (published TypeScript package), `cli` (Node command-line app) | always. Default: `web` + `backend` |
| Q3 | Layout | `single app`, `monorepo` | only when not forced |
| Q4 | Shared packages (multi-select) | `none`, `client` (typed data layer over the backend, shared by apps), `shared` (pure TypeScript types and utils) | monorepo only. Default: `client` when `backend` plus 2 or more of `web`, `mobile`; else `none` |
| Q5 | Auth | `none`, `better-auth` (Better Auth on Convex, anonymous sessions first) | `backend` selected |
| Q6 | UI | web: `@vllnt/ui` (Tailwind 3.4), `tailwind-only` (Tailwind 4), `none`. Mobile: `plain` (React Native styles), `@vllnt/ui-native` (experimental) | per web or mobile surface. Offer `@vllnt/ui-native` only if its [availability check](mobile-expo.md#native-ui) passes |
| Q7 | i18n | `none`, `yes` + locale list (default `en`) | `web` or `mobile` |
| Q8 | Analytics | `none`, `consent` (`@vllnt/analytics` consent gate), `consent+metrics` (adds `@vllnt/convex-analytics`) | `web`. `consent+metrics` needs `backend` |
| Q9 | AI features (multi-select) | `none`, `llms.txt` (`@vllnt/next-llms`), `mcp` (admin MCP endpoint on the backend) | `llms.txt` needs `web`; `mcp` needs `backend` |
| Q10 | Backend features (multi-select) | `none`, plus the [feature bundles](backend-convex.md#feature-bundles) | `backend` |
| Q11 | Deploy target | web: `vercel`, `docker`, `none`. Backend: `convex-cloud`, `self-hosted`. Mobile: `eas`, `none`. Library and CLI: `none`, `npm` | per surface |
| Q12 | Visibility and license | `private` (license `UNLICENSED`), `public` (license `MIT` by default, or `Apache-2.0`) | always |

Validate Q1:

- Lowercase npm name matching `^[a-z0-9][a-z0-9-]{0,213}$`, with no scope.
- Not a reserved word: `node_modules`, `src`, `dist`, `build`, `public`, `test`, `tests`.
- For mobile, derive the store id `com.<owner>.<app>`:
  - `<app>` is the name with every non-alphanumeric character removed, prefixed with `app` when it starts with a digit (`my-app` -> `myapp`, `2048` -> `app2048`).
  - Ask for `<owner>` once; the default is `example`. Validate it against `^[a-z][a-z0-9]*$`, which is valid for both iOS and Android.
  - Every Android segment must match `[A-Za-z][A-Za-z0-9_]*`.
  - Use `<app>`, never the raw name, for the mobile `scheme`: it always starts with a letter.

On an invalid answer, say which rule failed and ask again; never rewrite the answer silently.

## Forcing rules

| Condition | Effect |
|---|---|
| Two or more of `web`, `mobile`, `library`, `cli`; `library` or `cli` together with `backend`; or any shared package | Layout is forced to `monorepo` (Q3 not asked) |
| Only `backend` | Backend-only single app (Q6, Q7, Q8, and Q9 `llms.txt` not asked) |
| Only `library` or only `cli` | Single app (Q4 to Q10 not asked) |
| `better-auth`, `mcp`, `consent+metrics`, any Q10 bundle, or Q4 `client` | Requires `backend`. Add it and say so in the plan |
| `public` | Add `LICENSE`, `SECURITY.md`, and `CONTRIBUTING.md`; set `"license"` in every `package.json` |
| `private` | `"private": true` and `"license": "UNLICENSED"` in every `package.json`; no `LICENSE` file |
| Q11 web = `docker` | `output: "standalone"` and a `Dockerfile` ([web deploy](web-nextjs.md#deploy)) |
| Q11 backend = `self-hosted` | `docker-compose.yml` with pinned image tags and self-hosted env names ([self-hosted backend](backend-convex.md#self-hosted-backend)) |
| Q11 library or CLI = `npm` | Requires `public`. If `private` was chosen, ask the user to change one; never switch visibility silently. Adds a publish workflow ([library and CLI](library-cli.md#publish)) |

When a monorepo has only `backend` and `mobile`, it still uses the [monorepo layout](layouts.md#monorepo).

## Non-interactive mode

Accept a single JSON object and go straight to the plan. Missing keys take the defaults above.

```json
{
  "name": "my-app",
  "surfaces": ["web", "backend"],
  "layout": "single",
  "shared": [],
  "auth": "none",
  "ui": { "web": "@vllnt/ui", "mobile": "plain" },
  "i18n": { "enabled": false, "locales": ["en"] },
  "analytics": "none",
  "ai": [],
  "backendFeatures": [],
  "deploy": { "web": "vercel", "backend": "convex-cloud", "mobile": "eas", "library": "none", "cli": "none" },
  "visibility": "private",
  "license": "UNLICENSED",
  "owner": "example"
}
```

| Key | Allowed values |
|---|---|
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

Reject unknown keys and unknown values with a message that lists the allowed ones. Apply the forcing rules and state each forced change in the plan. Never drop a field or switch a preset silently.

## Not offered

- Page presets such as blog, docs, dashboard, or admin. Add pages after init as ordinary work guided by the generated `AGENTS.md`.
- A package-manager choice or a skip-install option. pnpm only, and install is part of verification.
- A later "add feature" command. Features are init questions; later additions follow `AGENTS.md`.
- Editor-specific rule files or a metadata file. `AGENTS.md` records the choices, and `CLAUDE.md` imports it.
- `@vllnt/convex-mcp`, which is deprecated; the MCP endpoint uses `@vllnt/convex-helpers/mcp`.
