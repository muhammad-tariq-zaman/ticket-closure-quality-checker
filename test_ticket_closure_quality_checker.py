import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check

def row(t, note, reopened):
    return {"ticket": t, "has_resolution_note": note, "reopened": reopened}

class TestClosureQuality(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(check([row("T1", "yes", "no")])[0][1], "PASS")
    def test_no_note_fails(self):
        self.assertEqual(check([row("T1", "no", "no")])[0][2], "no resolution note")
    def test_reopened_fails(self):
        self.assertEqual(check([row("T1", "yes", "yes")])[0][2], "reopened after closure")
    def test_case_insensitive(self):
        self.assertEqual(check([row("T1", "YES", "NO")])[0][1], "PASS")
