from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
    node = TextNode('This is some anchor text', TextType.TEXT, 'https://www.boot.dev')
    print(node)

def text_node_to_html_node(text_node):
        if TextType.TEXT == text_node.text_type:
            return LeafNode(None, text_node.text)
        elif TextType.BOLD == text_node.text_type:
            return LeafNode('b', text_node.text)
        elif TextType.ITALIC == text_node.text_type:
            return LeafNode('i', text_node.text)
        elif TextType.CODE == text_node.text_type:
            return LeafNode('code', text_node.text)
        elif TextType.LINK == text_node.text_type:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        elif TextType.IMAGE == text_node.text_type:
            return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
        else:
            raise ValueError(f"Unknown text type: {text_node.text_type}")

main()