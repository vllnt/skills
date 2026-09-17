# Optimization Playbook — metric → root cause → fix

Map a measured failure to its likely cause, then the smallest fix that targets it.
Confirm the cause with available browser traces, resource timings and actual Lighthouse audit results before changing code. Tool commands and audit names vary by installed version. Fix one lever at a time, then re-measure using the [measurement workflow](../SKILL.md). Infrastructure/cache changes need authorization and must preserve privacy, freshness and application semantics.

---

## LCP — Largest Contentful Paint

The LCP element is usually the hero image, a heading, or a large text block above the fold.

| Root cause | Evidence | Fix |
|------------|----------|-----|
| Slow TTFB | `vitals` TTFB > 0.8s | CDN/edge, server cache, SSG/ISR, cut DB work on the critical path |
| Render-blocking CSS/JS | `network requests` shows `.css`/`.js` before first paint; Lighthouse "Eliminate render-blocking resources" | Inline critical CSS, `defer`/`async` non-critical JS, split CSS by route |
| LCP image loads late | LCP element is an `<img>` discovered late | `<link rel=preload as=image>` the LCP image; `fetchpriority="high"`; avoid lazy-loading above-the-fold images |
| Unoptimized hero image | large bytes in HAR for the LCP resource | AVIF/WebP, responsive `srcset`/`sizes`, correct dimensions, framework image component (`next/image` etc.) |
| Client-side rendered LCP | empty HTML, LCP appears only after JS | SSR/SSG the above-the-fold content; stream HTML |
| Slow web font blocking text LCP | font request blocks text paint | `font-display: swap`/`optional`, `preload` the font, subset it, self-host |

---

## CLS — Cumulative Layout Shift

Caused by content that moves after it first paints.

| Root cause | Evidence | Fix |
|------------|----------|-----|
| Images/video without dimensions | `eval` finds `<img>` lacking width/height; Lighthouse "Image elements do not have explicit width and height" | Set `width`+`height` (or `aspect-ratio`) so space is reserved |
| Injected content (ads, embeds, banners) | shift happens as 3rd-party loads | Reserve a fixed-size container before load |
| Web font swap (FOUT) | shift on font load | `size-adjust`/`font-display: optional`, preload font, match fallback metrics |
| Dynamically inserted DOM above existing content | shift after data fetch | Render skeletons of the final size; insert below the fold |
| Non-composited animations | layout animated (top/left/height) | Animate `transform`/`opacity` only |

---

## INP — Interaction to Next Paint and TBT diagnostics

Investigate input delay, event handling and presentation delay during real interactions. TBT is a load-window lab blocking metric, not an INP measurement; improvements in TBT do not establish a field INP gain.

| Root cause | Evidence | Fix |
|------------|----------|-----|
| Long tasks (> 50ms) | Lighthouse "Avoid long main-thread tasks", trace shows long blocks | Break into smaller chunks, `scheduler.yield()`, `requestIdleCallback`, defer non-urgent work |
| Too much JS shipped | Lighthouse "Reduce unused JavaScript" + large script bytes | Code-split, lazy-load routes/components, tree-shake, drop heavy deps |
| Expensive event handlers | INP high on click/input | Debounce/throttle, move CPU work to a Web Worker, memoize |
| Large/complex DOM | Lighthouse "Avoid an excessive DOM size" | Virtualize long lists, paginate, simplify nesting |
| Hydration cost (SSR frameworks) | INP/TBT spike right after load | Partial/selective hydration, islands, defer below-the-fold hydration |
| Forced synchronous layout (layout thrash) | trace shows reflow loops | Batch reads then writes; avoid reading layout in loops |

---

## TTFB — Time To First Byte

| Root cause | Evidence | Fix |
|------------|----------|-----|
| No CDN / far origin | slow TTFB regardless of payload | Put a CDN/edge in front; serve static from edge |
| No caching | every request hits origin | Cache-Control, CDN cache, ISR/SSG, app-level + DB cache |
| Redirect chains | `network requests` shows 3xx before the doc | Link directly to the final URL; collapse redirects |
| Cold serverless start | first hit slow, warm fast | Keep-warm, smaller bundles, faster runtime/region near users |
| Heavy server render / N+1 queries | server time dominates | Pre-render (SSG/ISR), optimize queries, add indexes, cache fragments |

---

## FCP — First Contentful Paint

Usually a subset of LCP+TTFB causes.

| Root cause | Fix |
|------------|-----|
| Render-blocking resources | Inline critical CSS, defer JS, `preconnect`/`dns-prefetch` to key origins |
| Slow TTFB | See TTFB row above |
| Large CSS | Split per route, remove unused (Lighthouse "Reduce unused CSS") |

---

## Network / resource findings → fixes

From `agent-browser network requests` and the HAR / Lighthouse opportunities:

| Finding | Fix |
|---------|-----|
| Render-blocking `<script>` / `<link rel=stylesheet>` | `defer`/`async` JS; inline critical CSS, load rest async |
| Oversized images | AVIF/WebP, responsive sizes, compression, lazy-load below the fold |
| No text compression | Enable gzip/brotli on the server/CDN |
| Missing cache headers on static assets | Long-lived `Cache-Control: immutable` + content hashing |
| Too many requests | Bundle, HTTP/2-3 multiplexing, sprite/inline small assets |
| Failed requests (4xx/5xx) | Fix or remove; 404s waste round-trips and can block |
| Large JS bundles | Code-split, tree-shake, drop/replace heavy libraries, dynamic import |
| Blocking 3rd-party scripts | `async`, lazy-load on interaction, self-host critical ones, audit necessity |
| Unminified JS/CSS | Enable minification in the build |

---

## Quick prioritization

Prioritize the dominant measured bottleneck, not this list mechanically:

1. **TTFB** — when server latency dominates the critical path.
2. **Render-blocking** — cheap wins for FCP/LCP (defer JS, inline critical CSS).
3. **LCP image** — preload + optimize the single largest paint.
4. **CLS** — set dimensions / reserve space (low effort, high score impact).
5. **JS weight / long tasks** — biggest INP lever, usually the most work.

Use the evidence to select a lever; re-measure after each change so you can distinguish observed gains from hypotheses. Keep responsive layout and interaction behavior intact.
