import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        text = "This is a regular paragraph with no special formatting."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        
        text = "This is another paragraph\nwith multiple lines."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
    
    def test_heading(self):
        # Test all heading levels (1-6)
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        
        # Test invalid headings
        self.assertEqual(block_to_block_type("#No space after hash"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### Too many hashes"), BlockType.PARAGRAPH)
    