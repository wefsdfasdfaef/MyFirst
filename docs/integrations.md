# Integrations

## GitHub Actions quality gate

After `open-data-quality` is published to PyPI, copy [examples/quality-gate.yml](../examples/quality-gate.yml) to a downstream repository and adjust the data and rules paths. The example pins the package version, fails the workflow when a rule fails, and uploads JSON and HTML reports for review.

Use a pinned package version in production so a data pipeline does not change behavior without a deliberate upgrade:

```yaml
- name: Install Open Data Quality
  run: python -m pip install open-data-quality==0.1.1
```

The command's exit status is part of the integration contract:

- `0`: all configured checks passed;
- `1`: at least one configured check failed;
- another nonzero status: the command could not complete, for example because an input file or rule file was invalid.

Reports contain rule results and sampled row numbers. Do not upload source data or reports containing sensitive information to a public artifact store.
