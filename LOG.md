# Local Log — claude-for-legal-ru

## 2026-07-29 | claude-opus-4-8 | workspace initialized

- Оформлен folder-native Brain-проект: добавлены `BRAIN.md`, `TASKS.md`, `LOG.md`.
- Путь добавлен в `~/.config/brain/dashboard-env` → `BRAIN_DASHBOARD_WORKSPACE_ROOTS`.
- Проект: локализация плагинов `anthropic/claude-for-legal` под право РФ.

## 2026-07-29 | claude-opus-4-8 | local-001 done — эталон dogovornoe-pravo

- Создан форк-marketplace `claude-for-legal-ru` (Apache-2.0, NOTICE).
- Локализован commercial-legal → `dogovornoe-pravo`: 6 скиллов, CLAUDE.md-профиль по ГК РФ,
  .mcp.json без US/UK-коннекторов.
- Переработано существо: ст.15/330/394/401(п.4 умысел ничтожно)/333/450.1/782 ГК; подсудность
  АПК/ГПК; претензионный порядок ч.5 ст.4 АПК; NDA — режим КТ (ФЗ-98 ст.10)/секрет производства
  (ст.1465 ГК); адвокатская тайна (ст.8 ФЗ-63) вместо US work-product; ПД — ст.6 ч.3/ст.18 ч.5 ФЗ-152.
- `claude plugin validate` — passed (1 warning про root CLAUDE.md, ожидаемо: шаблон-профиль).
- Установлен: `dogovornoe-pravo@claude-for-legal-ru`, scope user, ~1k always-on токенов.
- git: commit 29591e5.

## 2026-08-06 | claude-opus-5 | local-004 WIP зафиксирован — personalnye-dannye (ФЗ-152)

Роль: pm (оркестрация). Работа по local-004 сделана ранее, но оставалась вне git.

- Локализован privacy-legal → `personalnye-dannye`: 8 скиллов (use-case-triage, pdn-assessment,
  poruchenie-review, subject-request, reg-gap-analysis, policy-monitor, cold-start-interview,
  customize), CLAUDE.md-профиль по ФЗ-152, `.mcp.json`, `references/currency-watch.md`.
- Покрытие норм подтверждено: ст.6 ч.3 (поручение), ст.9/10/11 (согласие, спецкатегории,
  биометрия), ст.12 (трансграничная передача), ст.14/20/21 (обращения субъекта), ст.18 ч.5
  (локализация БД), ст.18.1 (оценка вреда), ст.22/22.1 (уведомление РКН, ответственное лицо),
  КоАП ст.13.11 (в т. ч. оборотные штрафы, 420-ФЗ), УК ст.272.1, сроки 24/72 ч по инцидентам.
- `claude plugin validate personalnye-dannye` — passed (1 warning про root CLAUDE.md, как у эталона).
- Установлен и enabled: `personalnye-dannye@claude-for-legal-ru`, scope user.
- Скан перед коммитом: секретов и клиентских ПДн в плагинах нет.
- Задача остаётся `[~]`: правовое существо не прошло ревью роли `compliance`. По BRAIN.md
  (Action Gates) финализация без такого ревью требует одобрения пользователя. Заведена local-011.
- git: commit 9bcb1d9 (WIP-фиксация; задача не принята).

### Открытый ADR: политика scope при локализации

Плагины форка локализованы с разной полнотой относительно апстрима: `dogovornoe-pravo` — 6 из 12
скиллов commercial-legal (не перенесены amendment-history, matter-workspace, renewal-tracker,
review-proposals, saas-msa-review, stakeholder-summary); `personalnye-dannye` — 8 из 9 скиллов
privacy-legal (не перенесён matter-workspace). Решение не зафиксировано, владелец —
пользователь. Заведена local-012. → Закрыто ADR-002 ниже.

## 2026-08-06 | claude-opus-5 (роль architect) | local-012 done — ADR-002: политика scope

### ADR-002: Scope плагина = core (правовое существо РФ) + дешёвая generic-обвязка

**Status:** Accepted · **Date:** 2026-08-06

**Context.** `dogovornoe-pravo` — 6 из 12 скиллов commercial-legal (убрана вся generic-обвязка
и правовой скилл saas-msa-review); `personalnye-dannye` — 8 из 9 privacy-legal (оставлен
generic-tracker policy-monitor, убран matter-workspace). Критерий отбора не был зафиксирован:
у двух готовых плагинов асимметричные наборы функций одного класса, а пять плагинов в очереди
(corporate/employment/ip/regulatory/litigation) не имели правила для планирования scope.

**Decision.** Каждый апстрим-скилл классифицируется до начала локализации:
- **(a) правовое существо** — требует переработки под нормы РФ; переносится всегда.
- **(b) generic-обвязка** — механика без правовой специфики (workspace, трекеры, форматирование
  summary); переносится, если стоимость ≈0.5–1 сессия и функция востребована соло/малой практикой.
- **(c) неприменимо в РФ** — опирается на институт, которого нет в праве/процессе РФ; не переносится
  и не публикуется под видом РФ-скилла.

Полный паритет с апстримом не требуется. Правило внесено в `BRAIN.md` → Agent Rules.

**Класс (c) по инвентаризации 7 апстрим-плагинов:** takedown (DMCA §512 — в РФ ст. 15.7 ФЗ-149,
иная модель), deposition-prep, subpoena-triage (в РФ доказательства истребует суд — ст. 66 АПК,
ст. 57 ГПК), privilege-log-review (нет широкого discovery), leave-tracker/log-leave (FMLA),
expansion-* (EOR-модель найма за рубежом от лица US-компании), comments (NPRM по APA США),
ai-tool-handoff (Luminance/Kira — enterprise-инструменты).

**Alternatives considered.** Полный паритет — отвергнут: класс (c) юридически ложен при дословном
переносе, а переработка не окупается. Core-only (лишь класс a) — отвергнут: исключает дешёвую,
но нужную инфраструктуру (matter-workspace, chronology, portfolio-status).

**Consequences.** (+) Единый критерий на 5 плагинов очереди; исключён псевдо-РФ-скилл на
нероссийском институте. (−) Граница a/b/c субъективна на смешанных случаях (legal-hold,
claim-chart, entity-compliance, matter-intake); оценка «дешёвых» (b) может расти при вскрытии
скрытой правовой специфики (напр. конфликт-чек в matter-intake упирается в этику — ст. 13 КПЭА);
класс (c) требует пересмотра при изменении права РФ.

**Follow-up.** Заведены local-013 (добор `dogovornoe-pravo`: saas-msa-review + 4 generic-скилла,
3–5 сессий) и local-014 (`matter-workspace` — один общий модуль форка вместо 7 копий).
`review-proposals` не добирается: нефункционален без непортированного агента `playbook-monitor` —
вынесен в «Отложено».
