# Compatibility: documented, not universally tested

The core is plain Markdown plus JSON, with no required package install or paid API. A text-capable chatbot can discuss it; building, previewing and deploying require host capabilities. No end-to-end execution inside these agent products has been tested for this release.

| Host | Documented route | This release's evidence |
|---|---|---|
| Codex | Copy complete website-craft folder into .agents/skills/ | Format/path checked against official docs; runtime untested |
| Cursor | .agents/skills/ or .cursor/skills/ | Official docs reviewed; runtime untested |
| OpenCode | .opencode/skills/website-craft/ or .agents/skills/website-craft/ | Official docs reviewed; runtime untested |
| Claude Code | Use standard skill folder according to current product documentation, or explicitly ask it to read the complete folder | Portable core prepared; native install not tested here |
| GitHub Copilot | Reference the workflow through repository instructions supported by your current client | Official custom-instructions docs reviewed; native skill behaviour depends on client |
| ChatGPT, Claude chat, Gemini and other chatbots | Paste prompts/CHAT.md plus needed files, or attach them where supported | Text route only; no account-specific compatibility tests |
| Other agents | Explicitly read the complete folder; adapt to documented instructions format | Untested |

Sources checked 2026-11-05:
https://agentskills.io/specification
https://developers.openai.com/codex/skills/
https://cursor.com/docs/skills
https://opencode.ai/docs/skills/
https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
https://agents.md/

Manual copying does not override an agent's own policies or give it missing tools. Keep all references/assets together and inspect instructions from any third-party dependency before use. Never overwrite an existing project's instructions without reviewing the merge.
