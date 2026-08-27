# Review: nedvizhimost

Reviewer: codex-gpt-5, cross-provider review, 2026-08-27.

## Verdict

PASS_WITH_WARNINGS after fixes.

## Critical

- No open critical issues.

## High

- Fixed during this review: moratorium/deferral under PP No. 326/2227 was too broad. The plugin stated the 2026 deferral as covering all claims presented to the developer before 01.01.2026. Current text now narrows this to old claims by category and explicitly says not to use the universal "до 01.01.2026" formula: `nedvizhimost/CLAUDE.md:49`, `nedvizhimost/references/currency-watch.md:30`, `nedvizhimost/skills/ddu-proverka/SKILL.md:157`.

## Medium

- No open medium issues found in packaging after `claude plugin validate nedvizhimost`.

## Low

- `claude plugin validate` reports the known plugin-root `CLAUDE.md` warning. This is non-blocking in this repo pattern because executable guidance is in skills and root files are config templates.

## Suspect / needs primary-source check

- `nedvizhimost/CLAUDE.md:61` leaves 2026 developer capital / disclosure thresholds as `[проверить]`; that is acceptable but must not be used as verified law in outputs.
- Specific Rosreestr/MFC timing variants remain highly changeable and should be rechecked per matter.

## Confirmed good

- DDU registration fee now uses 700 / 12 000 ₽ and the current text distinguishes DDU registration from right-registration fees.
- New deferral text matches the current risk model: no blind reliance on memory; primary-source check required for each calculation.
