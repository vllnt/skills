Load this file when the plan includes a mobile surface (Expo / React Native), single app or monorepo.

## Commands

Run in the app directory: the root for a single app, or `apps/mobile`.

```sh
pnpm add expo@^<latest stable SDK major>
pnpm exec expo install expo-router expo-linking expo-constants expo-status-bar \
  react-native-safe-area-context react-native-screens react react-native
pnpm exec expo install --dev jest jest-expo @types/jest @types/react
pnpm add -D typescript@~6.0.3 eslint@^9.39.5 prettier@^3 \
  @vllnt/eslint-config@^2.0.0 @vllnt/typescript@^2.0.0
```

The SDK major for `expo@^<major>` is the newest major whose release is at least 7 days old.

`expo install` picks the versions that match the SDK, including the test packages and React types. Do not hand-pick them.

`expo install` pins the exact versions the SDK bundles, and those can be younger than 7 days. If pnpm fails with `ERR_PNPM_NO_MATURE_MATCHING_VERSION` for them, stop and ask the user: wait for them to mature, or add the named packages to `minimumReleaseAgeExclude` with the reason in `AGENTS.md`. Never loosen `minimumReleaseAge`.

With a backend, also run `pnpm add convex@^1` here. The app imports `convex/react` itself, and isolated installs do not share a sibling's dependencies.

## Files

### package.json

```json
{
  "name": "<name or @<name>/mobile>",
  "main": "expo-router/entry",
  "private": true,
  "scripts": {
    "dev": "expo start --localhost",
    "android": "expo run:android",
    "ios": "expo run:ios",
    "lint": "eslint --cache --cache-location node_modules/.cache/eslint/ --max-warnings 0 .",
    "typecheck": "tsc --noEmit",
    "test": "jest --maxWorkers=2",
    "check:expo": "expo install --check",
    "build": "expo export --platform android --output-dir dist",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "verify": "pnpm format:check && pnpm lint && pnpm typecheck && pnpm test && pnpm check:expo && pnpm build"
  },
  "jest": { "preset": "jest-expo", "testPathIgnorePatterns": ["/node_modules/", "/convex/"] },
  "expo": { "install": { "exclude": ["typescript"] } }
}
```

