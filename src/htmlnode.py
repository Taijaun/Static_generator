
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def __eq__(self, HTMLNode2):
        return (
            self.tag == HTMLNode2.tag and
            self.value == HTMLNode2.value and
            self.children == HTMLNode2.children and
            self.props == HTMLNode2.props
        )
    
    def props_to_html(self):
        base_string = ""

        if self.props == None:
            return ""

        for attr in self.props:
            base_string += f" {attr}=\"{self.props[attr]}\""
        
        return base_string
    
    def __repr__(self):
        return f"HTMLNode ({self.tag}, {self.value}, {self.children}, {self.props})"
