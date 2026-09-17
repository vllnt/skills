# Page audit snippets

Run these heuristic resource and timing snippets through an available browser evaluator. The optional agent-browser syntax below must match installed help; equivalent browser tools work. They are not scores or conformance checks. Inspect and sanitize all outputs before sharing, including page text and resource URLs.

## How to run (avoid shell-quoting pain)

Complex JS breaks on nested quotes. Prefer a file + `--stdin`:

```bash
# write the snippet to a file, pipe it in
agent-browser open https://example.com
agent-browser eval --stdin < audit.js
```

Or base64 (no escaping at all):

```bash
B64=$(base64 < audit.js | tr -d '\n')
agent-browser eval -b "$B64"
```

Inline single-line works for short checks (single quotes outside, none inside):

```bash
agent-browser eval 'document.querySelectorAll("img:not([alt])").length'
```

Each snippet ends in a `JSON.stringify(...)` so the result is machine-readable.

---

## Resource weight audit

Uses the Resource Timing API — byte sizes + slowest requests, no HAR needed. Cross-origin timing restrictions and cache hits can yield zero/missing sizes; do not treat these totals as complete transferred page weight. Encoded body size and transfer size are different quantities. URLs below still need privacy review.

```js
// audit.resources.js
const r = performance.getEntriesByType('resource');
const byType = {};
let total = 0;
for (const e of r) {
  const t = e.initiatorType || 'other';
  const bytes = e.transferSize || e.encodedBodySize || 0;
  byType[t] = (byType[t] || 0) + bytes;
  total += bytes;
}
const kb = n => Math.round(n / 1024);
JSON.stringify({
  requestCount: r.length,
  totalKB: kb(total),
  byTypeKB: Object.fromEntries(Object.entries(byType).map(([k, v]) => [k, kb(v)])),
  slowest: r.map(e => ({ url: e.name.slice(0, 80), ms: Math.round(e.duration), kb: kb(e.transferSize || 0) }))
           .sort((a, b) => b.ms - a.ms).slice(0, 10),
  heaviest: r.map(e => ({ url: e.name.slice(0, 80), kb: kb(e.transferSize || 0) }))
           .sort((a, b) => b.kb - a.kb).slice(0, 10),
})
```

---

## Render-blocking audit

Candidate scripts/styles in `<head>` that may block first paint. Confirm timing and blocking in an actual browser trace; markup order alone does not establish causality.

```js
// audit.blocking.js
const blockingScripts = [...document.querySelectorAll('head script[src]')]
  .filter(s => !s.async && !s.defer && (s.type === '' || s.type === 'text/javascript' || !s.type))
  .map(s => s.src);
const blockingStyles = [...document.querySelectorAll('head link[rel="stylesheet"]')]
  .filter(l => !l.media || l.media === 'all' || l.media === 'screen')
  .map(l => l.href);
JSON.stringify({
  blockingScriptCount: blockingScripts.length,
  blockingScripts: blockingScripts.slice(0, 15),
  blockingStyleCount: blockingStyles.length,
  blockingStyles: blockingStyles.slice(0, 15),
  thirdPartyScripts: [...document.querySelectorAll('script[src]')]
    .map(s => { try { return new URL(s.src).host; } catch { return null; } })
    .filter(h => h && h !== location.host)
    .filter((h, i, a) => a.indexOf(h) === i),
})
```

---

## Navigation timing (waterfall phases)

```js
// audit.timing.js
const n = performance.getEntriesByType('navigation')[0];
const ms = x => Math.round(x);
JSON.stringify(n ? {
  dns: ms(n.domainLookupEnd - n.domainLookupStart),
  tcp: ms(n.connectEnd - n.connectStart),
  ttfb: ms(n.responseStart - n.requestStart),
  download: ms(n.responseEnd - n.responseStart),
  domInteractive: ms(n.domInteractive),
  domContentLoaded: ms(n.domContentLoadedEventEnd),
  loadComplete: ms(n.loadEventEnd),
  transferKB: Math.round((n.transferSize || 0) / 1024),
} : { error: 'no navigation entry' })
```

---

## Interpreting results

- These are **heuristics from one browser session**. Resource and timing signals need traces or comparable measurements before a causal claim. See [measurement workflow](../SKILL.md).
