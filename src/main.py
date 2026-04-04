from src.textnode import TextNode, TextType

def main():
    print("Static Site Generator is running...")
    text_obj = TextNode("Hello, World!",TextType.TEXT,"gurupatel.netlify.app")

    print(text_obj)

main()