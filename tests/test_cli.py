import json
import unittest

from stockroom.cli import run


class Cli(unittest.TestCase):
    def test_title(self):
        out = json.loads(run(["--title", "x"]))
        self.assertEqual(out["title"], "x")
        self.assertEqual(out["status"], "open")
