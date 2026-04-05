from src.markdown import markdown_to_html_node
from src.textnode import TextNode, TextType
import os, shutil, pathlib, sys


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    os.makedirs(dest_dir_path, exist_ok=True)
    for item in os.listdir(dir_path_content):
        full_path = pathlib.Path(dir_path_content) / item
        if os.path.isfile(full_path):
            if item.endswith(".md"):
                htmlfilepath = pathlib.Path(dest_dir_path)/"index.html"
                generate_page(full_path, template_path, htmlfilepath, basepath)
        else:
            new_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(full_path, template_path, new_dest_path, basepath)

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        line = line.strip()
        
        # Check for H1 (starts with single # and a space)
        if line.startswith("# "):
            return line[2:].strip()
            
    # If no H1 found
    raise Exception("No H1 header found")

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Replace absolute paths with basepath
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

def copy_static_to_docs(basepath="/"):
    source = "./static"
    destination = "./docs"

    # Remove destination if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)

    # Copy entire directory
    shutil.copytree(source, destination)
    print("Static files copied to docs successfully!")
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = './docs/index.html'
    generate_page(from_path, template_path, dest_path, basepath)
    
def main():
    # Get basepath from CLI argument, default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Static Site Generator is running...")
    print(f"Using basepath: {basepath}")

    text_obj = TextNode("Hello, World!",TextType.TEXT,"gurupatel.netlify.app")

    copy_static_to_docs(basepath)
    generate_pages_recursive('./content', './template.html', './docs', basepath)
    print(text_obj)

main()