import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        pass

    def pop(self):
        pass

    def len(self):
        pass


## for stack we add values to the head/top
## the head/top is considered the start.
## when we remove we remove from the head/top
## a LL

## we always remove from an end or the front

## if this was an array adding is O(n)

## linkedlist is O(1)