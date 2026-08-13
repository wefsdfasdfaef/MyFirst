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

    def test_render_html_escapes_title_and_columns(self):
        html = render_html({
            "rows": 1,
            "checks": 1,
            "passed": 1,
            "failed": 0,
            "score": 100,
            "results": [{
                "rule": {"type": "required", "column": "<script>"},
                "passed": True,
                "failed_count": 0,
                "failed_rows": [],
            }],
        }, title="<Quality Report>")
        self.assertIn("&lt;Quality Report&gt;", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn("<script>", html)
        self.assertIn("Failed count", html)


if __name__ == "__main__":
    unittest.main()
