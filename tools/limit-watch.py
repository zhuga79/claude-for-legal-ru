#!/usr/bin/env python3
"""Расход токенов за скользящее окно — по транскриптам Claude Code.

Claude Code пишет usage по каждому запросу в ~/.claude/projects/<...>/<session>.jsonl.
Скрипт суммирует их за последние N часов по всем сессиям, включая подагентов.

Точного порога лимита скрипт не знает — он зависит от тарифа и не отдаётся наружу.
Порог калибруется: когда в сессии виден процент (/usage), запусти скрипт и впиши
пару «процент → billable» в CALIBRATION ниже. После двух точек оценка становится
линейной и пригодной для «стоп на 90%».

Использование:
    python3 tools/limit-watch.py            # окно 5 часов
    python3 tools/limit-watch.py --hours 1
    python3 tools/limit-watch.py --json
"""
import argparse
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECTS = Path.home() / ".claude" / "projects"

# Калибровка: [(процент, показанный в /usage, billable-токены на тот момент), ...]
# Точка (0, 0) — начало окна. Точка 2026-08-08: /usage показал 31% при 5 820 917 billable.
CALIBRATION: list[tuple[float, int]] = [(0.0, 0), (31.0, 5_820_917)]

# Порог, на котором нужно останавливаться (решение владельца 2026-08-08).
STOP_PCT = 90.0


def collect(hours: float) -> dict:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    totals = {
        "input": 0,
        "output": 0,
        "cache_creation": 0,
        "cache_read": 0,
        "requests": 0,
    }
    by_session: dict[str, int] = {}
    if not PROJECTS.exists():
        return {"totals": totals, "by_session": by_session, "error": "нет ~/.claude/projects"}

    for path in PROJECTS.rglob("*.jsonl"):
        try:
            if datetime.fromtimestamp(path.stat().st_mtime, timezone.utc) < cutoff:
                continue  # файл не трогали в окне — пропускаем целиком
        except OSError:
            continue
        session_billable = 0
        try:
            with path.open(encoding="utf-8") as fh:
                for line in fh:
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    usage = (rec.get("message") or {}).get("usage")
                    ts = rec.get("timestamp")
                    if not usage or not ts:
                        continue
                    try:
                        when = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    except ValueError:
                        continue
                    if when < cutoff:
                        continue
                    totals["requests"] += 1
                    totals["input"] += usage.get("input_tokens", 0)
                    totals["output"] += usage.get("output_tokens", 0)
                    totals["cache_creation"] += usage.get("cache_creation_input_tokens", 0)
                    totals["cache_read"] += usage.get("cache_read_input_tokens", 0)
                    session_billable += (
                        usage.get("input_tokens", 0)
                        + usage.get("output_tokens", 0)
                        + usage.get("cache_creation_input_tokens", 0)
                    )
        except OSError:
            continue
        if session_billable:
            by_session[path.stem[:8]] = session_billable

    return {"totals": totals, "by_session": by_session}


def billable(totals: dict) -> int:
    """Кэш-чтение считается по льготной ставке, поэтому в основную сумму не входит."""
    return totals["input"] + totals["output"] + totals["cache_creation"]


def estimate_pct(value: int) -> str:
    if len(CALIBRATION) < 2:
        return "порог не откалиброван — впиши две точки в CALIBRATION"
    (p1, v1), (p2, v2) = sorted(CALIBRATION)[:2]
    if v2 == v1:
        return "калибровочные точки совпали"
    rate = (p2 - p1) / (v2 - v1)
    return f"≈{p1 + (value - v1) * rate:.0f}% лимита"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=5.0)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    data = collect(args.hours)
    t = data["totals"]
    b = billable(t)

    if args.json:
        print(json.dumps({**data, "billable": b}, ensure_ascii=False))
        return

    print(f"Окно: последние {args.hours:g} ч · запросов: {t['requests']}")
    print(f"  ввод:            {t['input']:>12,}".replace(",", " "))
    print(f"  вывод:           {t['output']:>12,}".replace(",", " "))
    print(f"  запись кэша:     {t['cache_creation']:>12,}".replace(",", " "))
    print(f"  чтение кэша:     {t['cache_read']:>12,}".replace(",", " "))
    print(f"  ИТОГО billable:  {b:>12,}".replace(",", " "), f"({estimate_pct(b)})")

    if len(CALIBRATION) >= 2:
        (p1, v1), (p2, v2) = sorted(CALIBRATION)[:2]
        if p2 != p1:
            per_pct = (v2 - v1) / (p2 - p1)
            stop_at = int(v1 + (STOP_PCT - p1) * per_pct)
            left = stop_at - b
            print(f"\n  порог {STOP_PCT:.0f}%:   {stop_at:>12,}".replace(",", " "))
            if left > 0:
                print(f"  запас:           {left:>12,}".replace(",", " "),
                      f"≈ {left / per_pct:.0f} процентных пунктов")
            else:
                print("  ⛔ ПОРОГ ПРОЙДЕН — останавливаться")
    if data["by_session"]:
        print("\nПо сессиям (топ-5):")
        for sid, val in sorted(data["by_session"].items(), key=lambda kv: -kv[1])[:5]:
            print(f"  {sid}  {val:>12,}".replace(",", " "))


if __name__ == "__main__":
    main()
