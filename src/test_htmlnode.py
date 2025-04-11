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

    def test_props_to_html(self):
        props_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode("p", "hello world", None, props_dict)
        result = node1.props_to_html()
        correct_string = f" href=\"https://www.google.com\" target=\"_blank\""

        self.assertNotEqual(correct_string, "")
        self.assertEqual(correct_string, result)

    def test_props_to_html_no_props(self):
        node1 = HTMLNode("p", "hello world", None, None)
        result = node1.props_to_html()

        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
