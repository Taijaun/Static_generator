import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode("p", "hello world", None, props_dict)
        node2 = HTMLNode("p", "hello world", None, props_dict)

        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
