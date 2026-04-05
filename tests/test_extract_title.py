import unittest
from src.main import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_simple_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_h1_with_spaces(self):
        self.assertEqual(extract_title("   # Hello World   "), "Hello World")

    def test_h1_in_multiple_lines(self):
        md = """
        Some text
        # My Title
        More text
        """
        self.assertEqual(extract_title(md), "My Title")

    def test_ignore_h2(self):
        md = "## Not H1\n# Correct Title"
        self.assertEqual(extract_title(md), "Correct Title")

    def test_no_h1(self):
        md = "This has no title"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_multiple_h1(self):
        md = "# First Title\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")


if __name__ == "__main__":
    unittest.main()