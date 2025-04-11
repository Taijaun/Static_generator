from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("no value")
        
        if self.tag == None:
            return self.value
        
        print(f"props: {self.props}")
        props_html = self.props_to_html()
        print(f"props HTML: {props_html}")

        if props_html:
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
