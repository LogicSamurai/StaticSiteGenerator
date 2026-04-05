# import unittest

# from src.markdown import markdown_to_html_node
# from src.htmlnode import ParentNode, LeafNode


# class TestMarkdownToHTML(unittest.TestCase):
#     def test_paragraphs(self):
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here
# """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#         )

#     def test_code_block(self):
#         md = """
# ```
# This is text that _should not_ be **bolded**
# ```
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><pre><code>This is text that _should not_ be **bolded**</code></pre></div>",
#         )

#     def test_heading(self):
#         md = """
# # This is a heading

# ## This is a second heading

# ### This is a third heading        
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><h1>This is a heading</h1><h2>This is a second heading</h2><h3>This is a third heading</h3></div>",
#         )
    
#     def test_blockquote(self):
#         md = """
# > This is a 
# > blockquote block

# This is a paragraph text
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><blockquote>This is a blockquote block</blockquote><p>This is a paragraph text</p></div>"
#         )
    
#     def test_unordered_list(self):
#         md = """
# - Item 1
# - Item 2
# - Item 3
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
#         )
    
#     def test_ordered_list(self):
#         md = """
# 1. Item 1
# 2. Item 2
# 3. Item 3
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>"
#         )
    
#     def test_combined(self):
#         md = """
# # Heading

# This is a paragraph with **bold** and _italic_ text.

# - List item 1
# - List item 2

# ```
# code block
# ```

# > This is a quote
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
        
#         self.assertEqual(
#             html,
#             "<div><h1>Heading</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><ul><li>List item 1</li><li>List item 2</li></ul><pre><code>code block</code></pre><blockquote>This is a quote</blockquote></div>"
#         )
    
#     def test_inline_markdown_in_paragraph(self):
#         md = """
# This paragraph has a [link](https://example.com) and an ![image](https://example.com/image.png)
# """
    
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             '<div><p>This paragraph has a <a href="https://example.com">link</a> and an <img src="https://example.com/image.png" alt="image"></p></div>'
#         )
    
# if __name__ == "__main__":
#     unittest.main()