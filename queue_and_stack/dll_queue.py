import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        #self.length = 1 if self.storage is not None else 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):


    def dequeue(self):
        pass

    def len(self):
        return self.size

queue_list = Queue

print(queue_list)
