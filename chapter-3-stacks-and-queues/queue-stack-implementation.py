import sys
sys.path.append("../chapter-2-linked-lists") # to allow for implementation of the linked list module

from LL_implementation import LinkedList, LLNode

""" Implement Stack and Queue classes from Python list object. Stack should contain pop(), push(item), peek(), and is_empty() methods & Queue should contain enqueue(item) (add/push), dequeue() (remove/pop), peek(), and is_empty() methods. """

class Stack(object):

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, data):
        self.items.append(data)
        return

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop(-1)


class Queue(object):

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def enqueue(self, data):
        self.items.append(data)
        return

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]


""" Implement Stack and Queue classes from LinkedList object. """
