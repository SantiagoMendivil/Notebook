# Table of contents 
- [Table of contents](#table-of-contents)

# Nodes for stacks 
```python 
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
``` 


# Stack in Python 
```python 
class Stack:
  def __init__(self, limit=1000):
    self.size = 0
    self.limit = limit
    self.top_item = None
  
  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
    # Decrement the stack size here:
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The stack is empty")
  
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("The stack is empty")
```