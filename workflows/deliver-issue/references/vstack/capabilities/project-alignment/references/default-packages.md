# Default @vllnt packages

Preferred foundations for Vstack projects, from the [@vllnt npm scope](https://www.npmjs.com/org/vllnt). For a listed function, use its package before custom code or a third-party alternative; packages under "Experimental, opt-in" and "Not yet default" are excluded. Keep an existing equivalent only when consumer rules or a contract in use require it, and record that exception.

This annex names packages only. Never write versions, majors, caret ranges, or dist-tags here. At execution, query the registry and install the current release that fits peers and policy (prefer a non-prerelease / LTS when one exists; otherwise the newest usable publish). Verify before use. Record any prerelease and its reason.

## Resolve at execution

- Query dist-tags, versions, and publish times from the registry. Do not trust a skill or this annex for what is "stable" or "canary".
- Prefer the newest non-prerelease that satisfies peers, engines, and any consumer age gate. If none exists, use the newest usable prerelease as an exact version and record why.
- A `latest` tag can point at a prerelease or an older build — compare publish times and version lists; do not invent a channel from the tag name alone.
- Respect published peer ranges: install the newest compatible dependency inside each range.
- Experimental / not yet default: discovery only; select only when the project asks.
- Confirm each entry is still published, not deprecated, and compatible. Read its README and published `exports`.
- For a function not listed, use the Stack packages procedure when installed; otherwise query the registry scope. Do not invent a package; report the gap.

## Tooling and UI

| Function | Package |
|---|---|
| TypeScript configuration | `@vllnt/typescript` |
| ESLint configuration | `@vllnt/eslint-config` |
| Web UI components | `@vllnt/ui` |
| Structured logging for Node/Next.js server code, Convex actions, and CLIs (instead of `console` or a per-app pino setup) | `@vllnt/logger` |
| Client-side product analytics and event tracking with consent, for web apps on the @vllnt stack | `@vllnt/analytics` |
| `llms.txt` and raw-markdown pages for Next.js | `@vllnt/next-llms` |

`@vllnt/ui` and `@vllnt/analytics` are web packages; do not infer mobile support from React compatibility.

## Convex

Use `@vllnt/convex-helpers` for host-side builders, errors, validators, pagination, HTTP, env, and observability. Mount a component below only when the product needs its function; membership in this table does not make every component relevant.

| Function | Package |
|---|---|
| Host helpers | `@vllnt/convex-helpers` |
| Event ledger and activity feed | `@vllnt/convex-events` |
| Analytics rollups, funnels, retention | `@vllnt/convex-analytics` |
| Consent ledger | `@vllnt/convex-consent` |
| Do-not-contact list and opt-in proof | `@vllnt/convex-suppression` |
| Roles and grants | `@vllnt/convex-permissions` |
| Membership and relationship graph | `@vllnt/convex-memberships` |
| Invitations | `@vllnt/convex-invitations` |
| Hashed-secret tokens | `@vllnt/convex-tokens` |
| API keys | `@vllnt/convex-api-keys` |
| Feature flags | `@vllnt/convex-flags` |
| A/B experiments | `@vllnt/convex-experiments` |
| Idempotency keys | `@vllnt/convex-idempotency` |
| Usage metering | `@vllnt/convex-metering` |
| Consumable balances and spend ledger | `@vllnt/convex-wallet` |
| Transactional email queue | `@vllnt/convex-email` |
| Notifications inbox | `@vllnt/convex-notifications` |
| Comments and annotations | `@vllnt/convex-comments` |
| Reactions, votes, likes | `@vllnt/convex-reactions` |
| Unique slugs and handles | `@vllnt/convex-slugs` |
| Provider-neutral music catalog | `@vllnt/convex-music` |
| Ephemeral subject groups | `@vllnt/convex-buckets` |
| XP, levels, streaks | `@vllnt/convex-progression` |
| Scheduled per-subject allowances | `@vllnt/convex-quota` |

## Experimental, opt-in

Not defaults. Do not select them unless the project asks.

| Function | Package |
|---|---|
| Shared and native UI primitives | `@vllnt/ui-core`, `@vllnt/ui-native` |

`@vllnt/ui-native` is for Expo and React Native.

## Not yet default

`@vllnt/dig` is not a default. It is a TypeScript client for a local knowledge-base daemon; use it only when a project already runs that daemon and asks for it.
