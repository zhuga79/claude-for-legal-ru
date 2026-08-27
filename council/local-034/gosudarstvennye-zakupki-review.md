# Review: gosudarstvennye-zakupki

Reviewer: codex-gpt-5, cross-provider review, 2026-08-27.

## Verdict

PASS_WITH_WARNINGS after fixes.

## Critical

- No open critical issues.

## High

- No open high issues found.

## Medium

- Fixed during this review: `gosudarstvennye-zakupki/CLAUDE.md` referenced `references/currency-watch.md`, but the file was absent. Added `gosudarstvennye-zakupki/references/currency-watch.md:1` with 90-day staleness protocol and explicit volatile topics.

## Low

- `claude plugin validate` reports the known plugin-root `CLAUDE.md` warning. Non-blocking in this repo pattern.

## Suspect / needs primary-source check

- Thresholds, complaint periods, anti-dumping rules, national-regime lists, and RNP procedures are volatile; the new `currency-watch.md` requires primary-source verification before output.

## Confirmed good

- The plugin separates 44-FZ and 223-FZ and warns against applying 44-FZ "by analogy" where 223-FZ depends on the customer's procurement regulation.
- Marketplace and README include the plugin with the expected source path.
