import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        # self.length = 1 if self.size is not None else 0

    def push(self, value):
        push_val = DoublyLinkedList(value)
        self.size += 1

        if not self.size:
            self.size = push_val
        else:
            push_val = self.size
        # self.size = push_val
        # return add_val.append(value)

    def pop(self):
        pop_val = DoublyLinkedList()
        
        # pop_val.delete(self.size)

        if pop_val is not None:
            self.size -= 1
        else:
            return None
        # return pop_val
        # pop_val = DoublyLinkedList()
        # if pop_val != None:
        #     return pop_val.pop()


    def len(self):
        # return len(Stack)
        return self.size


## for stack we add values to the head/top
## the head/top is considered the start.
## when we remove we remove from the head/top
## a LL

## we always remove from an end or the front

## if this was an array adding is O(n)

## linkedlist is O(1)