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
        if len(pop_val) < 1:
            return None
        pop_value = self.size
        minus_one = pop_value - 1
        pop_val.delete(minus_one)
        return minus_one

    # def pop(self):
    #     pop_val = DoublyLinkedList()
       
    #     if self.size is 0:
    #         return None
    #     else:
    #         pop_value = self.size
    #         minus_one = pop_value - 1
    #         pop_val.delete(minus_one)
    #         return minus_one
    #     #     value.remove_from_head()
    #         # return value
    #         # value = self.size
    #         # minus_one = value - 1
    #         # print(minus_one)
    #         # pop_val.delete(minus_one)
    #         # return minus_one
    #         # self.size -= 1
    #         # self.size = pop_val
    #     # pop_value = self.size.length
    #     # self.size = self.size.next
    #     # self.size.
    #     return self.size
    #     # self.size -= 1
    #     # return pop_val
    #     # pop_val = DoublyLinkedList()
    #     # if pop_val != None:
    #     #     return pop_val.pop()


    def len(self):
        # return len(Stack)
        return self.size

# stack_list = Stack()
# print(stack_list.pop())
## for stack we add values to the head/top
## the head/top is considered the start.
## when we remove we remove from the head/top
## a LL

## we always remove from an end or the front

## if this was an array adding is O(n)

## linkedlist is O(1)