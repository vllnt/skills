Load this file when the plan includes a web surface (Next.js App Router), single app or monorepo.

This file states what the web surface must satisfy. Take file contents, configuration keys, and API names from the official Next.js documentation and from each package's README and published `exports` for the installed version.

## Packages

Run in the app directory: the root for a single app, or `apps/web`. Add packages by name, without versions, once the supply-chain policy is in place (see [Resolve versions](baseline.md#resolve-versions)):

- Runtime: `next`, `react`, `react-dom`, `@vllnt/logger`.
- Development: `typescript`, `@types/node`, `@types/react`, `@types/react-dom`, `eslint`, `prettier`, `@vllnt/eslint-config`, `@vllnt/typescript`, `vitest`.
- With a backend, also `convex`. Every app that imports the backend client declares `convex` itself, because pnpm's isolated layout does not let an app use a sibling package's dependency.

In a monorepo, take shared versions from `catalog:` (see [Monorepo](layouts.md#monorepo)).

## Files

- Scripts: the [baseline script set](baseline.md#baseline-scripts). `dev` and `start` bind to localhost on the worktree's port (see [Parallel worktrees](lifecycle.md#parallel-worktrees)). In a single app that also holds `convex/`, `typecheck` covers both the web and the backend tsconfig, and `codegen` exists. In a monorepo, `format`, `format:check` and `verify` live only at the root.
- `tsconfig.json` extends the `@vllnt/typescript` Next.js preset (see [TypeScript](baseline.md#typescript)), lists ambient types explicitly, and excludes `convex/` when the backend has its own tsconfig.
- `eslint.config.mjs` spreads the `@vllnt/eslint-config` Next.js preset. It ignores build output, generated declarations, test reports, and config files that no tsconfig covers, because typed linting fails on them. `no-console` is an error, so logging goes through `@vllnt/logger`. When the app holds `convex/`, the [backend ESLint blocks](backend-convex.md#eslint) join the same file.
- The Next.js config transpiles only packages that ship TypeScript source (check the installed package's entry points) and workspace packages, and enables standalone output only for the Docker target.
- The root layout imports the global stylesheet. Providers wrap the children: theme (UI library), then backend client, then auth or analytics where selected.
- Environment: one typed module, `lib/environment.ts`, reads every variable the app needs by its literal name (frameworks inline only direct references) and validates them all at start-up, failing with the name of the first missing or invalid one. `requireConvexUrl()` is its backend URL accessor. Mobile has the same module with `EXPO_PUBLIC_` names.
- Backend client: a client provider builds the backend client from `requireConvexUrl()`.
- Input boundaries: every route handler, server action, and parser of an outside service's response validates its input with a schema before use, and rejects invalid input with a client error. Backend functions already validate through their Convex validators.
- Security headers: every response carries a Content Security Policy, a framing restriction, `nosniff`, and a referrer policy, set in one place as the Next.js documentation describes. The policy allows the backend and any selected vendor origins only.
- Error path: an app-level error page, a global error boundary, and a not-found page exist. Server request errors go through the logging hook below, and client errors through one error-reporting function whose sink is pluggable (logger output now, a monitoring vendor later) without changing call sites.

### Pages, tests and support files

- `app/page.tsx` is a minimal server component that renders the project name. It is the only page; never link to routes that do not exist.
- `app/globals.css` always exists, because the layout imports it; the UI sections set its content.
- `lib/site.ts` holds the site name and an absolute-URL helper that falls back to localhost when the public site URL is empty, not only when it is unset (a copied `.env.example` sets it to an empty string).
- `tests/unit/*.test.ts` covers the URL helper and, with a backend, the environment module's failure path (an unset variable throws, naming it). Unit tests import with relative paths unless the test runner is configured for the tsconfig alias.
- A module declaration for CSS imports exists, because the preset checks side-effect imports.
- `.env.example` lists names only: the public site URL and `LOG_LEVEL`, then one entry per feature that needs one.
- The vitest config includes `tests/unit/**/*.test.ts` with at most 2 workers. When the app also holds `convex/`, use the two-project form from the [backend tests](backend-convex.md#tests).

Meet [Tests](baseline.md#tests).

## Logging

Always apply this section.

- Server request errors are logged through `@vllnt/logger` from the framework's request-error instrumentation hook.
- Log the route template, never the concrete request path: the path can carry tokens or identifiers.
- Never log headers, cookies, tokens, request bodies, or user identity. The logger has no redaction, so log through the allowlisting wrapper from [mandatory primitives](baseline.md#mandatory-primitives).
- `LOG_LEVEL` in the host environment sets verbosity; without it, only warnings and errors print.

## UI library

Apply this section when the UI choice is `@vllnt/ui`.

- Install `@vllnt/ui` and the Tailwind major that its stylesheet and preset are written for, read from its README, stylesheet, and peer metadata. A loose peer range does not prove support for a newer Tailwind major. Fail closed: if the declared peer range excludes the major the stylesheet needs, stop and report.
- Also install every peer and companion package the resolved version declares, such as its theme provider and animation plugin.
- Use the library's stylesheet and Tailwind preset as its README documents. The app stylesheet holds app-only rules and does not repeat what the library stylesheet already contains.
- Tailwind content scanning includes the library's built files under pnpm's symlinked `node_modules`. [Check 11](verification.md#checks) proves it.
- Mount the library's theme provider at the root as its README documents. Add tooltip or toast providers only when the app uses them.
- The library imports Next.js modules, so use it only in Next.js apps.

## Tailwind only

Apply this section when the UI choice is `tailwind-only`: the latest Tailwind with its PostCSS integration, set up as the official Tailwind documentation describes. Never mix this with `@vllnt/ui` in the same app.

## i18n

Apply this section when i18n is selected (`next-intl`).

- Install `next-intl` and set up routing, request config, navigation, and the request proxy as its documentation describes for the installed Next.js version.
- `messages/<locale>.json`: one per locale, all with the same keys.
- Exactly one root layout and one `<html>`: the locale segment's layout replaces the plain root layout, sets `lang` to the locale, returns not-found for unknown locales, and mounts the i18n provider plus the theme, backend, and analytics providers.
- `llms.txt` and other files with a dot in their path stay outside the locale segment and the proxy's matcher.
- Add this rule to the generated `AGENTS.md`: every user-visible string lives in all catalogs.

## Analytics

Apply this section when the analytics choice is `consent` or `consent+metrics` (`@vllnt/analytics`, consent gate).

- The package decides **whether** tracking may run (stored consent plus Do-Not-Track) and queues events. It **sends nothing**: the app wires a vendor SDK, if any, and starts it only when consent allows it.
- Mount its provider in the root layout as its README shows, with a module-level config object, and a consent banner inside the provider that uses the provider's accept and decline actions.
- The banner renders only after mount, so server and client output match.
- Decline and Do-Not-Track keep analytics off. Track events in client code only.
- If the installed version ships TypeScript source, add it to the Next.js transpile list.
- Web only. Never add it to mobile or to packages that mobile consumes.
- `consent+metrics` also mounts `@vllnt/convex-analytics` and `@vllnt/convex-consent` on the backend (see [feature bundles](backend-convex.md#feature-bundles)) for server-side events.

## llms.txt

Apply this section when the AI features include `llms.txt` (`@vllnt/next-llms`).

- Install from [default packages](vstack/capabilities/project-alignment/references/default-packages.md) using [Resolve release](baseline.md#resolve-release). Record any prerelease and reason in the generated `AGENTS.md`.
- Serve `llms.txt` from a static route built with the generator the installed version exports (confirm it in its `exports` and `.d.ts`). The route handler must pass the preset's naming rules.
- Add the markdown catch-all route only if the user has a content source. Its resolver receives the slug of the whole request path, so that resolver is the security boundary.

## End-to-end smoke

Every web app ships a browser smoke test of its production build, under `tests/e2e/*.spec.ts`, run by the `test:e2e` script locally and by the CI job in [End-to-end job](baseline.md#end-to-end-job). One browser, at most 2 workers locally. It is outside the default pre-push gate; CI runs it on every pull request. It asserts that:

- the home page renders the project name;
- an unknown URL shows the not-found page, and a forced render error shows the error page;
- the security headers above are present on the home page;
- an automated accessibility check of the home page reports no critical violations;
- with a backend, the health query answers from a real backend, never the CI placeholder URL: locally the worktree's backend, and in CI a local backend started in the job (the same anonymous local mode codegen uses) or the pull request's preview backend.

The runner is Playwright and the accessibility check is axe through its Playwright integration (`@axe-core/playwright`); take their setup from the official docs.

## Deploy

Apply the requirements for the web deploy target. Take commands and file formats from the host's and Convex's current documentation.

- `vercel` with a backend: the deploy build deploys the backend first, then builds the web app with the deployed backend URL. In a monorepo, the backend deploy runs in the backend package and the build targets the web app. The deploy key lives only in the hosting dashboard, one per environment (production, preview).
- `vercel` without a backend: no host config file unless the build needs one.
- `docker`: standalone output, a multi-stage image on the project's Node version that installs with the frozen lockfile, declares a health check on the health route, and has a `.dockerignore`.
