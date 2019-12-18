"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
        ## can type in len(DoublyLinkedList)
    
    def print(self):
      curr_node = self.head
      print(curr_node)
      while curr_node.next is not None:
        curr_node = curr_node.next
        print(curr_node)

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""


# """the value/new node is the actual data/number.
# # next = move right aka towards the tail
# # previous = move left aka towards head
# # head                       tail
# # [1,       2,        3,        4]

# # next and previous are managing the pointers. not actual data """

    def add_to_head(self, value):
        # current_head = self.head
        new_node = ListNode(value)
        self.length += 1
        # this is the first element in the list
        # we have to modify both the head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else: 
            # this helps to link the new node to the head. i.e. put 0 in front of 1, if 1 was the head
            ## the below is okay, but insert_before is more clean?
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            ## this is a helper, some say the helper is more confusing. 
            # self.head.insert_before(value)

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
    # if self.prev:
    #     self.prev.next = self.next
    # if self.next:
    #     self.next.prev = self.prev

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and self.tail:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        # if node is self.tail:
        #     self.remove_from_tail()
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return 
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head == node:
            self.head = node.next # or self.head.next (it's the same thing)
            self.length -= 1
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass

first_node = ListNode(100)
linked_list = DoublyLinkedList()
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)

linked_list.print()
print(linked_list.head)
print(len(linked_list))

linked_list.delete(first_node)
linked_list.remove_from_head()
linked_list.print()
print('---------------')
linked_list.remove_from_tail()
linked_list.print()