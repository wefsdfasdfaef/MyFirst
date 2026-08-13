"""Command-line interface for Open Data Quality."""

from __future__ import annotations

import argparse
import json

from . import __version__
from .core import run_quality_checks
from .reporting import render_html


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run data quality checks against a CSV file")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("csv", help="CSV file to validate")
    parser.add_argument("--rules", required=True, help="JSON rules file")
    parser.add_argument("--output", help="Optional path for the JSON report")
    parser.add_argument("--html-report", help="Optional path for an HTML report")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    report = run_quality_checks(args.csv, args.rules)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered + "\n")

    if args.html_report:
        with open(args.html_report, "w", encoding="utf-8") as handle:
            handle.write(render_html(report))

    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
