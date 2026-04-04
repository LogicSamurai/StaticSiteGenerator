# import unittest

# from src.htmlnode import HTMLNode, LeafNode


# class TestHTMLNode(unittest.TestCase):

#     def test_properties(self):
#         node = HTMLNode("a", None,"b",{"href":"https://gurupatel.netlify.app","target":"_blank"})
#         self.assertEqual(node.tag, "a")
#         self.assertEqual(node.value, None)
#         self.assertEqual(node.children, "b")
#         self.assertEqual(node.props, {"href":"https://gurupatel.netlify.app","target":"_blank"})

#     def test_repr(self):
#         node = HTMLNode("a", None,"b",{"href":"https://gurupatel.netlify.app","target":"_blank"})
#         expected_repr = "HTMLNode(a, None, b, {'href': 'https://gurupatel.netlify.app', 'target': '_blank'})"
#         self.assertEqual(repr(node), expected_repr)

#     def test_prop_to_html(self):
#         node = HTMLNode('a', None, 'b', {'href': 'https://gurupatel.netlify.app', 'target': '_blank'})
#         expected_str = ' href="https://gurupatel.netlify.app" target="_blank"'

#         actual_str = node.props_to_html()
#         self.assertEqual(node.props_to_html(),expected_str)

#     def test_empty_prop_to_html(self):
#         node = HTMLNode('a', None, 'b', None)
#         expected_str = ''

#         actual_str = node.props_to_html()
#         self.assertEqual(node.props_to_html(),expected_str)

#     def test_leaf_to_html_p(self):
#         node = LeafNode("p", "Hello, world!")
#         self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

#     def test_leaf_to_html_a(self):
#         node = LeafNode("a", "Click Me!",{"href": "https://www.google.com", "target": "_blank"})
#         self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click Me!</a>')

#     def test_left_to_html_no_tag(self):
#         node = LeafNode(None, "Click Me!")
#         self.assertEqual(node.to_html(),"Click Me!")

# if __name__ == "__main__":
#     unittest.main()