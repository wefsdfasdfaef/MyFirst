import unittest

from open_data_quality.reporting import render_html


class ReportingTest(unittest.TestCase):
    def test_render_html_contains_summary(self):
        html = render_html({
            "rows": 10,
            "checks": 2,
            "passed": 1,
            "failed": 1,
            "score": 50,
            "results": [
                {
                    "rule": {"type": "required", "column": "site_id"},
                    "passed": False,
                    "failed_count": 2,
                    "failed_rows": [3, 5],
                }
            ],
        })
        self.assertIn("Open Data Quality Report", html)
        self.assertIn("site_id", html)
        self.assertIn("50.00%", html)


if __name__ == "__main__":
    unittest.main()
