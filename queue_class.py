class Queue:
    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, entry): #Add item to the back of the queue.
        new_back = entry
        if self.is_empty():
            self._front = new_back
            self._back = new_back
        else:
            self._back.next = new_back
            self._back = new_back
            self._back.next = None

    def dequeue(self): #Remove item from front of the queue and return that item.
        front_value = self.peek_front()
        self._front = self._front.next
        return front_value

    def peek_front(self): #Return item in front of the queue.
        if self.is_empty():
            raise RuntimeError('Stack empty')
        else:
            return self._front

    def is_empty(self): #Check if queue is empty.
        return self._front == None
