# Local Tasks — claude-for-legal-ru

Локальная очередь проекта локализации. Формат Brain. Каждая задача — один плагин
или follow-up. Правовое существо — по нормам РФ; спорное помечать `[проверить]`.

- [x] [P1] local-001 — Эталон: локализовать commercial-legal → `dogovornoe-pravo` (ГК РФ, ФЗ-98)
      role: developer
      acceptance: Плагин установлен, `claude plugin validate` проходит; 6 скиллов (review, vendor-agreement-review, nda-review, escalation-flagger, customize, cold-start-interview); CLAUDE.md-профиль по ГК РФ; .mcp.json без US/UK-коннекторов; LICENSE+NOTICE. Готово.

- [ ] [P1] local-002 — Ревью правового существа `dogovornoe-pravo` ролью lawyer
      role: lawyer   mode: solo
      acceptance: Проверены нормы и квалификации в скиллах (ст. 15/330/394/401/333/450.1/782 ГК, подсудность АПК/ГПК, претензионный порядок ч.5 ст.4 АПК, ФЗ-98/ст.1465, адвокатская тайна ст.8 ФЗ-63); ошибки/пробелы исправлены; спорное помечено `[проверить]`.

- [ ] [P1] local-003 — Тест cold-start на реальном договоре
      role: developer   mode: solo
      acceptance: Прогон `/dogovornoe-pravo:cold-start-interview` + `/dogovornoe-pravo:review` на обезличенном договоре; выявленные дефекты скиллов зафиксированы в LOG.md и исправлены.

- [~] [P1] local-004 — Локализовать privacy-legal → «Персональные данные (ФЗ-152)»
      role: developer   mode: solo
      acceptance: Плагин `personalnye-dannye`: DPIA→оценка вреда/ПДн, поручение на обработку (ст.6 ч.3 ФЗ-152), локализация БД в РФ (ст.18 ч.5), уведомление РКН, DSAR→обращение субъекта ПДн (ст.14 ФЗ-152), трансграничная передача (ст.12). US/EU GDPR-существо заменено на ФЗ-152. validate проходит.

- [ ] [P1] local-011 — Ревью правового существа `personalnye-dannye` ролью compliance
      role: compliance   mode: solo
      контекст: плагин собран и установлен (enabled, user scope), но правовое существо не
      проверено; по BRAIN.md → Action Gates финализация без ревью требует одобрения. Блокирует
      закрытие local-004.
      acceptance: Проверены нормы и квалификации в 8 скиллах (ст.6 ч.3, ст.9/10/11, ст.12,
      ст.14/20/21, ст.18 ч.5, ст.18.1, ст.22/22.1 ФЗ-152; КоАП 13.11; УК 272.1; сроки 24/72 ч);
      сверены пункты `references/currency-watch.md` с первоисточниками; ошибки исправлены;
      спорное помечено `[проверить]`.

- [ ] [P1] local-012 — Решение: политика scope при локализации плагинов + ADR
      role: architect   mode: solo
      контекст: `dogovornoe-pravo` — 6 из 12 скиллов апстрима, `personalnye-dannye` — 8 из 9.
      Правило не зафиксировано, из-за чего каждый следующий плагин решает заново.
      acceptance: Выбрана политика (полный паритет с апстримом / core subset по правовому
      существу); решение записано ADR в `LOG.md` и правилом в `BRAIN.md` → Agent Rules; при
      выборе паритета заведены задачи на добор скиллов `dogovornoe-pravo`.

- [ ] [P1] local-005 — Оценить litigation-legal → плагин «Доследственная проверка / защита (УПК РФ)»
      role: architect   mode: council   council: [architect, lawyer]
      acceptance: Решение — локализация litigation или НОВЫЙ плагин под уголовную защиту РФ (ст.159.5 УК, доследственная проверка, УПК); зафиксирован scope, список скиллов, применимость docket-watcher/CourtListener (в РФ — kad.arbitr/ГАС «Правосудие»). ADR в LOG.md.

- [ ] [P2] local-006 — Локализовать corporate-legal → «Корпоративное право / M&A (РФ)»
      role: developer   mode: solo
      acceptance: Плагин: due diligence по ЕГРЮЛ, ФЗ-14 (ООО)/ФЗ-208 (АО), протоколы ОСУ/совета, closing checklist, tabular-review под РФ-реестры. US reps&warranties заменены на заверения об обстоятельствах (ст.431.2 ГК). validate проходит.

- [ ] [P2] local-007 — Локализовать employment-legal → «Трудовое право (ТК РФ)»
      role: developer   mode: solo
      acceptance: Плагин под ТК РФ: приём/увольнение (ст.77–84.1), основания расторжения, ЛНА, служебные проверки, классификация «самозанятый/ГПХ vs трудовой» (риск переквалификации, ст.19.1 ТК). US at-will/штатные тесты удалены. validate проходит.

- [ ] [P2] local-008 — Локализовать ip-legal → «Интеллектуальная собственность (часть 4 ГК)»
      role: developer   mode: solo
      acceptance: Плагин: товарные знаки (Роспатент), клиренс, служебные РИД (ст.1370), лицензии/отчуждение (ст.1234/1235), претензии о нарушении, домены. USPTO/US IP заменены на Роспатент/ч.4 ГК. validate проходит.

- [ ] [P3] local-009 — Локализовать regulatory-legal → «Регуляторный мониторинг (РФ)»
      role: developer   mode: solo
      acceptance: Плагин: мониторинг НПА (regulation.gov.ru, pravo.gov.ru), диффы против политик, сроки публичного обсуждения. validate проходит.

- [ ] [P3] local-010 — README.md форка + шаблон company-profile.md
      role: developer   mode: solo
      acceptance: README (назначение, установка `claude plugin marketplace add`, дисклеймер, атрибуция); `company-profile.md` шаблон, общий для плагинов форка (ОПФ, режим налогообложения, юрисдикция, ПД).

## Отложено / под вопрос

- product-legal, ai-governance-legal, law-student, legal-clinic, legal-builder-hub,
  cocounsel-legal — локализовать по необходимости; часть слабо ложится на РФ
  (юрклиники/law-school под US) или требует отдельного решения о scope.
