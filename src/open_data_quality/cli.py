"""Command-line interface for Open Data Quality."""

from __future__ import annotations

import argparse
import json

from .core import run_quality_checks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run data quality checks against a CSV file")
    parser.add_argument("csv", help="CSV file to validate")
    parser.add_argument("--rules", required=True, help="JSON rules file")
    parser.add_argument("--output", help="Optional path for the JSON report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report = run_quality_checks(args.csv, args.rules)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered + "\n")
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
