from markdowntoblocks import markdown_to_blocks
from htmlnode import HTMLNode
from blocktype import *
from textnode import *
from split_nodes import *

def extract_links(text):
    regex = r"\[([^\]]+)\]\(([^)]+)\)"  # Matches markdown links like [text](url)
    matches = list(re.finditer(regex, text))  # Find all matches
    nodes = []

    last_end = 0
    for match in matches:
        # Add any plain text before the link
        if match.start() > last_end:
            nodes.append(TextNode(text[last_end:match.start()], TextType.TEXT))
        
        # Add the link itself as a new node
        link_text = match.group(1)  # text inside [ ]
        link_url = match.group(2)
        nodes.append(TextNode(f"{link_text} ({link_url})", TextType.LINK))

        last_end = match.end()

    if last_end < len(text):
        nodes.append(TextNode(text[last_end:], TextType.TEXT))

    return nodes
    
def text_to_children(text):
    # 1. Start with plain text
    text = text.replace("\n", " ")  # Replace newlines with spaces
    
    
    # 2. Apply transformations in the correct order
    nodes = extract_links(text)

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    html_nodes = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    
    return html_nodes
    


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = HTMLNode("div", None, [], None)
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            p_node = HTMLNode("p", None, [], None)
            p_node.children = text_to_children(block)
            parent_node.children.append(p_node)
            
        elif block_type == BlockType.HEADING:
            # Count the number of # to determine heading level
            level = 0
            for char in block:
                if char == '#':
                    level += 1
                else:
                    break
            
            heading_text = block[level:].strip()
            h_node = HTMLNode(f"h{level}", None, [], None)
            h_node.children = text_to_children(heading_text)
            parent_node.children.append(h_node)
            
        elif block_type == BlockType.CODE:
            code_lines = block.split("\n")
            code_content = "\n".join(code_lines[1:-1])
            code_node = HTMLNode("pre", None, [
                HTMLNode("code", code_content)
            ])
            parent_node.children.append(code_node)
            
        elif block_type == BlockType.QUOTE:
            # Remove the > from each line
            quote_lines = block.split("\n")
            quote_text = "\n".join([line[1:].strip() for line in quote_lines])
            quote_node = HTMLNode("blockquote", None, [], [])
            quote_node.children = text_to_children(quote_text)
            parent_node.children.append(quote_node)

        elif block_type == BlockType.UNORDERED_LIST:
            ul_node = HTMLNode("ul", None, [])
            list_items = block.split("\n")
            for item in list_items:
                if item.strip():  # Skip empty lines
                    # Remove the "* " or "- " prefix
                    item_text = item.strip()[2:].strip()
                    li_node = HTMLNode("li", None, [])
                    li_node.children = text_to_children(item_text)
                    ul_node.children.append(li_node)
            parent_node.children.append(ul_node)

        elif block_type == BlockType.ORDERED_LIST:
            ol_node = HTMLNode("ol", None, [])
            list_items = block.split("\n")
            for item in list_items:
                if item.strip():  # Skip empty lines
                 # Remove the "1. " style prefix
                    # Find the first space after a digit and period
                    for i, char in enumerate(item.strip()):
                        if char == ' ' and i > 1 and item.strip()[i-1] == '.':
                            item_text = item.strip()[i+1:].strip()
                            break
                    li_node = HTMLNode("li", None, [])
                    li_node.children = text_to_children(item_text)
                    ol_node.children.append(li_node)
            parent_node.children.append(ol_node)

    return parent_node

