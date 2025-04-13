from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_text):

    # Check for heading ( 1-6 # followed by space)
    def is_heading(text):
        if text.startswith(('#', '##', '###', '####', '#####', '######')):
            hash_count = 0
            for char in text:
                if char == '#':
                    hash_count += 1
                else:
                    break

            if 1 <= hash_count <= 6 and len(text) > hash_count and text[hash_count] == ' ':
                return True
            return False


    # Check for code block (``)
    def is_code_block(text):
        if text.startswith("```") and text.endswith('```'):
            # ensure its not an empty code block
            if len(text) > 6:
                return True
            
        return False


    # check for quote ( >)
    def is_quote(text):
        lines = text.split("\n")

        for line in lines:
            if not line.startswith(">"):
                return False
        return True

    # Check for unordered list ( - )
    def is_unordered_list(text):
        lines = text.split("\n")

        for line in lines:
            if not line.startswith("- "):
                return False
        return True

    # Check for ordered list ( 1., 2.)
    def is_ordered_list(text):
        lines = text.split("\n")

        expected_number = 1
        for line in lines:
            expected_prefix = f"{expected_number}."
            if not line.startswith(expected_prefix):
                return False
            
            expected_number += 1

        return True


    match True:
        case _ if is_heading(markdown_text):
            return BlockType.HEADING
        case _ if is_code_block(markdown_text):
            return BlockType.CODE
        case _ if is_quote(markdown_text):
            return BlockType.QUOTE
        case _ if is_unordered_list(markdown_text):
            return BlockType.UNORDERED_LIST
        case _ if is_ordered_list(markdown_text):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
    # If none, return Blocktype.Paragraph