Notes on this manifest:
- The `expo.install.exclude` entry stops `expo install --check` from fighting the TypeScript 6 pin. It lists nothing else, so the check also covers the React types.
- `dev` binds to localhost. Testing on a physical device opts into `--lan` or a tunnel explicitly; record the opt-in in `AGENTS.md`.
- In a monorepo, drop `format`, `format:check` and `verify`. They live at the root.
- In a single app that also holds `convex/` (mobile + backend):
  - Jest ignores `convex/`, and the backend tests run under vitest with the backend-only config from the [backend tests](backend-convex.md#tests).
  - `test` becomes `jest --maxWorkers=2 && vitest run`.
  - `typecheck` becomes `tsc --noEmit && tsc --noEmit -p convex/tsconfig.json`.
  - The ESLint config adds the Convex blocks from the [backend ESLint rules](backend-convex.md#eslint).
  - The app tsconfig `exclude`s `convex`.

### tsconfig.json

`@vllnt/typescript` has no Expo preset, so compose one. Order matters: the later entry wins.

```json
{
  "extends": ["expo/tsconfig.base", "@vllnt/typescript/base.json"],
  "compilerOptions": {
    "types": ["jest"],
    "paths": { "@/*": ["./*"] }
  },
  "include": ["**/*.ts", "**/*.tsx", ".expo/types/**/*.ts", "expo-env.d.ts"]
}
```

Do not set `baseUrl`.

Unverified: this composition passes `tsc --showConfig`; a full Expo project typecheck has not been run against it. Run `pnpm typecheck` in the mobile app and report the real result. If it fails, fix the config. Never weaken strictness to make it pass, and never skip the check. See [check 5](verification.md#checks) for the config check and [check 9](verification.md#checks) for the typecheck.

### eslint.config.mjs

There is no React Native preset yet, so use `react`:

```js
import { react } from "@vllnt/eslint-config/react";

export default [
  { ignores: [".expo/**", "dist/**", "expo-env.d.ts", "node_modules/**", "*.config.{js,mjs,cjs,ts}"] },
  ...react,
  { linterOptions: { reportUnusedDisableDirectives: "error" } },
];
```

### app.json

- `name` and `slug` come from the project name. `scheme` uses the derived `<app>` id (see the [questions](questions.md#questions)), which always starts with a letter, not the raw name.
- `ios.bundleIdentifier` and `android.package` use the derived store id (see the [questions](questions.md#questions)).
- Set `userInterfaceStyle: "automatic"`, `plugins: ["expo-router"]` and `experiments.typedRoutes: true`.
- Do not reference icon or splash assets that do not exist. Add those fields only when the assets are added.

### Source files

- `app/_layout.tsx` is a `Stack` root.
- `app/index.tsx` renders `greeting(name)` from `lib/greeting.ts`, a pure function the screen uses, and `lib/greeting.test.ts` tests it with jest.
- `.env.example` holds `EXPO_PUBLIC_CONVEX_URL=` when the backend is selected.
- Optional, on request: Maestro end-to-end flows in `.maestro/`.

### Babel and Metro

Expo's defaults need no `babel.config.js` or `metro.config.js`. Do not create them unless a feature needs them. This includes monorepos, which Metro detects on its own.

If Metro fails to resolve packages under pnpm's isolated layout, set `nodeLinker: hoisted` in `pnpm-workspace.yaml`. Record why in `AGENTS.md`.

## Backend wiring

Apply this section when the plan includes a backend.

- `lib/environment.ts` exports `requireConvexUrl()`, reading `process.env.EXPO_PUBLIC_CONVEX_URL` by its literal name. It has the same shape as the [web file](web-nextjs.md#files).
- `app/_layout.tsx` creates one `ConvexReactClient(requireConvexUrl())` at module level and mounts `<ConvexProvider client={client}>` around the `Stack`.
- In a monorepo with `packages/client`, the factory comes from there (see [shared packages](layouts.md#shared-packages)).
- With Better Auth selected, `app/_layout.tsx` mounts `ConvexBetterAuthProvider` with the Expo `authClient` instead of `ConvexProvider`, as in [Auth](backend-convex.md#auth). Take session initialization from the pinned README and the docs it links to; never invent it. Client authentication is unverified unless it was exercised.
- `lib/environment.test.ts` asserts that `requireConvexUrl()` throws when `EXPO_PUBLIC_CONVEX_URL` is unset.
- Never ship an unmounted provider.

## i18n

Apply this section when i18n is selected.

Use `i18next` with `react-i18next`, plus `expo-localization` (install it with `expo install`). Catalogs live in `i18n/locales/<locale>.json` with the same keys as web.

## Native UI

Apply this section when the UI choice is `@vllnt/ui-native` (experimental). Otherwise use `plain` (React Native styles).

Offer `@vllnt/ui-native` only after an availability check:
- `npm view @vllnt/ui-native dist-tags --json` must show a non-placeholder release.
- The package's published native registry manifest (linked from its README) must report `installation.available: true`.

If either check fails, scaffold `plain` and add a "native UI library pending" line to `AGENTS.md`.

When it is available:
- Install it pinned to the annex version exactly (see [Canary packages](baseline.md#canary-packages)), and mount `<ThemeProvider colorScheme="system">` at the root.
- It needs no Tailwind, NativeWind, Babel or Metro changes.
- Peers: `react >=19.0.0 <20` and `react-native >=0.81.0 <1`.
- Exports include `ThemeProvider`, `useTheme`, `Button`, `Card`, `Text` and `Heading`. Components take `style`, `onPress` and accessibility props, not `className`.
- Never use `@vllnt/ui` (web) or `@vllnt/analytics` in mobile.

## Deploy

Apply this section when the mobile deploy target is `eas`.

`eas.json` has `development` (dev client, internal), `preview` (internal) and `production` profiles. It contains no hostnames, keys or project ids. The user links the project with `eas init` later.
