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
        #     return node
        if value < self.value:
        # if the new node value is less than the root node, insert left
            # if value is to the left, insert left
            # print('traversing the value to the left (parent)', value)
        # if there is no self.left value
            if self.left is None:
            # # or could have wrote if not self.left
            #     print('value in self.left...', value)
                # sets the new left child to be the new value
                self.left = node
            else:
                # inserts values to the left of the parent node (not necessarily root node)
                # this is the final step in the insertion for the value being passed
                self.left.insert(value)
                
                # print('value in self.left... ELSE', self.left.insert(value))
                # self.left.value = None
            # else insert right
        else:
            # print('traversing the value to the right (parent)', value)
            if self.right is None:
                # print('value of right self.right', value)  
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
        # print('target', target)
        
        if self.value == target:
            # print('self.value', self.value)
            # print('target printed', target)
            #returns true if the root node (self.value) is equal to the target. 
            return True
        # elif self.left == target:
        if target < self.value:
            if self.left is None: # could also be "if not self.left"
                # print('value is not in the binary search tree! LEFT SIDE', target)
                return False
        #    print('if less than the node target', self.left.contains(target))
            # print('CONTAINS IF LESS', target)
            # print('CONTAINs self.value LESS', self.left.contains(target))
            node = self.left.contains(target)
            return node
        elif target > self.value:
            if self.right is None:
                # print('value is not in the binary search tree! RIGHT SIDE', target)
                return False
            # print('CONTAINS GREATER self.value', self.value.contains(target))
            # print('CONTAINS IF GREATER', target)
            # print('CONTAINs self.value MORE', self.right.contains(target))
            node = self.right.contains(target)
            return node
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = 0
        # EDGE CASE:
        # if there are no values in self.right, print the root node
        if self.right is None:
            max_value = self.value
            # print('max value as self.value', max_value)
            return self.value
        while self.right is not None:
            # print('max_value...', max_value)
            # print('self.value', self.value)
            max_value = self.right.value
            print('max_value in while loop', max_value)
            # print('get max recursion', self.right.get_max())
            return self.right.get_max()
    def get_max2(self):
        if not self.right:
            return self.value
        while self.right is not None:
            return self.right.get_max2()           
           
        # traverse right side of tree until null is found. 
        # this mean last value found on the right side of tree is max value
        # return max_value
    # def get_max2(self):
    #     while self.right is not None:
    #         return self.right.get_max2()
    #     else:
    #         return self.value

    # Call the function `cb` (callback..) on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            # print(node.in_order_print(node.left))
            print(self.value)
            # print('node', node)
            return
    
        # print(self.left.in_order_print(node.left))
        # self.left.in_order_print(node.left)
        # print(node.value)
        # self.right.in_order_print(node.right)
        print(self.value)
        return self.value

        # if node is not None:
        #     print(self.value)
        #     # print('node', node)
        #     return
        # print the current node
        # print('printing node(self.value): ', node(self.value))
        # node(self.value, node)
        # if self.value:
        ## will go all the way to the left, then bubble back up then go to the right
            # go left if you can 
            # print(self.left.in_order_print(node))
        # print(self.left.in_order_print(node))
        # if self.left:
        #     self.left.in_order_print(node.right)
        #     print('self.left', self.left)
        #     print(node.value)
        # if self.right:
        #     self.right.in_order_print(node.left)
        #     print(node.value)
        # return self.value
        # if self.right:
            # go right if you can
            # self.right.in_order_print(node)
        ## they do not get executed at the same time!
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack to keep track of nodes
        # place the first node onto stack

        # while stack is not empty:
            #pop the top node
            #print he node
            #add children to the stack 
            # remember which children to add first
            # because that changes the output order



        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



# binary_search = BinarySearchTree(5)
# print(binary_search.insert(2))
# print(binary_search.insert(3))
# print(binary_search.insert(7))
# print(binary_search.insert(8))
# print(binary_search.contains(3))
# print(binary_search.contains(4))
# print(binary_search.contains(5))
# print(binary_search.get_max(), 5)
# print(binary_search.insert(30))
# print(binary_search.get_max(), 30)
# print(binary_search.insert(300))
# print(binary_search.insert(3))
# print(binary_search.get_max(), 300)

# print(binary_search.get_max2(), 5)
# print(binary_search.insert(31))
# print(binary_search.get_max2(), 31)
# print(binary_search.insert(301))
# print(binary_search.insert(31))
# print(binary_search.get_max2(), 301)