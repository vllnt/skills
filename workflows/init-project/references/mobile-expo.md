Load this file when the plan includes a mobile surface (Expo / React Native), single app or monorepo.

This file states what the mobile surface must satisfy. Take file contents, configuration keys, and commands from the official Expo documentation and from each package's README and published `exports` for the installed version.

## Commands

Run in the app directory: the root for a single app, or `apps/mobile`.

- Add `expo` by name, without a version: pnpm picks the newest SDK release at least 7 days old.
- Add the router, its peers, React, React Native, and the test packages with `expo install`, which picks the versions that match the SDK. Do not hand-pick them.
- Add `typescript`, `eslint`, `prettier`, `@vllnt/eslint-config`, and `@vllnt/typescript` by name (see [Resolve versions](baseline.md#resolve-versions)).
- With a backend, also add `convex` here. The app imports the backend client itself, and isolated installs do not share a sibling's dependencies.

`expo install` pins the exact versions the SDK bundles, and those can be younger than 7 days. If pnpm refuses them as too young, stop and ask the user: wait for them to mature, or add the named packages to the release-age exclude list with the reason in `AGENTS.md`. Never loosen the release-age gate.

## Files

- Scripts: the [baseline script set](baseline.md#baseline-scripts), plus native run scripts and `check:expo` (Expo's dependency alignment check). `build` is an Expo export. `dev` binds to localhost on the worktree's port; a physical device opts into LAN or a tunnel explicitly, recorded in `AGENTS.md`. In a monorepo, `format`, `format:check` and `verify` live at the root.
- If the TypeScript version that the @vllnt presets' peer range requires differs from the one the SDK expects, exclude `typescript` from Expo's alignment check, record the reason in `AGENTS.md`, and keep the check for every other package.
- In a single app that also holds `convex/`: the mobile test runner ignores `convex/`, the backend tests run under vitest (see [backend tests](backend-convex.md#tests)), `typecheck` covers both tsconfigs, the ESLint config adds the [backend blocks](backend-convex.md#eslint), and the app tsconfig excludes `convex/`.
- `tsconfig.json`: extend the `@vllnt/typescript` Expo preset if the installed version exports one; otherwise extend Expo's base config and then the `@vllnt/typescript` base preset (the later entry wins). Run `pnpm typecheck` and report the real result; if it fails, fix the config without weakening strictness or skipping the check (see [checks 5 and 9](verification.md#checks)).
- `eslint.config.mjs`: spread the `@vllnt/eslint-config` React Native preset if the installed version exports one, otherwise its React preset, ignore Expo's generated files and output, and report unused disable directives as errors.
- App config: name and slug from the project name; `scheme` uses the derived `<app>` id, and the iOS bundle identifier and Android package use the derived store id (see the [questions](questions.md#questions)); automatic light and dark mode; the router plugin with typed routes. Do not reference icon or splash assets that do not exist.
- No Babel or Metro config unless a feature needs one; Expo's defaults cover monorepos. If Metro cannot resolve packages under pnpm's isolated layout, switch pnpm to a hoisted layout and record why in `AGENTS.md`.

### Source files

- `app/_layout.tsx` is a `Stack` root.
- `app/index.tsx` renders `greeting(name)` from `lib/greeting.ts`, a pure function the screen uses, and `lib/greeting.test.ts` tests it with jest.
- `.env.example` holds `EXPO_PUBLIC_CONVEX_URL=` when the backend is selected.
- Optional, on request: Maestro end-to-end flows in `.maestro/`.

## Backend wiring

Apply this section when the plan includes a backend.

- `lib/environment.ts` exports `requireConvexUrl()`, reading `EXPO_PUBLIC_CONVEX_URL` by its literal name, with the same behavior as the [web module](web-nextjs.md#files), and a test asserts that it throws when the variable is unset.
- The root layout creates one backend client at module level and mounts its provider around the navigator. In a monorepo with `packages/client`, the factory comes from there (see [shared packages](layouts.md#shared-packages)).
- With Better Auth selected, the root layout mounts the adapter's auth provider with the Expo auth client instead, as in [Auth](backend-convex.md#auth). Take session initialization from the installed README; never invent it. Client authentication is unverified unless it was exercised.
- Never ship an unmounted provider.

## i18n

Apply this section when i18n is selected.

Use `i18next` with `react-i18next`, plus `expo-localization` (install it with `expo install`). Catalogs live in `i18n/locales/<locale>.json` with the same keys as web.

## Native UI

Apply this section when the UI choice is `@vllnt/ui-native` (experimental). Otherwise use `plain` (React Native styles).

Offer `@vllnt/ui-native` only after an availability check:
- Its registry dist-tags show a real, non-placeholder release.
- The package's published native registry manifest (linked from its README) reports installation as available.

If either check fails, scaffold `plain` and add a "native UI library pending" line to `AGENTS.md`.

When it is available:
- Install it as in [Canary packages](baseline.md#canary-packages) and mount its theme provider at the root, following the system color scheme.
- Satisfy the peers its installed version declares. It needs no Tailwind, NativeWind, Babel or Metro changes.
- Take component names and props from its README and `exports`. Components take React Native styles and accessibility props, not class names.
- Never use `@vllnt/ui` (web) or `@vllnt/analytics` in mobile.

## Deploy

Apply this section when the mobile deploy target is `eas`.

EAS build configuration has development (dev client, internal), preview (internal), and production profiles. It contains no hostnames, keys or project ids. The user links the project with EAS later.
