import unittest

from src.textnode import TextNode, TextType
from src.inline_markdown import split_nodes_image,split_nodes_link,text_to_textnodes
from src.blockutils import markdown_to_blocks


class TestTextNode(unittest.TestCase):
    # def test_delim_bold(self):
    #     node = TextNode("This is text with a **bolded** word", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is text with a ", TextType.TEXT),
    #             TextNode("bolded", TextType.BOLD),
    #             TextNode(" word", TextType.TEXT),
    #         ],
    #         new_nodes,
    #     )

    # def test_delim_bold_double(self):
    #        node = TextNode(
    #            "This is text with a **bolded** word and **another**", TextType.TEXT
    #        )
    #        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #        self.assertListEqual(
    #            [
    #                TextNode("This is text with a ", TextType.TEXT),
    #                TextNode("bolded", TextType.BOLD),
    #                TextNode(" word and ", TextType.TEXT),
    #                TextNode("another", TextType.BOLD),
    #            ],
    #            new_nodes,
    #        )

    # def test_delim_bold_multiword(self):
    #     node = TextNode(
    #         "This is text with a **bolded word** and **another**", TextType.TEXT
    #     )
    #     new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is text with a ", TextType.TEXT),
    #             TextNode("bolded word", TextType.BOLD),
    #             TextNode(" and ", TextType.TEXT),
    #             TextNode("another", TextType.BOLD),
    #         ],
    #         new_nodes,
    #     )


    # def test_delim_italic(self):
    #     node = TextNode(
    #         "This is text with a _italic word_ and another", TextType.TEXT
    #     )
    #     new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is text with a ", TextType.TEXT),
    #             TextNode("italic word", TextType.ITALIC),
    #             TextNode(" and another", TextType.TEXT),
    #         ],
    #         new_nodes,
    #     )

    # def test_delim_italic_double(self):
    #         node = TextNode(
    #             "This is text with a _italic word_ and _another_", TextType.TEXT
    #         )
    #         new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    #         self.assertListEqual(
    #             [
    #                 TextNode("This is text with a ", TextType.TEXT),
    #                 TextNode("italic word", TextType.ITALIC),
    #                 TextNode(" and ", TextType.TEXT),
    #                 TextNode("another", TextType.ITALIC),
    #             ],
    #             new_nodes,
    #         )
    #

    # def test_split_images(self):
    #     node = TextNode(
    #         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #         TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_image([node])
    #     self.assertListEqual(
    #         [TextNode("This is text with an ", TextType.TEXT),
    #             TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
    #             TextNode(" and another ", TextType.TEXT),
    #             TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")],
    #         new_nodes,
    #     )

    # def test_split_links(self):
    #     node = TextNode(
    #         "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #         TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_link([node])
    #     self.assertListEqual(
    #         [
    #             TextNode("This is text with a link ", TextType.TEXT),
    #             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #             TextNode(" and ", TextType.TEXT),
    #             TextNode(
    #                 "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #             ),
    #         ],
    #         new_nodes,
    #     )
    #
    #

    # def test_text_to_textnodes_bold(self):
    #     text = "This is **bold** text"
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is ", TextType.TEXT),
    #             TextNode("bold", TextType.BOLD),
    #             TextNode(" text", TextType.TEXT),
    #         ],
    #         nodes,
    #     )

    # def test_text_to_textnodes_italic(self):
    #     text = "This is *italic* text"
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is ", TextType.TEXT),
    #             TextNode("italic", TextType.ITALIC),
    #             TextNode(" text", TextType.TEXT),
    #         ],
    #         nodes,
    #     )

    # def test_text_to_textnodes_code(self):
    #     text = "This is `code` text"
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is ", TextType.TEXT),
    #             TextNode("code", TextType.CODE),
    #             TextNode(" text", TextType.TEXT),
    #         ],
    #         nodes,
    #     )

    # def test_text_to_textnodes_image(self):
    #     text = "This is ![image](https://example.com/image.png) text"
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is ", TextType.TEXT),
    #             TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
    #             TextNode(" text", TextType.TEXT),
    #         ],
    #         nodes,
    #     )

    # def test_text_to_textnodes_link(self):
    #     text = "This is [link](https://example.com) text"
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is ", TextType.TEXT),
    #             TextNode("link", TextType.LINK, "https://example.com"),
    #             TextNode(" text", TextType.TEXT),
    #         ],
    #         nodes,
    #     )

    # def test_text_to_textnodes_combined(self):
    #     text = "This is **bold** and *italic* and `code` and ![image](https://example.com/image.png) and [link](https://example.com)"
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is ", TextType.TEXT),
    #             TextNode("bold", TextType.BOLD),
    #             TextNode(" and ", TextType.TEXT),
    #             TextNode("italic", TextType.ITALIC),
    #             TextNode(" and ", TextType.TEXT),
    #             TextNode("code", TextType.CODE),
    #             TextNode(" and ", TextType.TEXT),
    #             TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
    #             TextNode(" and ", TextType.TEXT),
    #             TextNode("link", TextType.LINK, "https://example.com"),
    #         ],
    #         nodes,
    #     )

    # def test_text_to_textnodes_no_markdown(self):
    #     text = "This is plain text"
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is plain text", TextType.TEXT),
    #         ],
    #         nodes,
    #     )

    # def test_text_to_textnodes_empty(self):
    #     text = ""
    #     nodes = text_to_textnodes(text)
    #     self.assertListEqual([], nodes)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_ignores_empty_blocks(self):
        md = """

First block



Second block

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block",
            ],
        )


if __name__ == "__main__":
    unittest.main()
