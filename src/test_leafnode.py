import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_p_to_html(self):
        leaf_node = LeafNode("p", "I'm a paragraph", None)
        result = "<p>I'm a paragraph</p>"
        self.assertEqual(leaf_node.to_html(), result)

    def test_a_to_html_with_props(self):
        props_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        leaf_node = LeafNode("a", "Click me!", props_dict)
        print(f"leafNode props: {leaf_node.props}")
        html = leaf_node.to_html()
        print(f"generated HTML: {html}")

        # Dictionary is unordered so cant check for exact matching string
        self.assertTrue(html.startswith("<a"))
        self.assertTrue('href="https://www.google.com"' in html)
        self.assertTrue('target="_blank"' in html)
        self.assertTrue(">Click me!</a>" in html)

if __name__ == "__main__":
    unittest.main()