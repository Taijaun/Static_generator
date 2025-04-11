from htmlnode import HTMLNode

class LeafNode():
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)

    def to_html(self):
        if not self.value:
            raise ValueError("no value")
        
        if self.tag == None:
            return f"{self.value}"
        
        html_string = f"<{self.tag} {self.props}>{self.value}</{self.tag}>"
        return html_string