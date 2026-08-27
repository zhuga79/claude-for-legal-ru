# Review: protivodejstvie-otmyvaniyu

Reviewer: codex-gpt-5, cross-provider review, 2026-08-27.

## Verdict

PASS_WITH_WARNINGS after fixes.

## Critical

- No open critical issues.

## High

- Fixed during this review: freezing/blocking deadline for listed terrorism/extremism/WMD persons was still described as "1 working day". Current 115-FZ wording uses immediate action, not later than 24 hours, and separate notification of Rosfinmonitoring not later than the next working day. Fixed in `protivodejstvie-otmyvaniyu/CLAUDE.md:13`, `protivodejstvie-otmyvaniyu/CLAUDE.md:112`, `protivodejstvie-otmyvaniyu/skills/proverka-sanktsionnyh-spiskov/SKILL.md:55`, `protivodejstvie-otmyvaniyu/skills/soobschenie-v-rosfinmonitoring/SKILL.md:70`.

## Medium

- No open medium packaging issues found after `claude plugin validate protivodejstvie-otmyvaniyu`.

## Low

- Several source-history comments still mention the old "1 working day for suspicious operations" as a historical upstream error. That is acceptable because the operational instructions now state 3 working days for suspicious-operation reporting and 24 hours for freezing.

## Suspect / needs primary-source check

- `protivodejstvie-otmyvaniyu/skills/pravila-vnutrennego-kontrolya/SKILL.md:65` and `:67` still leave 706-П/681-П for non-credit organizations as `[проверить]`; do not treat these as confirmed.
- FES format codes and quarterly FES 3-FM should be checked against the current Rosfinmonitoring/CBR format before producing a filing plan.

## Confirmed good

- The plugin separates compliance work from lawyer/tax-advisor roles.
- Tipping-off guardrail is present in root profile and FES workflow.
- Suspicious-operation and mandatory-control reporting are consistently routed as 3 working days after the latest fix.
