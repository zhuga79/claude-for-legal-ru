# Review: local-035 gap-fill skills

Reviewer: codex-gpt-5, 2026-08-27.

## Verdict

PASS_WITH_WARNINGS.

## Scope

- `regulyatornyj-monitoring/skills/poisk-probelov/SKILL.md`
- `regulyatornyj-monitoring/skills/pererabotka-politiki/SKILL.md`
- `trudovoe-pravo/skills/otvet-gosinspekcii-truda/SKILL.md`

## Findings

- No blocking packaging issue: `claude plugin validate regulyatornyj-monitoring` and `claude plugin validate trudovoe-pravo` pass with the known root `CLAUDE.md` warning.
- The two regulatory-monitoring skills are complementary, not duplicates: `poisk-probelov` selects affected LNA across the portfolio, `policy-diff` checks a selected document, and `pererabotka-politiki` drafts a redline only after a confirmed discrepancy.
- The GIT skill is correctly separated from internal employer investigations and has criminal stop-triggers.

## Integration decision

Include all three skills in the current release. They are not left as untracked drafts. README and marketplace descriptions were updated to include them.

## Warnings

- GIT inspection deadlines and moratorium exceptions require current primary-source checks before use in a real matter.
- `pererabotka-politiki` must not be used as a first-step gap finder; it requires input from `policy-diff` or `poisk-probelov`.
