from src.textnode import TextNode, TextType
import re
# from Exceptions import ValidationError

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        splited_nodes = []
        splited_node = node.text.split(delimiter)

        if len(splited_node) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not ended.")

        for i in range(len(splited_node)):
            if splited_node[i] == "":
                continue

            if i%2 == 0:
                splited_nodes.append(TextNode(splited_node[i],TextType.TEXT))
            else:
                splited_nodes.append(TextNode(splited_node[i],text_type))

        new_nodes.extend(splited_nodes)

    return new_nodes

def extract_markdown_images(text):
    markdown_images = []

    alt_texts = re.findall(r"!\[(.*?)\]", text)
    image_paths = re.findall(r"\((.*?)\)",text)

    if len(alt_texts) != len(image_paths):
        return markdown_images

    for i in range(len(alt_texts)):
        markdown_images.append((alt_texts[i], image_paths[i]))


    return markdown_images


def extract_markdown_links(text):
    markdown_links = []

    alt_texts = re.findall(r"\[(.*?)\]", text)
    image_paths = re.findall(r"\((.*?)\)",text)

    if len(alt_texts) != len(image_paths):
        return markdown_links

    for i in range(len(alt_texts)):
        markdown_links.append((alt_texts[i], image_paths[i]))


    return markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            new_nodes.append(i)
            continue
        splitted_text = re.split(r"(!\[.*?\]\(.*?\))",i.text)
        # print("splitted text!!!!!!!!!!!!!!11111",splitted_text)
        for j in splitted_text:
            if not j:
                continue
            if j.startswith('!'):
                alt_text = re.findall(r'!\[(.*?)\]',j)
                image_link = re.findall(r'\((.*?)\)',j)
                node = TextNode(alt_text[0], TextType.IMAGE, image_link[0])
                new_nodes.append(node)
            else:
                node = TextNode(j,TextType.TEXT)
                new_nodes.append(node)

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for i in old_nodes:
        if i.text_type != TextType.TEXT:
            new_nodes.append(i)
            continue
        splitted_text = re.split(r"(\[.*?\]\(.*?\))",i.text)
        for j in splitted_text:
            if not j:
                continue
            if j.startswith('['):
                alt_text = re.findall(r'\[(.*?)\]',j)
                link = re.findall(r'\((.*?)\)',j)
                node = TextNode(alt_text[0], TextType.LINK, link[0])
                new_nodes.append(node)
            else:
                node = TextNode(j,TextType.TEXT)
                new_nodes.append(node)

    return new_nodes

def text_to_textnodes(text):
    if text == "":
        return []

    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
