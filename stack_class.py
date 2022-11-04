from calls_class import Calls

class Stack:
    def __init__(self):
        self._top = None
    
    def push(self, entry): #Add items to stack.
        new_top = Calls(entry)
        if self._top == None:
            self._top = new_top
        else:
            self._top.next = new_top
            self._top = new_top

    def pop(self): #Remove items from stack.
        if self._top != None:
            self._top = self._top.next
        else:
            raise RuntimeError('Stack empty')

    def peek(self): #Check top item in stack.
        if self._top != None:
            return self._top
        else:
            raise RuntimeError('Stack empty')

    def is_empty(self): #Check if stack is empty.
        return self._top == None
    
