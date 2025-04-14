from textnode import *
from extractmarkdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
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

def text_to_textnodes(text):
    if not text:
        return []
    
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)

    return nodes

        

        