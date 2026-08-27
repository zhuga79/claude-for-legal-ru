# Review: administrativnoe-pravo

Reviewer: codex-gpt-5, cross-provider review, 2026-08-27.

## Verdict

PASS_WITH_WARNINGS after fixes.

## Critical

- No open critical issues.

## High

- Fixed during this review: root profile narrowed the inspections moratorium to SMEs, while the GIT skill described the moratorium more broadly for organizations and IPs with risk-based exceptions. Current profile now states the broader rule and exceptions: `administrativnoe-pravo/CLAUDE.md:127`.

## Medium

- No open medium packaging issues found after `claude plugin validate administrativnoe-pravo`.

## Low

- `claude plugin validate` reports the known plugin-root `CLAUDE.md` warning. Non-blocking in this repo pattern.

## Suspect / needs primary-source check

- KoAP penalty amounts and 248-FZ inspection exceptions change frequently; the plugin correctly marks current checks as required, but concrete outgoing documents must re-open the primary sources.

## Confirmed good

- The plugin separates administrative-offense proceedings under KoAP from control/supervision events under 248-FZ.
- Criminal stop-triggers are present and route out of the administrative skill.
