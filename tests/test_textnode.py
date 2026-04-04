# import unittest

# from src.textnode import TextNode, TextType, text_node_to_html_node


# class TestTextNode(unittest.TestCase):
#     def test_eq(self):
#         node = TextNode("This is a text node", TextType.BOLD)
#         node2 = TextNode("This is a text node", TextType.BOLD)
#         self.assertEqual(node, node2)

#     def test_neq(self):
#         node = TextNode("This is a text node", TextType.BOLD)
#         node2 = TextNode("This is another text node", TextType.BOLD)
#         self.assertNotEqual(node, node2)

#     def test_url_none(self):
#         node = TextNode("This is a text node", TextType.BOLD, None)
#         node2 = TextNode("This is a text node", TextType.BOLD)
#         self.assertEqual(node, node2)

#     def test_empty_text(self):
#         node = TextNode("", TextType.TEXT)
#         node2 = TextNode("", TextType.TEXT)
#         self.assertEqual(node, node2)

#     def test_different_types(self):
#         node = TextNode("Text", TextType.ITALIC)
#         node2 = TextNode("Text", TextType.BOLD)
#         self.assertNotEqual(node, node2)

#     def test_properties(self):
#         node = TextNode("Hello", TextType.CODE, "https://example.com")
#         self.assertEqual(node.text, "Hello")
#         self.assertEqual(node.text_type, TextType.CODE)
#         self.assertEqual(node.url, "https://example.com")

#     def test_repr(self):
#         node = TextNode("This is a text node", TextType.BOLD)
#         expected_repr = "TextNode(This is a text node, bold, None)"
#         self.assertEqual(repr(node), expected_repr)


# class TestTextNodeToHTMLNode(unittest.TestCase):
#     def test_text(self):
#         node = TextNode("This is a text node", TextType.TEXT)
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, None)
#         self.assertEqual(html_node.value, "This is a text node")

#     def test_image(self):
#         node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, "img")
#         self.assertEqual(html_node.value, "")
#         self.assertEqual(
#             html_node.props,
#             {"src": "https://www.boot.dev", "alt": "This is an image"},
#         )

#     def test_bold(self):
#         node = TextNode("This is bold", TextType.BOLD)
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, "b")
#         self.assertEqual(html_node.value, "This is bold")


# if __name__ == "__main__":
#     unittest.main()
