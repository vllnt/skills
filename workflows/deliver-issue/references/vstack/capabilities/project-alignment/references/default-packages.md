# Default @vllnt packages

Preferred foundations for Vstack projects, from the [@vllnt npm scope](https://www.npmjs.com/org/vllnt). For a listed function, use its package before custom code or a third-party alternative; packages under "Experimental, opt-in" and "Not yet default" are excluded. Keep an existing equivalent only when consumer rules or a contract in use require it, and record that exception.

This annex names packages and channels only. Never write majors, caret ranges, or canary SHAs here. Resolve the exact version at execution from the registry and consumer peers, then verify before use.

## Channel rules

- Default every package to its latest release, resolved at run time from the registry (its dist-tags and publish times), never from a version written in a skill.
- Stable packages: install the latest stable release.
- Canary-only packages: first check whether a stable release now exists and, if so, treat the package as stable. Otherwise install the newest canary by publish time, as an exact version, and record it as a prerelease with its reason in the consumer's agent file. A `latest` tag can point at an older prerelease, so compare publish times instead of trusting the tag.
- Respect published peer ranges: when a selected package peers a dependency, install the newest version of that dependency inside the range.
- Experimental / not yet default: listed for discovery only, never chosen by default. Select one only when the project asks for it.
- Before relying on an entry, confirm it is still published, not deprecated, and compatible with the consumer's framework, TypeScript, and runtime peers. Read its README and published `exports` for usage.
- For a function not listed, use the Stack packages procedure when installed; otherwise query the registry scope directly. Do not name, assume, or create a package; report the gap as a package request.

## Tooling and UI

| Function | Package | Channel |
|---|---|---|
| TypeScript configuration | `@vllnt/typescript` | stable |
| ESLint configuration | `@vllnt/eslint-config` | stable |
| Web UI components | `@vllnt/ui` | stable |
| Structured logging for Node/Next.js server code, Convex actions, and CLIs (instead of `console` or a per-app pino setup) | `@vllnt/logger` | stable |
| Client-side product analytics and event tracking with consent, for web apps on the @vllnt stack | `@vllnt/analytics` | stable |
| `llms.txt` and raw-markdown pages for Next.js | `@vllnt/next-llms` | canary-only |

`@vllnt/ui` and `@vllnt/analytics` are web packages; do not infer mobile support from React compatibility.

## Convex

Use `@vllnt/convex-helpers` for host-side builders, errors, validators, pagination, HTTP, env, and observability. Mount a component below only when the product needs its function; membership in this table does not make every component relevant.

| Function | Package | Channel |
|---|---|---|
| Host helpers | `@vllnt/convex-helpers` | stable |
| Event ledger and activity feed | `@vllnt/convex-events` | stable |
| Analytics rollups, funnels, retention | `@vllnt/convex-analytics` | stable |
| Consent ledger | `@vllnt/convex-consent` | stable |
| Do-not-contact list and opt-in proof | `@vllnt/convex-suppression` | stable |
| Roles and grants | `@vllnt/convex-permissions` | stable |
| Membership and relationship graph | `@vllnt/convex-memberships` | stable |
| Invitations | `@vllnt/convex-invitations` | stable |
| Hashed-secret tokens | `@vllnt/convex-tokens` | stable |
| API keys | `@vllnt/convex-api-keys` | stable |
| Feature flags | `@vllnt/convex-flags` | stable |
| A/B experiments | `@vllnt/convex-experiments` | stable |
| Idempotency keys | `@vllnt/convex-idempotency` | stable |
| Usage metering | `@vllnt/convex-metering` | stable |
| Consumable balances and spend ledger | `@vllnt/convex-wallet` | stable |
| Transactional email queue | `@vllnt/convex-email` | stable |
| Notifications inbox | `@vllnt/convex-notifications` | stable |
| Comments and annotations | `@vllnt/convex-comments` | stable |
| Reactions, votes, likes | `@vllnt/convex-reactions` | stable |
| Unique slugs and handles | `@vllnt/convex-slugs` | stable |
| Provider-neutral music catalog | `@vllnt/convex-music` | stable |
| Ephemeral subject groups | `@vllnt/convex-buckets` | canary-only |
| XP, levels, streaks | `@vllnt/convex-progression` | canary-only |
| Scheduled per-subject allowances | `@vllnt/convex-quota` | canary-only |

## Experimental, opt-in

Not defaults. Do not select them unless the project asks.

| Function | Package | Channel |
|---|---|---|
| Shared and native UI primitives | `@vllnt/ui-core`, `@vllnt/ui-native` | experimental, opt-in; canary-only |

`@vllnt/ui-native` is for Expo and React Native.

## Not yet default

`@vllnt/dig` (canary-only) is not a default. It is a TypeScript client for a local knowledge-base daemon; use it only when a project already runs that daemon and asks for it.
