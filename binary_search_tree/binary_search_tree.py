import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTree(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BinarySearchTree(value)
                    break

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while True:
            if target == current.value:
                return True
            if target < current.value:
                if current.left:
                    current = current.left
                else:
                    return False  
            else:
                if current.right:
                    current = current.right
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        max_value = self.value
        while True:
            if current.right:
                current = current.right
                max_value = current.value
            else:
                return max_value

    # Call the function `cb` on the value of each node
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
        current = node
        if current.left:
            self.in_order_print(current.left)
        print(current.value)
        if current.right:
            self.in_order_print(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        current = node
        stack = Stack()
        stack.push(current)
        while stack.len() > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.right:
                stack.push(popped.right)
            if popped.left:
                stack.push(popped.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # if self.left:
        #     self.left.for_each(cb)
        # cb(self.value)
        # if self.right:
        #     self.right.for_each(cb)
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
