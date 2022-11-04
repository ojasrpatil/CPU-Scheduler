from stack_class import Stack

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None
        self.stack_calls = Stack()
