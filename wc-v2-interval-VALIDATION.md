# Local validation record

## Exercised
- Five routes,320/390/768/1024/1440:25actual Chromium renders. No page overflow. One H1 each. All buttons/inputs measured at least44by44CSS pixels. Actual phone, desktop and mid-width pixels inspected; generated waveform page visually reinspected after change.
-48native toggle buttons, actual edit/undo/clear, arrow/Home navigation, invalid tempo then recovery, explicit live play and edit stopping, hidden-page stop.
- Actual downloaded WAV checked with Python wave reader: RIFF/PCM16mono44.1kHz, current tempo120BPM =>2.3seconds including tail, nonzero audio samples, no full-scale PCM clipping. Empty pattern actual download all-zero samples and explicit silence note.
- Maximum-density pattern at180BPM and70%volume deterministic. Mix maximum0.708738/minimum-0.489129, below clipping threshold. This is numerical headroom, not a hearing-safety or sound-quality guarantee.
- Web Audio unavailable: truthful error, independent actual WAV download still succeeds. JavaScript disabled: notice visible and inactive instrument hidden; other content/navigation remains.
- Delayed audio resume followed by pattern edit: cancellation token prevents stale playback start. Reduced-motion mode removes playback-position pulse.
- Axe five pages: zero automated violations after fixing missing landmark and step accessible names that omitted visible zero padding. Manual incomplete nodes are decorative wordmark dots and export arrow. Blue/cream approximately7.17:1; white/dark approximately17.4:1. Labels remain when decorative shapes are hidden. Automated checks are not accessibility certification.

## Actual defects found and fixed
Initial narrow-grid eight-column plan could not retain44px controls; narrow phones now use four columns. Over-tight heading tracking relaxed. SVG sound plots now derive from actual synthesis instead of suggestive wave drawings. Async playback start can no longer run a changed pattern after delayed resume. Initial markup scaffold accidentally separated h1/h2 tags while adjusting prose spacing; corrected before testing completion. Axe label-in-name and landmark findings fixed and rerun.

## Not established
No actual human listening evaluation, hearing safety, studio quality, physical device, Safari, assistive technology, native coding-client install, field performance or production audio timing proof. Read tool found no speech in example WAV; that is not listening-quality assessment. Live setInterval playback is not sample-accurate. State intentionally session-only. No publication or commercial launch implied.

## Chronology refinement after review
The actual phone editor now separates each track into four labelled beat groups: Beat1/01-04, Beat2/05-08, Beat3/09-12, Beat4/13-16. Narrow layouts stack groups in order; tablet places two groups on each row; desktop puts four groups across. Visible zero-padded step numbers remain inside native buttons and their accessible names. Arrow/Home movement uses all16steps rather than DOM children, so group wrappers do not break navigation.25renders and all interaction/audio/axe tests rerun after this refinement. Home preview now numbers each step too; it remains a noninteractive overview, not the editor. Phone/tablet chronology visually inspected. No actual usability study is claimed.

## Initial-load layout stability / 6 November
Local Chromium, Python HTTP server,390x844, fresh context, three runs per route, no CPU/network throttling. Not field Core Web Vitals or real-mobile speed. INP not measured.
- index.html: maximum observed CLS 0.0328; maximum initial transfer 219000 bytes; median lab LCP 104ms. Only initial viewport; offscreen lazy media not forced.
- instrument.html: maximum observed CLS 0.0000; maximum initial transfer 219301 bytes; median lab LCP 132ms. Only initial viewport; offscreen lazy media not forced.
The JS-enabled tool shell now reserves its initial layout while deferred code initializes, without exposing inactive controls. With JavaScript disabled it remains hidden and the useful notice remains visible. A prior local run observed CLS0.56 in Relay and0.415 in Interval; after fixing tool reveal these sampled routes measured below0.001 and0 respectively.
After the fix: layout and journey/failure/keyboard tests rerun, actual phone tool pixels visually reinspected. These three-run local samples are regression evidence, not a universal guarantee.

## Partial-script startup recovery
Blocked application script and required fixture independently, plus Interval synthesis script (seven actual failure scenarios across the three products). Each shows a visible reload/guide notice; actual reload after removing the block recovers the ready state. Failed Relay/Interval shells collapse instead of leaving a long reserved blank region. Morrow controls remain disabled until app and product data initialize, preventing a dead form from looking usable. Ordinary JS-disabled navigation still works. Startup notices stay as quiet ready/session-state notes after success to avoid introducing another load-time layout shift. Actual phone failure and normal tool pixels visually inspected. This does not establish every possible runtime failure.

## Forced-colors selection
Chromium forced-colors emulation previously erased selected backgrounds. Added system-color borders/underlines and a visible step dot so selection does not depend on the replaced fill. Selected steps, filters and pack options checked at 320/390/1024px; actual phone instrument/filter pixels inspected. This is browser emulation, not native Windows high-contrast or screen-reader proof.
