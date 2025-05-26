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

'''
Empty List of Children:
What should happen if a ParentNode is constructed with an empty list for children? Should it raise an error, or produce something like <div></div>? Why?

Children with Different Node Types:
What if you mix LeafNode and ParentNode as siblings inside a parent? Does your code handle that variety without raising an error?

Recursive Nesting:
If you build a three- or four-level nested set of ParentNode objects, does the output stay correctly formed? Could you accidentally introduce duplicate or missing tags?

Invalid Children:
What if a child that's not an HTMLNode (like a string or a number) is included in the children list? Should your class raise an error? If so, have you checked for this?

Props Argument:
How does your class handle optional props? If you add attributes to your nodes (e.g., <div class="foo">), do those attributes appear properly in the HTML output?

'''