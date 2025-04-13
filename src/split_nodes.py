from textnode import *
from extractmarkdown import *

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

def split_nodes_image(old_nodes):
    result_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result_nodes.append(old_node)
            continue

        text = old_node.text
        images = extract_markdown_images(text)

        if not images:
            result_nodes.append(old_node)
            continue

        current_text = text
        
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            if image_markdown in current_text:
                parts = current_text.split(image_markdown, 1)
                
                if parts[0]:
                    result_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                result_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                
                current_text = parts[1] if len(parts) > 1 else ""
            
        if current_text:
            result_nodes.append(TextNode(current_text, TextType.TEXT))

    return result_nodes
        
def split_nodes_links(old_nodes):
    result_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result_nodes.append(old_node)
            continue

        text = old_node.text
        links = extract_markdown_links(text)

        if not links:
            result_nodes.append(old_node)
            continue

        current_text = text
        
        for link_text, url in links:
            links_markdown = f"[{link_text}]({url})"
            if links_markdown in current_text:
                parts = current_text.split(links_markdown, 1)
                
                if parts[0]:
                    result_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                result_nodes.append(TextNode(link_text, TextType.LINK, url))
                
                current_text = parts[1] if len(parts) > 1 else ""
            
        if current_text:
            result_nodes.append(TextNode(current_text, TextType.TEXT))

    return result_nodes

        

        