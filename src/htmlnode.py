
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            return self.value or ""
    
        props_html = self.props_to_html()
    
        if self.children is None:
            if self.value is None:
                return f"<{self.tag}{props_html}></{self.tag}>"
            else:
                return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
    
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    
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
