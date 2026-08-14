#!/usr/bin/env bash
# Ставит git-хуки проекта. Запускать один раз после клонирования:
#   ./tools/install-hooks.sh
#
# Хуки не versioned-объекты git: .git/hooks не клонируется, поэтому шаг ручной.

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

for hook in pre-commit; do
  src="tools/$hook"
  dst=".git/hooks/$hook"
  [ -f "$src" ] || { echo "нет $src — пропускаю"; continue; }
  if [ -e "$dst" ] && ! [ -L "$dst" ]; then
    echo "уже есть свой $dst — не трогаю; перенесите вручную"
    continue
  fi
  ln -sf "../../$src" "$dst"
  chmod +x "$src"
  echo "установлен: $dst → $src"
done

echo
echo "Проверка на ПД использует brain-guard, если он есть в PATH, иначе встроенный python-фолбэк."
command -v brain-guard >/dev/null 2>&1 \
  && echo "brain-guard: найден" \
  || echo "brain-guard: не найден — работает запасная проверка (только обезличенные признаки)"
