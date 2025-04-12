from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        
        if self.children == None:
            raise ValueError("No children")
        
        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}>{children_html}</{self.tag}>"
        
