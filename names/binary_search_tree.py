import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from doubly_linked_list import ListNode


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.queue = dll_queue()
        # self.stack = dll_stack()


    # Insert the given value into the tree
    def insert(self, value):
        new_node = BinarySearchTree(value)
        
        #adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
        # First check if root is empty, if value is < root, move value left and vice versa
        if value < self.value and self.left is None:
            self.left = new_node

        elif value < self.value and self.left is not None:
            self.left.insert(value)

        # Go down to the next node or "root", evaluate if value is < or > and move it to its appropriate side
        elif value >= self.value and self.right is None:
            self.right = new_node
            #self.right.insert(new_value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)   
       


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # 1. How do we check if a value is in a tree?
        if self.value is None:
            return False
        elif target == self.value:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value.
        # Cal cb function to self.value
        cb(self.value)
        # Call for each on on the right side so it can call cb on each value
        if self.right:
            self.right.for_each(cb)
        # call for each on the left side so it can call cb on each value
        if self.left:
            self.left.for_each(cb)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return   

        if node.left is not None:
            node.in_order_print(node.left)   
        print(node.value)
        if node.right is not None:
            node.in_order_print(node.right)
        
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Iterative BFT
        # Create queue
        queue = Queue()
        # # Add root to queue
        queue.enqueue(node)
        while queue.size != 0:
        # Pop node off queue
            deleted_node = queue.dequeue() 
            print(deleted_node.value)

            if deleted_node.left is not None:
                queue.enqueue(deleted_node.left)
            if deleted_node.right is not None:
                queue.enqueue(deleted_node.right)
       
        # Add children of node to queue
    

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Iterative DFT
        # Create Stack
        stack = Stack()
        # Add root to Stack
        stack.push(node)
        # while Stack is not empty, set node = pop top off Stack
        while stack.size != 0:
        # Pop node off Stack
            deleted_node = stack.pop()
        # Print
            print(deleted_node.value)
        # Add children of node to Stack
            if deleted_node.right is not None:
                stack.push(deleted_node.right)
            if deleted_node.left is not None:
                stack.push(deleted_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
