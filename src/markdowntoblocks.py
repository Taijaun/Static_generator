

def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    blocks = markdown.split("\n\n")

    cleaned_blocks = []

    for block in blocks:
        if block.strip():
            lines = [line.strip() for line in block.split('\n')]
            cleaned_block = '\n'.join(lines)
            cleaned_blocks.append(cleaned_block)

    return cleaned_blocks
