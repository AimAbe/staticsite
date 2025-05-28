from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise TypeError("Child must be an instance of HTMLNode")
            html += child.to_html()
        html += f"</{self.tag}>"
        return html

    def props_to_html(self):
        if not self.props:
            return ""
        props_html = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {props_html}" if props_html else ""
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    

 