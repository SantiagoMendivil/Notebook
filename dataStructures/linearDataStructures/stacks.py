class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def set_next_node(self, next_node):
        self.next_node = next_node
        
    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value
    
    
class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
    
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("All out of space!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This stack is totally empty.")
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Nothing to see here!")
        
    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0
  
  
"""
Fibonacci Sequence
How it works:
1. The base cases are n = 0 and n = 1, which return 0 and 1 respectively.
2. For any n > 1, the function calls itself twice:
   - Once for (n-1) and once for (n-2)
3. It then adds the results of these two recursive calls.
4. This process continues, breaking down the problem into smaller subproblems,
   until it reaches the base cases.
Note: This recursive approach is not efficient for large values of n due to
      repeated calculations. For large n, consider using dynamic programming
      or iterative approaches.
"""

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

