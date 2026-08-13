"""Core data-quality checks using only the Python standard library."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Iterable


def load_csv(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_rules(path: str | Path) -> list[dict[str, Any]]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("rules file must contain a JSON object")
    rules = data.get("rules")
    if not isinstance(rules, list):
        raise ValueError("rules file must contain a 'rules' array")
    if any(not isinstance(rule, dict) for rule in rules):
        raise ValueError("every item in 'rules' must be an object")
    return rules


def _required(rows: list[dict[str, str]], column: str) -> list[int]:
    return [i for i, row in enumerate(rows, 1) if not str(row.get(column, "")).strip()]


def _unique(rows: list[dict[str, str]], column: str) -> list[int]:
    seen: set[str] = set()
    failed: list[int] = []
    for i, row in enumerate(rows, 1):
        value = str(row.get(column, ""))
        if value in seen:
            failed.append(i)
        else:
            seen.add(value)
    return failed


def _regex(rows: list[dict[str, str]], column: str, pattern: str) -> list[int]:
    compiled = re.compile(pattern)
    return [i for i, row in enumerate(rows, 1) if row.get(column, "") and not compiled.fullmatch(str(row[column]))]


def _range(rows: list[dict[str, str]], column: str, minimum: float | None, maximum: float | None) -> list[int]:
    try:
        lower = float(minimum) if minimum is not None else None
        upper = float(maximum) if maximum is not None else None
    except (TypeError, ValueError) as exc:
        raise ValueError("range rule bounds must be numeric") from exc
    if lower is not None and upper is not None and lower > upper:
        raise ValueError("range rule minimum cannot exceed maximum")

    failed: list[int] = []
    for i, row in enumerate(rows, 1):
        value = row.get(column, "")
        if value in ("", None):
            continue
        try:
            number = float(value)
        except (TypeError, ValueError):
            failed.append(i)
            continue
        if lower is not None and number < lower:
            failed.append(i)
        elif upper is not None and number > upper:
            failed.append(i)
    return failed


def check_rows(rows: Iterable[dict[str, str]], rules: list[dict[str, Any]]) -> dict[str, Any]:
    materialized = list(rows)
    results: list[dict[str, Any]] = []

    for rule in rules:
        kind = rule.get("type")
        column = rule.get("column")
        if not column:
            raise ValueError("every rule requires a column")

        if kind == "required":
            failed_rows = _required(materialized, column)
        elif kind == "unique":
            failed_rows = _unique(materialized, column)
        elif kind == "regex":
            failed_rows = _regex(materialized, column, rule["pattern"])
        elif kind == "range":
            failed_rows = _range(materialized, column, rule.get("min"), rule.get("max"))
        else:
            raise ValueError(f"unsupported rule type: {kind}")

        results.append({
            "rule": rule,
            "passed": not failed_rows,
            "failed_count": len(failed_rows),
            "failed_rows": failed_rows[:20],
        })

    passed = sum(1 for result in results if result["passed"])
    total = len(results)
    return {
        "rows": len(materialized),
        "checks": total,
        "passed": passed,
        "failed": total - passed,
        "score": round((passed / total * 100) if total else 100.0, 2),
        "results": results,
    }


def run_quality_checks(csv_path: str | Path, rules_path: str | Path) -> dict[str, Any]:
    return check_rows(load_csv(csv_path), load_rules(rules_path))
