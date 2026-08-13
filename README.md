# Open Data Quality

A lightweight, configuration-driven data quality toolkit for CSV datasets. It provides auditable quality checks for data governance workflows.

## Features

- Completeness checks for required columns
- Uniqueness checks
- Regex validation
- Numeric range validation
- JSON quality reports
- Self-contained HTML quality reports
- Command-line interface
- CI-friendly execution

## Quick start

```bash
python -m open_data_quality.cli examples/sample.csv --rules examples/rules.json
```

Generate an HTML report:

```bash
python -m open_data_quality.cli examples/sample.csv --rules examples/rules.json --html-report report.html
```

## Environmental monitoring example

The project includes a governance example for environmental monitoring datasets:

- monitoring station identifiers
- record uniqueness
- PM2.5 value validation
- temperature range validation

Example rules:

```bash
examples/environment_monitoring_rules.json
```

## Why this project

Open Data Quality targets practical governance scenarios where teams need transparent rules, repeatable checks, and machine-readable quality results that can integrate with larger data platforms.

## Development

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## License

Apache License 2.0.
