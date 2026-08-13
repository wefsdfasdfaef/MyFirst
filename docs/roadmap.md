# Roadmap

The roadmap is ordered around a stable, reviewable core. Each feature should include tests, documentation, an example, and a clear compatibility note before it is considered complete.

## 0.1 — Core quality checks — released

CSV input, required/unique/regex/range rules, JSON and HTML reports, CLI execution, tests, CI, and environmental monitoring examples.

## 0.2 — Quality-gate usability

- Publish versioned packages and document installation and upgrade behavior.
- Add date-format, enumeration, cross-column, severity, and summary-metric rules.
- Improve diagnostics for missing columns, malformed rules, and large inputs.

## 0.3 — Data-source and scale options

- Explore database adapters behind optional dependencies.
- Add streaming behavior for large CSV files with documented memory guarantees.
- Provide reusable rule packs and scheduled-execution examples.

## 0.4 — Optional assisted rule authoring

Explore optional generation and explanation of quality rules from metadata and sample data. Any assisted feature must produce reviewable deterministic rules, remain opt-in, and never execute generated rules without user approval.
