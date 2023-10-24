from char_node import CharNode
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, char):
        new_node = CharNode(char)
        new_node.next_node = self.head
        self.head = new_node

    def display(self):
        current = self.head
        inverted_word = ""
        while current:
            inverted_word += current.char
            current = current.next_node
        return inverted_word