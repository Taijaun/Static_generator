from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        # validate
        if self.tag == None:
            raise ValueError("tag is required")
        
        if self.children == None:
            raise ValueError("children is required")
        
        # Create opening tag
        props_html = self.props_to_html()
        opening_tag = f"<{self.tag}{props_html}"
        
        # Process children tags
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"{opening_tag}>{children_html}</{self.tag}>"
        
