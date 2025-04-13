import unittest
from split_nodes import *

class TestSplitNodes(unittest.TestCase):
    def test_no_delimiters(self):
        # Test when there are no delimiters in the text
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Just plain text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    
    def test_one_delimiter_pair(self):
        # Test with one pair of delimiters
        node = TextNode("Text with a **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    

    
    def test_different_delimiter_types(self):
    # Test with code delimiter (backtick)
        node = TextNode("Here is some `code` to display", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
    
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Here is some ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " to display")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    
        # Test with italic delimiter (underscore)
        node = TextNode("This word is _italicized_ for emphasis", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
    
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This word is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "italicized")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " for emphasis")
        self.assertEqual(result[2].text_type, TextType.TEXT)