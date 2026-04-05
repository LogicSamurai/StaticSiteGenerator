from multiprocessing import Value
from pydoc import html, text
from src.blockutils import BlockType, block_to_block_type, markdown_to_blocks
from src.htmlnode import HTMLNode, ParentNode
from src.inline_markdown import text_to_textnodes
from src.textnode import TextNode, TextType, text_node_to_html_node


def _text_to_children(text):
    text = text.replace("\n"," ")
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    # looping over each block to find it's type
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = _block_to_html_node(block,block_type)
        html_nodes.append(html_node)
    
    return ParentNode("div",html_nodes)

def _block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        return _paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING:
        return _heading_to_html_node(block)
    elif block_type == BlockType.CODE:
        return _code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return _quote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return _uolist_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return _olist_to_html_node(block)
    else:
        raise ValueError(f"Invalid block type: {block_type}")
        
def _paragraph_to_html_node(block):
    children = _text_to_children(block)
    return ParentNode("p",children)
    
def _heading_to_html_node(block):
    # it will be only single line so we ahe to do accordingly
    # first count the no of #'s
    count = 0
    for char in block:
        if char == '#':
            count += 1
        else:
            break
    
    text = block[count+1:]
    children = _text_to_children(text)
    return ParentNode(f"h{count}", children)
    
def _code_to_html_node(block):
    # Remove the opening ``` and closing ```
    lines = block.split("\n")
    text = "\n".join(lines[1:-1])
    
    # create TextNode directly, no inline markdown parsing
    text_node = TextNode(text,TextType.CODE)
    html_node = text_node_to_html_node(text_node)
   
    return ParentNode("pre",[html_node])

def _quote_to_html_node(block):
    # first split all the lines in block
    
    lines = block.split("\n")
    new_lines = []
    
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    
    text = " ".join(new_lines)
    children = _text_to_children(text)
    
    return ParentNode("blockquote",children)

def _uolist_to_html_node(block):
    lines = block.split("\n")
    
    list_items = []
    for line in lines:
        text = line[2:]
        children = _text_to_children(text)
        list_items.append(ParentNode("li",children))
    
    return ParentNode("ul",list_items)

def _olist_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        #remove the 1. numberings
        index = line.find(". ")
        text = line[index+2:]
        children = _text_to_children(text)
        list_items.append(ParentNode("li",children))
    
    return ParentNode("ol",list_items)