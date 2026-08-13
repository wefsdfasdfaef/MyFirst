"""Open Data Quality public API."""

from .core import check_rows, load_csv, run_quality_checks
from .reporting import render_html

__all__ = ["check_rows", "load_csv", "render_html", "run_quality_checks"]
__version__ = "0.1.0"
