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
