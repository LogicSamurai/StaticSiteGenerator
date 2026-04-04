from src.blockutils import block_to_block_type, markdown_to_blocks
from src.htmlnode import HTMLNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    # looping over each block to find it's type
    for block in blocks:
        block_type = block_to_block_type(block)

        newHtmlNode = HTMLNode()
