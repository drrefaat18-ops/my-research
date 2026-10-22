#!/usr/bin/env python3
"""Turn a usage-report line into dollars at list price, for every model in a price table.

Usage:
  python cost.py "12.4k input, 118.0k output, 19.8M cache read, 1.5M cache write" [--prices prices.json]
  python cost.py --selftest

prices.json: {"models": {"<id>": {"input": .., "output": .., "cache_write": .., "cache_read": ..}}}, USD per
million tokens. The first model is the base for ratios. Repricing the same tokens on another model is
arithmetic, not a forecast: models spend different token counts on the same task.
"""
import json
import re
import sys
from pathlib import Path

UNIT = {"": 1, "k": 1_000, "m": 1_000_000, "b": 1_000_000_000}
KINDS = ("input", "output", "cache write", "cache read")


def parse(line):
    """'12.4k input, 1.5M cache write' -> token counts per meter."""
    out = dict.fromkeys(KINDS, 0.0)
    for num, unit, kind in re.findall(r"(\d+(?:\.\d+)?)\s*([kKmMbB]?)\s+(input|output|cache read|cache write)", line):
        out[kind] = float(num) * UNIT[unit.lower()]
    return out


def parts(price, tokens):
    return {k: tokens[k] * price[k.replace(" ", "_")] / 1_000_000 for k in KINDS}


def report(tokens, models):
    base_id = next(iter(models))
    base = sum(parts(models[base_id], tokens).values())
    lines = [f"{'model':<24} {'total':>9}  vs {base_id}"]
    for m, p in models.items():
        d = sum(parts(p, tokens).values())
        ratio = f"{d / base:>5.2f}x" if base else "  n/a"
        lines.append(f"{m:<24} ${d:>8.2f}  {ratio}")
    lines += ["", f"where the {base_id} dollars go:"]
    for kind, d in parts(models[base_id], tokens).items():
        share = f"{d / base:>4.0%}" if base else " n/a"
        lines.append(f"  {kind:<12} ${d:>7.2f}  {share}")
    return "\n".join(lines)


def selftest():
    t = parse("12.4k input, 118.0k output, 19.8M cache read, 1.5M cache write")
    assert t == {"input": 12_400, "output": 118_000, "cache write": 1_500_000, "cache read": 19_800_000}, t
    assert parse("5.7B cache read")["cache read"] == 5_700_000_000  # long-run totals print billions
    # neutral sample prices, not any vendor's
    models = {"model_a": {"input": 3, "output": 15, "cache_write": 3.75, "cache_read": 0.3},
              "model_b": {"input": 1.5, "output": 7.5, "cache_write": 1.875, "cache_read": 0.15}}
    a = sum(parts(models["model_a"], t).values())
    b = sum(parts(models["model_b"], t).values())
    assert abs(a - (0.0372 + 1.77 + 5.625 + 5.94)) < 1e-9, a
    assert abs(b - a / 2) < 1e-9
    out = report(t, models)
    assert "0.50x" in out and "cache write" in out
    assert "n/a" in report(t, {"free": dict.fromkeys(("input", "output", "cache_write", "cache_read"), 0)})
    print(out)
    print("\nselftest OK")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--selftest"]:
        selftest()
        sys.exit(0)
    if not args:
        sys.exit(__doc__)
    prices = Path(args[args.index("--prices") + 1]) if "--prices" in args else Path(__file__).with_name("prices.json")
    print(report(parse(args[0]), json.loads(prices.read_text(encoding="utf-8"))["models"]))
