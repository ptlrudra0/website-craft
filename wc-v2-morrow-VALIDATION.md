# Local test boundary

This fictional product specimen has 10 pages and a browser-local enquiry planner. It does not process orders, reserve stock, send messages or take payment. It remains a local candidate, separate from the earlier published preview.

## Verified locally

- Chromium: 50 renders at 360/390/768/1024/1440 pixels. No horizontal overflow, missing images, failed local links or uncaught JavaScript errors in the normal-media run.
- Full product-pack/quantity flow, local persistence, list edit/clear/empty states, drawer focus/Escape return, category filter, phone menu, prepared enquiry and regular-supply brief. Actual clipboard text was read back and downloaded plain text inspected.
- Draft invalidation after list/form edits and cross-tab changes, safe text handling, invalid quantities and corrupted storage rejection. Stored pack names must match the product's permitted options.
- Simulated unavailable storage, clipboard denial, disabled JavaScript and failed photographs. Storage-disabled mode warns that data cannot survive navigation/reload and offers an actual downloaded-list recovery before leaving; clipboard denial offers manual copy. With JavaScript disabled the navigation and reading remain available, local tools are hidden and explained. Failed photos show a named original illustration without breaking layout.
- Deterministic standard-library build with shared navigation/footer/drawer partials and a single product-data source for runtime selection and catalogue cards.

## Accessibility evidence and limits

Axe-core WCAG 2 A/AA and 2.1 AA scan found no violations on 10 normal-state pages. Three incomplete contrast nodes were manually reviewed: burgundy on butter about 11.32:1, white credit text on the darkest-transparent overlay with worst-case white photo backing about 5.75:1, white on red button about 5.24:1. These ratios are for the reviewed colours, not every UI state. The arrow symbol has an accessible link label.

The scan is not an accessibility certificate. Real screen readers, physical devices, older Safari and deployed network conditions remain untested. Local unthrottled resource/latency readings are not a public performance score. Screenshot inspection is recorded separately from automated checks.

No independent coding-agent execution or native-client installation compatibility result is claimed for this specimen. These are authored reference products, not model benchmark results. MIT covers original code/illustration only; fonts and selected photos keep their own notices/terms. See credits.html, media/CREDITS.md and fonts/*-OFL.txt.

## Initial-load layout stability / 6 November
Local Chromium, Python HTTP server,390x844, fresh context, three runs per route, no CPU/network throttling. Not field Core Web Vitals or real-mobile speed. INP not measured.
- index.html: maximum observed CLS 0.0538; maximum initial transfer 624858 bytes; median lab LCP 156ms. Only initial viewport; offscreen lazy media not forced.
- enquiry.html: maximum observed CLS 0.0175; maximum initial transfer 467150 bytes; median lab LCP 140ms. Only initial viewport; offscreen lazy media not forced.
Initial empty enquiry-list content is now in the static page so deferred rendering does not suddenly insert it below the heading. A prior local run observed CLS0.174 there before this fix.
After the fix: layout and journey/failure/keyboard tests rerun, actual phone tool pixels visually reinspected. These three-run local samples are regression evidence, not a universal guarantee.

## Partial-script startup recovery
Blocked application script and required fixture independently, plus Interval synthesis script (seven actual failure scenarios across the three products). Each shows a visible reload/guide notice; actual reload after removing the block recovers the ready state. Failed Relay/Interval shells collapse instead of leaving a long reserved blank region. Morrow controls remain disabled until app and product data initialize, preventing a dead form from looking usable. Ordinary JS-disabled navigation still works. Startup notices stay as quiet ready/session-state notes after success to avoid introducing another load-time layout shift. Actual phone failure and normal tool pixels visually inspected. This does not establish every possible runtime failure.

## Clipboard revision race
Delayed successful and failed clipboard promises were resolved after editing and preparing a new enquiry/supply brief. Old completions cannot mark the current revision copied or failed; current completion reports normally. Clipboard calls themselves cannot be undone after dispatch. Actual clipboard journey tests rerun separately from the delayed-promise test.

## Focus after mutation
Quantity edits preserve focus on the matching rebuilt input in both main list and dialog. Removing the final item moves focus to the empty-state range link instead of the document body. Actual keyboard continuation, empty-state action and dialog Escape return checked at 320, 390 and 1024px. These are browser keyboard checks, not screen-reader proof.

## Destructive list recovery
Removal/clear now has one-level on-page Undo, with visible persistent recovery beside the list. Clear/recovery, dialog removal/recovery, invalidated prepared draft, focus return and saved restored quantity verified at 320/390/1024px. Undo is session-only and drops on a later add/quantity edit, external list update or reload.

## Forced-colors selection
Chromium forced-colors emulation previously erased selected backgrounds. Added system-color borders/underlines and a visible step dot so selection does not depend on the replaced fill. Selected steps, filters and pack options checked at 320/390/1024px; actual phone instrument/filter pixels inspected. This is browser emulation, not native Windows high-contrast or screen-reader proof.
