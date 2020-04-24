import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.queue = DoublyLinkedList()
        #self.remove_from_head = DoublyLinkedList.remove_from_head
        # Why is our DLL a good choice to store our elements?
        #self.storage = []
        #dequeue should remove and return an item from the front of the queue. (remove from head, return item)
        #len returns the number of items in the queue. (return len of items in queue)
    
    def enqueue(self, value):
        # We increments the size of the queue
        #enqueue should add an item to the back of the queue. (Add to tail)
        if value is not None:
            self.queue.add_to_tail(value) 
            self.size += 1

        
    def dequeue(self):
        if self.queue.head is not None:
            self.size -= 1
            return self.queue.remove_from_head()

    def len(self):
        self.size = len(self.queue)
        return self.size

