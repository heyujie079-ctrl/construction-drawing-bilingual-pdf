#!/usr/bin/env python3
"""Convert millimetres to whole inches using decimal half-up rounding."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


MM_PER_INCH = Decimal("25.4")


def convert(value: str) -> tuple[Decimal, int]:
    try:
        millimetres = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid millimetre value: {value}") from exc
    inches = (millimetres / MM_PER_INCH).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return millimetres, int(inches)


def format_decimal(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert one or more millimetre values to rounded whole inches."
    )
    parser.add_argument("values", nargs="+", help="Millimetre values to convert")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    results = []
    for raw in args.values:
        millimetres, inches = convert(raw)
        results.append(
            {
                "millimetres": format_decimal(millimetres),
                "inches": inches,
                "label": f"{inches} inch",
            }
        )

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(f"{item['millimetres']} mm -> {item['label']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
