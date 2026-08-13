import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from open_data_quality import __version__
from open_data_quality.cli import build_parser, main


class CliTest(unittest.TestCase):
    def _write_inputs(self, directory: Path, csv_text: str, rules: dict) -> tuple[Path, Path]:
        csv_path = directory / "data.csv"
        rules_path = directory / "rules.json"
        csv_path.write_text(csv_text, encoding="utf-8")
        rules_path.write_text(json.dumps(rules), encoding="utf-8")
        return csv_path, rules_path

    def test_version_flag(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            with self.assertRaises(SystemExit) as result:
                build_parser().parse_args(["--version"])
        self.assertEqual(result.exception.code, 0)
        self.assertIn(__version__, output.getvalue())

    def test_successful_run_writes_reports(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            csv_path, rules_path = self._write_inputs(
                directory,
                "id,name\n1,Alice\n2,Bob\n",
                {"rules": [{"type": "required", "column": "name"}]},
            )
            json_path = directory / "quality.json"
            html_path = directory / "quality.html"
            with contextlib.redirect_stdout(io.StringIO()):
                exit_code = main([
                    str(csv_path),
                    "--rules",
                    str(rules_path),
                    "--output",
                    str(json_path),
                    "--html-report",
                    str(html_path),
                ])
            self.assertEqual(exit_code, 0)
            self.assertEqual(json.loads(json_path.read_text(encoding="utf-8"))["failed"], 0)
            self.assertIn("Quality Report", html_path.read_text(encoding="utf-8"))

    def test_failed_run_returns_nonzero(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            csv_path, rules_path = self._write_inputs(
                directory,
                "id,name\n1,Alice\n1,Bob\n",
                {"rules": [{"type": "unique", "column": "id"}]},
            )
            with contextlib.redirect_stdout(io.StringIO()):
                exit_code = main([str(csv_path), "--rules", str(rules_path)])
            self.assertEqual(exit_code, 1)
