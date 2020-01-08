import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # create a new node that contains the element.
        node = BinarySearchTree(value)
        # if the root value is null set the root to the node
        # if self.value is None:
        #     self.value = node
        #     print('self.value', self.value)
        #     print('value', value)
        #     print('node', node)
        #     return node
        if value < self.value:
        # if the new node value is less than the root node, insert left
            # if value is to the left, insert left
            print('traversing the value to the left (parent)', value)
            if self.left is None:
                print('value in self.left...', value)
                # sets the node for the value
                self.left = node
            else:
                # inserts values to the left of the parent node (not necessarily root node)
                # this is the final step in the insertion for the value being passed
                self.left.insert(value)
                
                # print('value in self.left... ELSE', self.left.insert(value))
                # self.left.value = None
            # else insert right
        elif value >= self.value:
            print('traversing the value to the right (parent)', value)
            if self.right is None:
                print('value of right self.right', value)  
                self.right = node
            else:
                self.right.insert(value)
                # print('value in self.right... ELSE', self.right.insert(value))
                # self.right.value = None
     # possibly can be removed   
        return value
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        print('target', target)
        
        if self.value == target:
            print('self.value', self.value)
            print('target printed', target)
            #returns true if the root node (self.value) is equal to the target. 
            return True
        # elif self.left == target:
        if target < self.value:
            if self.left is None:
                return False
        #    print('if less than the node target', self.left.contains(target))
            # print('CONTAINS IF LESS', target)
            print('CONTAINs self.value LESS', self.left.contains(target))
            node = self.left.contains(target)
            return node
        elif target > self.value:
            if self.right is None:
                print('value is not in the binary search tree!', self.value)
                return False
            # print('CONTAINS GREATER self.value', self.value.contains(target))
            print('CONTAINS IF GREATER', target)
            print('CONTAINs self.value MORE', self.right.contains(target))
            node = self.right.contains(target)
            return node
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` (callback..) on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



binary_search = BinarySearchTree(5)
print(binary_search.insert(2))
print(binary_search.insert(3))
print(binary_search.insert(7))
print(binary_search.insert(8))
print(binary_search.contains(3))
print(binary_search.contains(4))
print(binary_search.contains(5))
