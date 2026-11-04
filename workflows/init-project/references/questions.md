Load before asking anything.

## Asking

- Infer answers from the request. Ask only what is still open.
- Stages: path (Q0) when unknown; then surfaces (Q2) when path is `vstack` and surfaces unknown; then remaining relevant questions. Use dependent follow-ups when an answer changes the set.
- Prefer the harness structured question tool (`AskUserQuestion` or equivalent). Else numbered chat with defaults. Else [non-interactive](#non-interactive-mode).
- Defaults: first option is default; answer `defaults` accepts all open defaults.
- After answers, print the plan (path, surfaces, layout, run location, package manager, resolved packages/prereleases, files). Confirm unless every answer was given or `defaults`.

## Questions

| # | Question | Options (first = default) | Asked when |
|---|---|---|---|
| Q0 | Path | `vstack` (@vllnt Next.js / Convex / Expo / library / CLI), `other` (any other stack; minimal baseline) | when unknown. Infer `vstack` from those surfaces; infer `other` from a named other framework or npm/yarn/bun |
| Q1 | Project name | free text; default = target directory name | always |
| Q2 | Surfaces (multi-select) | `web`, `backend`, `mobile`, `library`, `cli` | `vstack` only. Default: `web` + `backend` |
| Q3 | Layout | `monorepo` (pnpm + Turborepo), `single app` | `vstack`, when not forced |
| Q4 | Shared packages (multi-select) | `none`, `client`, `shared` | `vstack` monorepo. Default: `client` when `backend` plus 2+ of `web`,`mobile`; else `none` |
| Q5 | Auth | `none`, `better-auth` | `vstack` + `backend` |
| Q6 | UI | web: `@vllnt/ui`, `tailwind-only`, `none`. Mobile: `plain`, `@vllnt/ui-native` (if [available](mobile-expo.md#native-ui)) | `vstack` web/mobile |
| Q7 | i18n | `none`, `yes` + locales (default `en`) | `vstack` web/mobile |
| Q8 | Analytics | `none`, `consent`, `consent+metrics` | `vstack` web. `consent+metrics` needs `backend` |
| Q9 | AI (multi-select) | `none`, `llms.txt`, `mcp` | `vstack`. `llms.txt` needs `web`; `mcp` needs `backend` |
| Q10 | Backend features | `none` + [bundles](backend-convex.md#feature-bundles) | `vstack` + `backend` |
| Q11 | Deploy | web: `vercel`,`docker`,`none`. Backend: `convex-cloud`,`self-hosted`. Mobile: `eas`,`none`. Lib/CLI: `none`,`npm` | `vstack` per surface |
| Q12 | Visibility | `private` (`UNLICENSED`), `public` (`MIT` or `Apache-2.0`) | always |
| Q13 | Run location | detected mode first, then `local-only`, `cloud`, `hybrid` | `vstack`. Behavior: [Run location](lifecycle.md#run-location) |
| Q14 | Other stack | free text: framework/runtime + package manager | `other` only. No default — must be stated or asked. Record exactly what the user said |

Q1 rules: lowercase `^[a-z0-9][a-z0-9-]{0,213}$`, no scope; not `node_modules|src|dist|build|public|test|tests`. Mobile store id `com.<owner>.<app>`: ask `<owner>` (default `example`, `^[a-z][a-z0-9]*$`); `<app>` strips non-alphanumerics, prefix `app` if digit-leading; scheme uses `<app>`. Invalid → say which rule failed; never rewrite silently.

## Forcing rules

| Condition | Effect |
|---|---|
| Named Next.js/Convex/Expo/@vllnt library or CLI without a conflicting other stack | Q0 = `vstack` |
| Named other framework, or npm/yarn/bun required | Q0 = `other`; skip Q2–Q13 |
| `vstack` and two or more of `web`,`mobile`,`library`,`cli`; or `library`/`cli` with `backend`; or any shared package | Q3 = `monorepo` |
| `vstack` and only `web` or only `mobile` | Q3 = `single app` |
| `vstack` and only `backend` | single app; skip Q6–Q8 and Q9 `llms.txt` |
| `vstack` and only `library` or only `cli` | single app; skip Q4–Q10 |
| `better-auth`, `mcp`, `consent+metrics`, Q10 bundle, or Q4 `client` | requires `backend` (add and state in plan) |
| `public` | add `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`; set `"license"` in every package manifest |
| `private` | `"private": true` and `"license": "UNLICENSED"` in every package manifest; no `LICENSE` file |
| Q11 web = `docker` | standalone web output + container build ([web deploy](web-nextjs.md#deploy)) |
| Q11 backend = `self-hosted` | compose file with release tags resolved at execution ([self-hosted](backend-convex.md#self-hosted-backend)) |
| Q13 = `local-only` | backend `self-hosted`; web `docker` or `none`; mobile `none`; lib/CLI `none`; no hosted CI/previews/remote cache |
| Q13 = `cloud` or `hybrid` | hosted deploy defaults: `vercel`, `convex-cloud`, `eas` |
| Q11 library or CLI = `npm` | requires `public`; adds publish workflow ([library-cli](library-cli.md#publish)) |

## Non-interactive mode

Accept one object of keys below; missing keys use defaults. `path` required when not inferable. Reject unknown keys/values. Apply forcing rules; state forced changes in the plan.

| Key | Maps to |
|---|---|
| `path` | Q0 |
| `name` | Q1 |
| `surfaces` | Q2 |
| `layout` | Q3 (`single` or `monorepo`) |
| `shared` | Q4 |
| `auth` | Q5 |
| `ui.web` / `ui.mobile` | Q6 |
| `i18n.enabled` / `i18n.locales` | Q7 |
| `analytics` | Q8 |
| `ai` | Q9 |
| `backendFeatures` | Q10 |
| `deploy.*` | Q11 per surface |
| `visibility` / `license` | Q12 |
| `runs` | Q13 |
| `otherStack` | Q14 |
| `owner` | mobile `<owner>` |

## Not offered

- Page presets, package-manager choice (on `vstack`), skip-install, or a later "add feature" command.
- Editor-specific rule files. `AGENTS.md` records choices; `CLAUDE.md` imports it.
- `@vllnt/convex-mcp` (deprecated); MCP uses `@vllnt/convex-helpers/mcp` when selected.
