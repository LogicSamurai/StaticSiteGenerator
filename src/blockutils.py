import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered_list"
    ORDERED_LIST="ordered_list"


# def block_to_block_type(block):
#     if block.startswith("# "):
#         return BlockType.HEADING
#     elif block.startswith("```\n") and block.endswith("```"):
#         return BlockType.CODE
#     elif block.startswith(">"):
#         return BlockType.QUOTE
#     elif block.startswith("- "):
#         return BlockType.UNORDERED_LIST
#     elif all(re.match(r"^\d+\.\s.+$", line) for line in block.split("\n")):
#         return BlockType.ORDERED_LIST
#     else:
#         return BlockType.PARAGRAPH
# 

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown=None):
    if markdown is None:
        return []

    blocks = markdown.split("\n\n")
    stripped_blocks = []

    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            stripped_blocks.append(stripped_block)

    return stripped_blocks
