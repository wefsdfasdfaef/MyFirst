import unittest

from open_data_quality.core import check_rows
from open_data_quality.reporting import render_html


class QualityChecksTest(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"id": "1", "name": "Alice", "age": "30", "email": "alice@example.com"},
            {"id": "2", "name": "", "age": "130", "email": "invalid"},
            {"id": "2", "name": "Bob", "age": "20", "email": "bob@example.com"},
        ]

    def test_required(self):
        report = check_rows(self.rows, [{"type": "required", "column": "name"}])
        self.assertEqual(report["failed"], 1)
        self.assertEqual(report["results"][0]["failed_rows"], [2])

    def test_unique(self):
        report = check_rows(self.rows, [{"type": "unique", "column": "id"}])
        self.assertEqual(report["results"][0]["failed_rows"], [3])

    def test_range(self):
        report = check_rows(self.rows, [{"type": "range", "column": "age", "min": 0, "max": 120}])
        self.assertEqual(report["results"][0]["failed_rows"], [2])

    def test_regex(self):
        report = check_rows(self.rows, [{"type": "regex", "column": "email", "pattern": r"^[^@]+@[^@]+\.[^@]+$"}])
        self.assertEqual(report["results"][0]["failed_rows"], [2])

    def test_html_report(self):
        html = render_html({"rows": 3, "checks": 1, "passed": 1, "failed": 0, "score": 100, "results": []})
        self.assertIn("Open Data Quality Report", html)
        self.assertIn("100.00%", html)


if __name__ == "__main__":
    unittest.main()
