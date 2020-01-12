import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = DoublyLinkedList()
        #self.length = 1 if self.storage is not None else 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        queue_back = DoublyLinkedList(value)
        self.size += 1

        if not self.size:
            self.size = queue_back 
        else:
            queue_back = self.size
            

    def dequeue(self):
        # return self.storage.remove_from_head()
        
        remove_queue = DoublyLinkedList()
        
        if self.size is 0:
            return None
        else:
         
            # print('hmm..', self.storage.remove_from_head())
            self.size -= 1
       
            
            return remove_queue.remove_from_head() 

        # else:
        #     return None
        # queue_value = self.size
        # queue_remove = DoublyLinkedList()
        
    
        # remove_queue = self.size
        # self.size = remove_queue
       
     
        return remove_queue


    def len(self):
        return self.size

# queue_list = Queue

# print(queue_list)
