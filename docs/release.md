# Release guide

This document keeps releases reproducible for maintainers and downstream users.

## Local verification

From a clean checkout:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python -m pip install build
python -m build
```

The `dist/` directory should contain one source archive and one wheel. Install the wheel into a clean virtual environment and run both a passing and a failing example before publishing.

## Version and GitHub release

1. Update the version in `pyproject.toml` and `src/open_data_quality/__init__.py`.
2. Add a dated section to [CHANGELOG.md](../CHANGELOG.md).
3. Run the local checks above and review the generated archive contents.
4. Merge the release pull request into `main`.
5. Create a tag such as `v0.2.0` and a GitHub Release using the changelog entry.

## PyPI publishing

The repository includes a GitHub Actions workflow for publishing a GitHub Release to PyPI through trusted publishing. Before the first release, the maintainer must create or claim the `open-data-quality` project on PyPI and configure its trusted publisher for this repository and the `Publish package` workflow. The workflow uses the `pypi` environment and OIDC; no long-lived PyPI token should be committed to GitHub.

After publishing, verify:

```bash
python -m pip install --upgrade open-data-quality
open-data-quality --version
```

Record the published version and any installation or compatibility notes in the release description.
