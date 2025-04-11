from textnode import TextNode
from textnode import TextType

def main():
    print("hello world")
    node1 = TextNode("Hello", TextType.NORMAL, "https://example.com")
    node2 = TextNode("Hello", TextType.NORMAL, "https://example.com")
    node3 = TextNode("Goodbye", TextType.BOLD, "big bean")
    print(repr(node1))
    print(node1 == node3)



main()