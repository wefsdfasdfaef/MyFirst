# Open Data Quality

A lightweight, configuration-driven data quality toolkit for CSV datasets. It provides auditable quality checks for data governance workflows.

## Overview

Open Data Quality is designed for data governance teams that need transparent, repeatable validation before data delivery, analysis, or platform ingestion.

Typical workflow:

```
CSV / Data Export
        |
        v
Quality Rules (JSON)
        |
        v
Open Data Quality Engine
        |
        +--> JSON Report
        |
        +--> HTML Report
```

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

The project includes a governance example based on environmental monitoring data:

- monitoring station identifiers
- record uniqueness
- PM2.5 value validation
- temperature range validation

Example files:

```text
examples/environment_monitoring_sample.csv
examples/environment_monitoring_rules.json
```

## Use cases

- Data governance quality gates
- Data delivery validation
- ETL pipeline checks
- Public-sector and enterprise data audits

## Development

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## License

Apache License 2.0.
