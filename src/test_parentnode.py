import unittest

from parentnode import ParentNode 
from leafnode import LeafNode

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
# This code is a test suite for the ParentNode class, which is part of a static site generator.
# It checks various scenarios to ensure that the ParentNode behaves correctly when generating HTML output.
if __name__ == "__main__":
    unittest.main()