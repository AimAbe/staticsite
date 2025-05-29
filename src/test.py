import unittest

from parentnode import ParentNode 
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
       node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
       self.assertEqual(node.url, "https://www.boot.dev")   
       node2 = TextNode("This is a text node", TextType.BOLD)
       self.assertNotEqual(node, node2)     
       self.assertEqual(node2.url, None) 
       
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_nested_parents(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        inner_parent_node = ParentNode("div", [child_node])
        outer_parent_node = ParentNode("div", [inner_parent_node])
        self.assertEqual(
            outer_parent_node.to_html(),
            "<div><div><span><b>grandchild</b></span></div></div>",
        )
    
    def test_to_html_with_none(self):
        child = ParentNode(None, None)
        
        with self.assertRaises(ValueError) as cm:
            child.to_html()
            print('Value error!')
        
        self.assertEqual(
            str(cm.exception), 
            "ParentNode must have a tag"
        ) 

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
        
    def test_to_html_with_invalid_child(self):
        with self.assertRaises(TypeError) as cm:
            parent_node = ParentNode("div", ["invalid_child"])
            parent_node.to_html()
        
        self.assertEqual(
            str(cm.exception), 
            "Child must be an instance of HTMLNode"
        )
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        props = {'class': 'foo', 'id': 'bar'}
        parent_node = ParentNode("div", [child_node], props)
        self.assertEqual(
            parent_node.to_html(),
            '<div class="foo" id="bar"><span>child</span></div>'
        )


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()  