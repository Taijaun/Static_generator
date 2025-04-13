from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        # if node is not a TEXT type, add it unchanged
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
            # How to find first delimiter

        if delimiter not in text:
            new_nodes.append(old_node)
            continue
        
        try:
            first_delimiter_index = text.index(delimiter)
            second_delimiter_index = text.index(delimiter, first_delimiter_index + len(delimiter))
            
            
            before_delimiter = text[:first_delimiter_index]
            between_delimiters =  text[first_delimiter_index + len(delimiter): second_delimiter_index]
            after_delimiter = text[second_delimiter_index + len(delimiter):]

            
            if before_delimiter:
                new_nodes.append(TextNode(before_delimiter, TextType.TEXT))
            
            new_nodes.append(TextNode(between_delimiters, text_type))
            
            if after_delimiter:
                new_nodes.append(TextNode(after_delimiter, TextType.TEXT))

        except ValueError:
            raise Exception(f"No closing delimiter found for {delimiter}")
        
        
    return new_nodes

