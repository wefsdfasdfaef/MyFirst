# Open Data Quality

[![CI](https://github.com/wefsdfasdfaef/open-data-quality/actions/workflows/ci.yml/badge.svg)](https://github.com/wefsdfasdfaef/open-data-quality/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Auditable, configuration-driven quality gates for CSV data delivery and CI workflows.

## Why this project

Data-quality failures are often discovered after data has been delivered, loaded into a platform, or used in analysis. Open Data Quality keeps the rule definition, validation result, and exit status reproducible so a data pipeline can stop on a failed quality gate and retain a reviewable report.

```text
CSV export -> JSON rules -> quality checks -> JSON / HTML report
                                      |
                                      +-> exit 0 when all checks pass
                                      +-> exit 1 when any check fails
```

## Current capabilities

- Required-value, uniqueness, regular-expression, and numeric-range checks
- JSON reports for machines and self-contained HTML reports for reviewers
- A small command-line interface with no runtime dependencies outside Python's standard library
- Deterministic, CI-friendly execution
- Examples for general data delivery and environmental monitoring records

The current input format is CSV. Database adapters, streaming for large files, and optional AI-assisted rule suggestions remain roadmap items; the core command does not connect to external systems or call an AI service.

## Install

After the v0.1.1 release is published to PyPI, install the pinned package:

```bash
python -m pip install open-data-quality==0.1.1
```

Until then, install the project from source:

```bash
python -m pip install -e .
```

The package requires Python 3.10 or newer. A release workflow and packaging checks are included in [docs/release.md](docs/release.md).

## Quick start

Run a quality gate and print the JSON report:

```bash
open-data-quality examples/valid_sample.csv --rules examples/rules.json
```

Write both machine-readable and reviewer-friendly reports:

```bash
open-data-quality \
  examples/valid_sample.csv \
  --rules examples/rules.json \
  --output quality-report.json \
  --html-report quality-report.html
```

`examples/sample.csv` intentionally contains invalid rows so it can be used to inspect failures. The command exits with status `1` when a rule fails, which makes it suitable for a CI quality gate.

## Rule format

Rules are stored in a JSON object with a `rules` array:

```json
{
  "rules": [
    {"type": "required", "column": "name"},
    {"type": "unique", "column": "id"},
    {"type": "range", "column": "age", "min": 0, "max": 120},
    {"type": "regex", "column": "email", "pattern": "^[^@]+@[^@]+\\.[^@]+$"}
  ]
}
```

Each result records the rule, pass/fail status, failed-row count, and a bounded sample of failed row numbers. Empty values can be handled separately with a `required` rule.

## Examples

The environmental monitoring example checks station identifiers, record uniqueness, PM2.5 values, and temperature ranges:

```bash
open-data-quality \
  examples/environment_monitoring_sample.csv \
  --rules examples/environment_monitoring_rules.json \
  --html-report environmental-quality.html
```

## CI usage

The repository's CI runs the test suite on Python 3.10–3.13, builds an sdist and wheel, installs the wheel into a clean virtual environment, and runs a command-line smoke test. A downstream workflow can use the same command and fail its job when the quality gate returns status `1`.

For a non-confidential CSV workflow, see [the early feedback request](https://github.com/wefsdfasdfaef/open-data-quality/issues/28) for the trial steps and privacy boundary.

## Contributing and maintenance

See [docs/integrations.md](docs/integrations.md) for a downstream GitHub Actions example, [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and pull-request expectations, [SECURITY.md](SECURITY.md) for vulnerability reports, [docs/release.md](docs/release.md) for releases, and [docs/roadmap.md](docs/roadmap.md) for planned work.

## License

Apache License 2.0. See [LICENSE](LICENSE).
