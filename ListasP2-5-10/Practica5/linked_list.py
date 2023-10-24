from word_node import WordNode
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, word):
        new_node = WordNode(word)
        new_node.next_node = self.head
        self.head = new_node

    def display(self):
        current = self.head
        list = []
        while current:
            list.append(current.word)
            current = current.next_node
        return list