import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.stack = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        if value is not None:
        #adding to top
            self.stack.add_to_tail(value)
            self.size += 1


    def pop(self):
        #removing from the top
        if self.stack.tail is not None:
            self.size -= 1
            return self.stack.remove_from_tail()
        
        
        

    def len(self):
        self.size = len(self.stack)
        return self.size
