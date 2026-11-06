# Candidate test boundary / 5 November 2026

Local candidate, not published. Chromium: 25 actual full-page renders across five routes at 320/390/768/1024/1440 pixels. No overflow, unloaded images or uncaught JavaScript errors. Actual desktop/phone/tablet/midwidth pixels inspected for all routes and populated editor/review.

Normal export, edit/review invalidation, remove/undo, filters and return persistence checked. Actual exported Markdown and clipboard text read back. Eight edge scenarios passed: invalid/empty input, text-not-markup, actual clipboard, replace/cancel/Escape/undo, cross-tab no-silent-overwrite, edited review invalidation, storage-blocked actual incomplete-draft download, JavaScript-off readable navigation.

Deeper checks: all fields at maximum lengths across all five widths with no overflow; reduced-motion scroll disabled; corrupt schema rejected; failed original SVG without layout overflow; visible tool buttons at least44x44 CSS pixels. Dialog Tab/Shift+Tab initially found a focus escape to the document body. Explicit focus cycling was added and actual forward/backward trap, Escape and trigger return now pass. This browser test does not prove all assistive-technology behavior.

Latest axe-core normal-state scan: zero automated WCAG2 A/AA/2.1 AA violations across five pages. Populated editor/review zero violations or incomplete checks. Open replacement dialog zero violations, one incomplete manual check. Home has one incomplete arrow-only contrast rule; arrows are decorative beside semantic labelled steps. Normal-page automated audit is not an accessibility certificate.

Physical devices, Safari, screen readers, production backend, native coding-agent installation and field performance remain untested. Local transfer/latency readings are not Core Web Vitals field results. Authored specimen is not an independent generated-agent benchmark.

## Initial-load layout stability / 6 November
Local Chromium, Python HTTP server,390x844, fresh context, three runs per route, no CPU/network throttling. Not field Core Web Vitals or real-mobile speed. INP not measured.
- index.html: maximum observed CLS 0.0026; maximum initial transfer 424455 bytes; median lab LCP 108ms. Only initial viewport; offscreen lazy media not forced.
- workbench.html: maximum observed CLS 0.0009; maximum initial transfer 424965 bytes; median lab LCP 84ms. Only initial viewport; offscreen lazy media not forced.
The JS-enabled tool shell now reserves its initial layout while deferred code initializes, without exposing inactive controls. With JavaScript disabled it remains hidden and the useful notice remains visible. A prior local run observed CLS0.56 in Relay and0.415 in Interval; after fixing tool reveal these sampled routes measured below0.001 and0 respectively.
After the fix: layout and journey/failure/keyboard tests rerun, actual phone tool pixels visually reinspected. These three-run local samples are regression evidence, not a universal guarantee.

## Partial-script startup recovery
Blocked application script and required fixture independently, plus Interval synthesis script (seven actual failure scenarios across the three products). Each shows a visible reload/guide notice; actual reload after removing the block recovers the ready state. Failed Relay/Interval shells collapse instead of leaving a long reserved blank region. Morrow controls remain disabled until app and product data initialize, preventing a dead form from looking usable. Ordinary JS-disabled navigation still works. Startup notices stay as quiet ready/session-state notes after success to avoid introducing another load-time layout shift. Actual phone failure and normal tool pixels visually inspected. This does not establish every possible runtime failure.

## Clipboard revision race
Delayed successful and failed clipboard promises resolved after editing and reviewing a new draft cannot mark that revision copied or failed. Only the latest copy request for the current revision updates status. This does not cancel a dispatched browser clipboard write. Actual clipboard journey checks rerun separately.

## Focus after mutation
Changing state inside a filtered view moves focus to the active filter after the item leaves the view, with an announced remaining count. Actual keyboard continuation, empty-state action and dialog Escape return checked at 320, 390 and 1024px. These are browser keyboard checks, not screen-reader proof.

## Forced-colors selection
Chromium forced-colors emulation previously erased selected backgrounds. Added system-color borders/underlines and a visible step dot so selection does not depend on the replaced fill. Selected steps, filters and pack options checked at 320/390/1024px; actual phone instrument/filter pixels inspected. This is browser emulation, not native Windows high-contrast or screen-reader proof.
