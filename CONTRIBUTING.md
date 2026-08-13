# Contributing

Thank you for considering a contribution. The project is intentionally small: a focused change with a reproducible example is easier to review and maintain.

## Development setup

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python -m pip install build
python -m build
```

Python 3.10–3.13 are covered by CI. Runtime code should continue to use the standard library unless a dependency has a clear project-level benefit.

## Issues and pull requests

For a bug, include the smallest CSV/rules example that reproduces it, the expected result, the observed result, and the project version. For a feature, describe the data-quality problem, the intended rule or report behavior, compatibility considerations, and how a maintainer can validate it.

Pull requests should:

- keep one problem or feature per change;
- add or update tests for behavior changes;
- update the README, roadmap, or changelog when user-visible behavior changes;
- avoid real personal, confidential, or production data in examples;
- include the exact validation commands in the pull-request description.

The default branch should remain installable and testable after every merge. See [docs/release.md](docs/release.md) for the release process.
