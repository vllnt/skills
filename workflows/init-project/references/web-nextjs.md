Load this file when the plan includes a web surface (Next.js App Router), single app or monorepo.

## Commands

Run in the app directory: the root for a single app, or `apps/web`.

```sh
pnpm add next@^16 react@^19 react-dom@^19 @vllnt/logger@^0.1.2
pnpm add -D typescript@~6.0.3 @types/node@^24 @types/react@^19 @types/react-dom@^19 \
  eslint@^9.39.5 prettier@^3 @vllnt/eslint-config@^2.0.0 @vllnt/typescript@^2.0.0 vitest
```

With a backend, also add `convex@^1`. Every app that imports `convex/react` declares `convex` itself, because pnpm's isolated layout does not let an app use a sibling package's dependency.

In a monorepo, take shared versions from `catalog:` (see [pnpm-workspace.yaml](layouts.md#pnpm-workspaceyaml)).

## Files

### package.json

Web part:

```json
{
  "name": "<name>",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "next dev --hostname 127.0.0.1 --port 3000",
    "build": "next build",
    "start": "next start --hostname 127.0.0.1 --port 3000",
    "lint": "eslint --cache --cache-location node_modules/.cache/eslint/ --max-warnings 0 .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "verify": "pnpm format:check && pnpm lint && pnpm typecheck && pnpm test && pnpm build"
  }
}
```

In a single app that also holds `convex/`:
- `typecheck` becomes `tsc --noEmit && tsc --noEmit -p convex/tsconfig.json`, because the web tsconfig excludes `convex`.
- Add `"codegen": "convex dev --once"`.

Compose the scripts from the [baseline script set](baseline.md#baseline-scripts). In a monorepo, `format`, `format:check` and `verify` live only at the root. `test:e2e` exists only with [End-to-end (optional)](#end-to-end-optional).

### tsconfig.json

It must extend the preset:

```json
{
  "extends": "@vllnt/typescript/nextjs.json",
  "compilerOptions": {
    "types": ["node", "react"],
    "paths": { "@/*": ["./*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules", "convex"]
}
```

Notes:
- `base.json` sets `"types": []`, so list ambient types explicitly.
- Do not set `baseUrl`; it was removed in preset v2.
- Exclude `convex` because the backend has its own tsconfig (see [backend files](backend-convex.md#files)).

### eslint.config.mjs

```js
import { nextjs } from "@vllnt/eslint-config/nextjs";

export default [
  {
    ignores: [
      ".next/**",
      "coverage/**",
      "next-env.d.ts",
      "node_modules/**",
      "out/**",
      "playwright-report/**",
      "test-results/**",
      "*.config.{js,mjs,cjs,ts}",
    ],
  },
  ...nextjs,
  { rules: { "no-console": "error" } },
];
```

Notes:
- The `ignores` block is required. Typed linting fails on config files and generated `.d.ts` that no tsconfig covers.
- The `no-console` override routes logging through `@vllnt/logger`.
- When the app holds `convex/` (single app with backend), add the [backend ESLint blocks](backend-convex.md#eslint) to this same file.

### next.config.ts

```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {};

export default nextConfig;
```

Add to it as the features below require:
- `transpilePackages`: only for packages that ship TypeScript source, such as `@vllnt/analytics@0.1.x` and workspace packages.
- `output`: only for the Docker target.
- The i18n plugin wrapper.

### app/layout.tsx

This version has no UI library and no i18n. The other features wrap `children`.

```tsx
import "./globals.css";

import type { ReactNode } from "react";

export default function RootLayout({ children }: { readonly children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

### Backend client

With a backend, write `app/convex-client-provider.tsx`. With i18n, `app/[locale]/` holds the layout that mounts it.

```tsx
"use client";

import { ConvexProvider, ConvexReactClient } from "convex/react";
import type { ReactNode } from "react";

import { requireConvexUrl } from "@/lib/environment";

const client = new ConvexReactClient(requireConvexUrl());

export function ConvexClientProvider({ children }: { readonly children: ReactNode }) {
  return <ConvexProvider client={client}>{children}</ConvexProvider>;
}
```

The root layout renders `<body><ConvexClientProvider>{children}</ConvexClientProvider></body>`. With `@vllnt/ui`, `ThemeProvider` wraps it. With `better-auth`, swap in the auth provider (see [backend auth](backend-convex.md#auth)).

Write `lib/environment.ts`:

```ts
const convexUrl = process.env.NEXT_PUBLIC_CONVEX_URL;

export function requireConvexUrl(): string {
  if (!convexUrl) {
    throw new Error("NEXT_PUBLIC_CONVEX_URL is not set");
  }
  return convexUrl;
}
```

Read the variable by its literal name so Next.js can inline it. Mobile has the same file with `EXPO_PUBLIC_CONVEX_URL`.

### Pages, tests and support files

- `app/page.tsx` is a minimal server component that renders the project name. It is the only page. Do not link to routes that do not exist.
- `app/globals.css` always exists, because the layout imports it. With UI choice `none` it holds one minimal rule such as `body { margin: 0; }`. The UI sections below set its content otherwise.
- `lib/site.ts` holds a `siteName` constant and `absoluteUrl(path)`, which returns `new URL(path, process.env.NEXT_PUBLIC_SITE_URL || "http://localhost:3000").toString()`. Use `||`, not `??`: a copied `.env.example` sets the variable to an empty string, and `new URL` throws on an empty base.
- `tests/unit/site.test.ts` tests `absoluteUrl` with one passing vitest test, so `pnpm test` is green on day one.
- Unit tests import with relative paths (`../../lib/site`). Vitest does not read the tsconfig `paths`, so an `@/` import fails there.
- `css.d.ts` contains `declare module "*.css";`. It is needed because `@vllnt/typescript` enables `noUncheckedSideEffectImports`.
- `.env.example` lists names only, with no values. Start with `NEXT_PUBLIC_SITE_URL=` and `LOG_LEVEL=`, then add one entry per feature that needs one.

`vitest.config.ts`:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["tests/unit/**/*.test.{ts,tsx}"],
    maxWorkers: 2,
  },
});
```

When the app also holds `convex/`, use the two-project form from the [backend tests](backend-convex.md#tests).

With a backend, add `tests/unit/environment.test.ts` for the failure path of `requireConvexUrl`. The module reads the variable when it loads, so the test stubs it and imports inside the test:

```ts
import { afterEach, expect, test, vi } from "vitest";

afterEach(() => {
  vi.unstubAllEnvs();
  vi.resetModules();
});

test("requireConvexUrl throws when the variable is unset", async () => {
  vi.stubEnv("NEXT_PUBLIC_CONVEX_URL", "");
  const { requireConvexUrl } = await import("../../lib/environment");
  expect(() => requireConvexUrl()).toThrow("NEXT_PUBLIC_CONVEX_URL is not set");
});
```

## Logging

Always apply this section.

Write `instrumentation.ts` at the app root:

```ts
import type { Instrumentation } from "next";

import { createBackendLogger } from "@vllnt/logger";

const logger = createBackendLogger("next");

export const onRequestError: Instrumentation.onRequestError = (error, request, context) => {
  logger.error("request_error", {
    errorName: error instanceof Error ? error.name : "unknown",
    method: request.method,
    routePath: context.routePath,
    routeType: context.routeType,
  });
};
```

Rules:
- Never log headers, cookies, tokens, request bodies or user identity. The logger has no redaction.
- Log `context.routePath`, never `request.path`. `routePath` is the route template; the request path is the concrete URL, which can carry tokens or identifiers.
- Set `LOG_LEVEL` (`debug|info|warn|error`) in the host environment. Without it, only `warn` and `error` print.

`@vllnt/logger` exports:
- `.`: `createBackendLogger`, `createLogger`, `createExtendedLogger`, `composeOutputs`, `consoleOutput`, `formatLogEntry`, `parseLogLevel`, plus types `Logger`, `LogLevel`, `LogData`, `LogEntry`, `LogOutput`, `LoggerConfig`, `ExtendedLogger`.
- `./convex`: `createConvexLogger(scope, level = "info")`.
- `./testing`: `createTestOutput()`.
- `./posthog`: `createPostHogOutput(capture)`.

## UI library

Apply this section when the UI choice is `@vllnt/ui` (Tailwind 3.4).

`@vllnt/ui` needs Tailwind 3.4, not 4. Its stylesheet uses `@tailwind` directives and its preset is a v3 JS config. The 0.3.0 peer metadata (`>=3.0.0`) is loose: it lets Tailwind 4 install, but the CSS would not work. So always install Tailwind `^3.4.19`.

Fail closed only if `peerDependencies.tailwindcss` of the resolved `@vllnt/ui` version excludes 3.4. Then stop and report instead of continuing. Treat Tailwind 4 support as real only when the package README or CHANGELOG says so. Until then, this section stands.

```sh
pnpm add @vllnt/ui@^0.3.0 next-themes@^0.4 tailwindcss@^3.4.19 tailwindcss-animate@^1
pnpm add -D postcss autoprefixer
```

`tailwindcss-animate` is needed explicitly on 0.3.x. From 0.4.0 it becomes a dependency of `@vllnt/ui`, and `next-themes` becomes a required peer.

`postcss.config.mjs`:

```js
const config = { plugins: { tailwindcss: {}, autoprefixer: {} } };

export default config;
```

`tailwind.config.ts`:

```ts
import type { Config } from "tailwindcss";

import uiPreset from "@vllnt/ui/tailwind-preset";

const config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./node_modules/@vllnt/ui/dist/**/*.js",
  ],
  presets: [uiPreset],
} satisfies Config;

export default config;
```

Tailwind 3 ignores a preset's `content` once the app sets its own, so the `node_modules/@vllnt/ui/dist` glob is required.

`app/layout.tsx` adds:

```tsx
import "@vllnt/ui/styles.css";
import "./globals.css";

import { ThemeProvider } from "@vllnt/ui";
```

The layout wraps `children` in `<ThemeProvider attribute="class" defaultTheme="system" enableSystem disableTransitionOnChange>` and puts `suppressHydrationWarning` on `<html>`. Add `TooltipProvider` and `<Toaster />` only when a tooltip or toast is used.

Rules for this setup:
- `app/globals.css` holds app-only rules. Do not repeat `@tailwind` directives, because `styles.css` already contains them.
- `@vllnt/ui` public entry points:
  - `.` exports components, `ThemeProvider`, `ThemePresetProvider`, `TooltipProvider`, `SidebarProvider`, `Toaster` and `toast`, `cn`, and hooks such as `useMounted` and `useDebounce`.
  - `./tailwind-preset` (default export).
  - `./styles.css`.
  - `./themes/default.css`.
  - `./themes/presets.css`, needed only with `ThemePresetProvider`.
- The npm package ships compiled ESM, so it does not need `transpilePackages`.
- The package imports `next/link`, `next/image` and `next/navigation` at module level. Use it only in Next.js apps.

Verification hook: [check 11](verification.md#checks) greps the built CSS for a class that only the library uses (for example `bg-primary`). This proves the content glob works under pnpm's symlinked `node_modules`.

## Tailwind only

Apply this section when the UI choice is `tailwind-only` (Tailwind 4).

```sh
pnpm add -D tailwindcss@^4 @tailwindcss/postcss
```

`postcss.config.mjs` is `{ plugins: { "@tailwindcss/postcss": {} } }`, and `app/globals.css` is `@import "tailwindcss";`.

Never mix this with `@vllnt/ui` in the same app.

## i18n

Apply this section when i18n is selected (`next-intl`).

```sh
pnpm add next-intl@^4
```

Files:
- `i18n/routing.ts`: `defineRouting({ defaultLocale: "<first>", localePrefix: "as-needed", locales: [...] })`.
- `i18n/request.ts`: `getRequestConfig`, loading `../messages/${locale}.json`.
- `i18n/navigation.ts`: `createNavigation(routing)`.
- `messages/<locale>.json`: one per locale, all with the same keys.
- `app/[locale]/layout.tsx` **replaces** `app/layout.tsx` as the only root layout, so there is exactly one `<html>`:
  - It owns `<html lang={locale}>` and the `globals.css` and `styles.css` imports.
  - It calls `notFound()` for unknown locales.
  - It wraps content in `NextIntlClientProvider`, plus the theme, backend and analytics providers.
- `app/[locale]/page.tsx` **replaces** `app/page.tsx`. With i18n, neither `app/layout.tsx` nor `app/page.tsx` exists.
- `app/llms.txt/` (see [llms.txt](#llmstxt)) stays outside `[locale]`. `proxy.ts` skips it because its path contains a dot.
- `proxy.ts` at the app root. Next 16 names this file `proxy.ts`, not `middleware.ts`.

```ts
import createMiddleware from "next-intl/middleware";

import { routing } from "./i18n/routing";

export default createMiddleware(routing);

export const config = { matcher: "/((?!api|_next|.*\\..*).*)" };
```

Wrap `next.config.ts` with `createNextIntlPlugin("./i18n/request.ts")`. In vitest, set `server.deps.inline: ["next-intl"]` if a test imports it.

Add this rule to the generated `AGENTS.md`: every user-visible string lives in all catalogs.

## Analytics

Apply this section when the analytics choice is `consent` or `consent+metrics` (`@vllnt/analytics`, consent gate).

What the package does:
- It decides **whether** tracking may run (stored consent plus Do-Not-Track) and queues events.
- It **sends nothing**. Its `sendEvent` is a no-op. The app wires a vendor SDK, if any, and starts it only when consent allows it.

Setup:
- `pnpm add @vllnt/analytics@^0.1.1`, and add `"@vllnt/analytics"` to `transpilePackages` while on 0.1.x.
- `app/analytics-provider.tsx` (`"use client"`) renders `<AnalyticsProvider config={ANALYTICS_CONFIG}>` from `@vllnt/analytics/react`. Keep `ANALYTICS_CONFIG = { app: "<name>", version: 1 }` at module level, because the provider's effect depends on the object's identity.
- Mount in the root layout (`app/[locale]/layout.tsx` with i18n), as the package README shows for the provider. The layout wraps `children` in the `app/analytics-provider.tsx` component, which renders the banner inside `AnalyticsProvider` so that `useAnalytics()` has its context.
- `components/consent-banner.tsx` (`"use client"`):
  - Take `acceptAll`, `declineAnalytics` and `hasResponded` from **`useAnalytics()`**. Do not use `useConsent()`: inside the provider it saves consent but never enables tracking.
  - Gate rendering on a `useSyncExternalStore` mount check (server snapshot `false`). `isLoading` is always `false`, so it cannot prevent a hydration mismatch.
  - With `@vllnt/ui`, the banner may use its `CookieConsent` component.
- Decline and Do-Not-Track keep analytics off: after `declineAnalytics()`, or with Do-Not-Track set, `isAnalyticsEnabled()` is `false`.
- Events: `track` and `trackPage` from `@vllnt/analytics`, in client code only.
- Exports:
  - `.`: `initAnalytics`, `track`, `trackPage`, `identify`, `enableAnalytics`, `disableAnalytics`, `isAnalyticsEnabled`, `getAnalyticsState`, `resetAnalytics`, `loadConsent`, `saveConsent`, `clearConsent`, `getConsentFromCookie`, `isDoNotTrackEnabled`, `isValidConsentState`, `CONSENT_STORAGE_KEY`, `CONSENT_COOKIE_NAME`, `CONSENT_VERSION`, and others.
  - `./react`: `AnalyticsProvider`, `useAnalytics`, `useConsent`.
- Web only. Never add it to mobile or to packages that mobile consumes.

`consent+metrics` additionally mounts `@vllnt/convex-analytics` and `@vllnt/convex-consent` on the backend (see [feature bundles](backend-convex.md#feature-bundles)). Server-side events then use `AnalyticsClient.track(ctx, ...)`.

## llms.txt

Apply this section when the AI features include `llms.txt` (`@vllnt/next-llms`).

The package has no stable release, so it is canary-only. Pin the annex version (see [Canary packages](baseline.md#canary-packages)):
1. Install that exact version with no caret. Never use the `latest` tag: it points at an older canary without input hardening.
2. Confirm the exports below in that version (`npm view @vllnt/next-llms@<pin> exports --json`, then its `.d.ts`).
3. State the pin in the plan, and record the pin and the reason in the generated `AGENTS.md`.

Then write `app/llms.txt/route.ts`:

```ts
import { generateLlmsText } from "@vllnt/next-llms";

export const dynamic = "force-static";

export const GET = (): Response => {
  const body = generateLlmsText({
    sections: [{ links: [{ title: "Home", url: "/" }], title: "Pages" }],
    summary: "<one-line summary>",
    title: "<name>",
  });
  return new Response(`${body}\n`, { headers: { "Content-Type": "text/plain; charset=utf-8" } });
};
```

Use an arrow `const`, not `function GET`. The preset's naming exception for route handlers covers only `app/api/**`, so a function declaration named `GET` here fails `naming-convention`.

Exports on the current canary:
- Functions: `generateLlmsText(config)` and `createMarkdownRoute(resolver, options?)`.
- Types: `LlmsConfig`, `LlmsLink`, `LlmsSection`, `MarkdownResolver`, `MarkdownRouteOptions`.

Do not use `generateLlmsFullText`; it exists only in the old canary. Add the markdown catch-all route only if the user has a content source. Its resolver receives the slug of the whole request path, and that resolver is the security boundary.

## End-to-end (optional)

Apply this section only when the plan includes end-to-end tests. Add all of it or none, so no script or file points at something missing:
- `pnpm add -D @playwright/test`.
- The script `"test:e2e": "playwright test"` in `package.json`.
- `playwright.config.ts` and `tests/e2e/home.spec.ts`, as set out in [End-to-end job](baseline.md#end-to-end-job), which also owns the CI `e2e` job.

## Deploy

Apply the block that matches the web deploy target.

### vercel with a backend

- Single app: `package.json` gets `"build:deploy": "convex deploy --cmd 'pnpm build' --cmd-url-env-var-name NEXT_PUBLIC_CONVEX_URL"`.
- Monorepo: `convex deploy` must run in the backend package, and the build command must target the web app. In `apps/web/package.json`: `"build:deploy": "pnpm --dir ../../packages/backend exec convex deploy --cmd 'pnpm --dir ../../apps/web build' --cmd-url-env-var-name NEXT_PUBLIC_CONVEX_URL"`. The hosting project's root directory is `apps/web`.
- `vercel.json` (next to the web app's `package.json`) is `{ "buildCommand": "pnpm build:deploy", "installCommand": "pnpm install --frozen-lockfile" }`.
- `CONVEX_DEPLOY_KEY` is set in the hosting dashboard, never in files: production key for production, preview key for previews.

### vercel without a backend

No `vercel.json` is needed.

### docker

- `next.config.ts` gets `output: process.env.VERCEL ? undefined : "standalone"`.
- Add a multi-stage `Dockerfile` on the pinned Node major: `corepack enable`, `pnpm install --frozen-lockfile`, `pnpm build`, then copy `.next/standalone`, `.next/static` and `public`.
- Add a `.dockerignore`.
