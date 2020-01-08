import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max_num_nodes = limit 
        self.cur_num_nodes = 0
        self.cache = {}
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # returns None if there is no Value
        value = None
        if key in self.cache is not None:
            node = self.cache[key]
            # make sure the node equals the value not the key
            value = node.value[1]
            # move to the front of the node of the storage. 
            self.storage.move_to_front(node)

        return value
        


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.cache is not None:
            # update with the new key
            node = self.cache[key]
            ## move the key to the front of the array
            self.storage.move_to_front(node)
            # maybe should be node.value instead of self.cache[key]
            # 
            node.value = [key, value]

            return
        # if the current num of nodes reached the limit remove the least used one
        if self.cur_num_nodes == self.max_num_nodes:
            # delete the key
            self.cache.pop(self.storage.tail.value[0])
            # removes the value at the end of the array
            self.storage.remove_from_tail()
            # subtracts the current number of nodes 
            self.cur_num_nodes -= 1

        #Adds the given key-value pair to the cache
        self.storage.add_to_head([key, value])
        ## sets the storage of the cache key to equal the self storage head
        self.cache[key] = self.storage.head
        # continue counting up the nodes
        self.cur_num_nodes += 1
# lru_list = LRUCache
# print(lru_list)