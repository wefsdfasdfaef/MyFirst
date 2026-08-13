# Open Data Quality

A lightweight, configuration-driven data quality toolkit for CSV datasets. It is designed for data governance teams that need auditable, repeatable checks without deploying a heavy platform.

## Features

- Completeness checks for required columns
- Uniqueness checks
- Regex validation
- Numeric range validation
- JSON quality reports with row-level issue samples
- Command-line interface
- Zero runtime dependencies

## Quick start

```bash
python -m open_data_quality.cli examples/sample.csv --rules examples/rules.json
```

Example output:

```json
{
  "rows": 5,
  "checks": 4,
  "passed": 3,
  "failed": 1,
  "score": 75.0
}
```

## Install for development

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Rule format

```json
{
  "rules": [
    {"type": "required", "column": "name"},
    {"type": "unique", "column": "id"},
    {"type": "regex", "column": "email", "pattern": "^[^@]+@[^@]+\\.[^@]+$"},
    {"type": "range", "column": "age", "min": 0, "max": 120}
  ]
}
```

## Why this project

Many data-governance projects need a small quality gate that can run in CI, scheduled jobs, data delivery pipelines, or local audits. Open Data Quality focuses on transparent rules and machine-readable results so it can be embedded into larger governance platforms.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache License 2.0.
