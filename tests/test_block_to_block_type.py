import unittest

from src.blockutils import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> this is a quote\n> still a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = "- first item\n- second item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = "1. first item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        block = "This is a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_multiline_ordered_list_block(self):
        block = "1. first item\n2. second item\n3. third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
