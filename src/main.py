from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode

def main():
    node = TextNode('This is some anchor text', TextType.NORMAL, 'https://www.boot.dev')
    print(node)

def text_node_to_html_node(text_node):
    if TextType.NORMAL == text_node.text_type:
        return f'<a href="{text_node.url}">{text_node.text}</a>'
    elif TextType.HEADING == text_node.text_type:
        return f'<h1>{text_node.text}</h1>'
    elif TextType.BOLD == text_node.text_type:
        return f'<strong>{text_node.text}</strong>'
    elif TextType.ITALIC == text_node.text_type:
        return f'<em>{text_node.text}</em>'
    elif TextType.CODE == text_node.text_type:
        return f'<code>{text_node.text}</code>'
    elif TextType.LINK == text_node.text_type:
        return f'<a href="{text_node.url}">{text_node.text}</a>'
    elif TextType.IMAGE == text_node.text_type:
        return f'<img src="{text_node.url}" alt="{text_node.text}">'
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
    ''' see you're on the right track with the structure, but there are a few important things to consider:

Return type: The lesson asks you to return a LeafNode object, but you're returning HTML strings. What type of object should this function actually create and return?

TextType values: You're using TextType.NORMAL and TextType.HEADING, but looking at the lesson requirements, what are the actual TextType enum values you need to handle?

HTML tags: Some of your HTML tags don't match what the lesson specifies. For example, what tag should TextType.BOLD use according to the requirements?

Let's start with the first point - instead of returning HTML strings, what kind of object should you be creating? And do you have the necessary imports at the top of your file to create that type of object?'''
     
main()