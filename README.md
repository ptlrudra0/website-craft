# Website Craft

A portable website-design workflow with industry-aware direction recipes, source-aware assets and same-brief example pairs. Built to help a coding agent make deliberate choices, not reuse one landing-page skeleton.

**Early public preview.** Four original SVG motifs, seven industry categories with alternative directions, and four authored demo pages. This is not a vast stock-asset pack, a universal agent integration, or proof of better output than every competing skill.

## Start here

1. Give your coding agent the complete `skills/website-craft/` folder and ask it to use Website Craft.
2. Describe your business, audience and main action. A reference is optional.
3. Review the proposed direction, then build and check the actual result.

The skill opens each new website request with this invitation:

> For a more tailored result, share a reference from Behance, Cosmos or Dribbble. It helps clarify the layout, typography and mood. No reference? I can still work from your brief.

Already supplied a reference? It acknowledges that instead of asking again. A reference communicates direction; it does not grant rights to copy assets.

## What is included

- [Portable skill](skills/website-craft/SKILL.md)
- [Industry directions](skills/website-craft/references/industry-sets.json): technology business, farm/poultry, food/hospitality, professional services, health/wellness, creative/culture, retail/product. These are direction recipes; only the first two have demo variants here.
- [Asset catalog](skills/website-craft/assets/catalog.json): four editable original conceptual SVGs, plus explicitly external discovery sources. Not a stock photo mirror.
- [Same-brief examples](examples/index.html): product-lab vs technical-editorial; field-journal vs supply-ledger. These are authored demonstrations, not repeated autonomous model runs.
- [Chatbot copy/paste route](prompts/CHAT.md), [compatibility matrix](docs/COMPATIBILITY.md), [documented competitor comparison](docs/BENCHMARK.md), [test summary](docs/VALIDATION.md).
- [Optional scroll-craft resource](skills/website-craft/references/resources.md) by Nate Herk, linked and credited. No code vendored, no automatic plugin install or paid generator.

## Try the examples locally

From this repository, run `python -m http.server 8000 --bind 127.0.0.1`, then open `http://localhost:8000/examples/`. Stop the server when finished. The pages need no build, network images, keys or JavaScript. No real orders, messages or forms are submitted.

## Install in a coding agent

Copy the entire `website-craft` skill folder, not only SKILL.md, into a location documented by your client. Common routes: Codex/Cursor/OpenCode `.agents/skills/website-craft/`; Cursor also `.cursor/skills/website-craft/`; OpenCode also `.opencode/skills/website-craft/`. Check current product documentation and merge existing instructions rather than overwrite them. See the matrix for evidence limits and other hosts.

For a chatbot, paste the chat prompt and relevant files or attach them where supported. Chat-only use can produce plans/code; it cannot honestly claim browser testing or deployment without those tools. Native agent execution is not yet tested across products.

## How variety works

Choose by audience, business job, content evidence and mood, not just industry. Alternative plans should differ in information order, composition, typography, imagery or purposeful interaction. A palette swap alone is not a different direction. Preserve the user's brand/reference rather than randomizing for novelty. See [variation review](skills/website-craft/references/variation-review.md).

## Rights

Original text, code and four SVG motifs are MIT, copyright 2026 ptlrudra0. External resources retain their own terms. Behance/Cosmos/Dribbble are inspiration links, not free asset licences. Unsplash photos are not bundled; check exact current terms for selected use. Never claim a stock image depicts the actual client or proves a certification. See [rights guidance](skills/website-craft/references/rights.md).

## Current limits and next work

No controlled cross-agent performance benchmark, real-device testing or accessibility certification. More rights-reviewed media and more industry examples are needed. Contributions should add a coherent direction, item-level provenance and evidence of actual checks rather than inflate asset counts. Do not contribute private client data or third-party gallery dumps.
