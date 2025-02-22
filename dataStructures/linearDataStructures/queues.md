# Table of contents
- [Table of contents](#table-of-contents)

# Queues 
The node structure is almost the same as the linked list and doubly linked list structure. The queue itself just checks for the head and tail of the queue.
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

class Queue:
  def __init__(self):
    self.head = None 
    self.tail = None

  def peek(self):
    return self.head.get_value()
```

## Queues python size 
- A size property to keep track of the queue's current size
- A max_size property that bounded queues can utilize to limit the total node count 

```python
class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def peek(self):
    if self.is_empty():
      print("Nothig to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size

  def has_space(self):
    if self.max_size is None:
      return True
    else:
      return self.max_size > self.get_size()

  def is_empty(self):
    return self.size == 0
``` 

## Queues Python Enqueue
This is a fancy way of saying "add to a queue". There are three scenarios that we are concerned with when adding a node to the queue 

- The queue is empty, so the node we're adding is both the head and tail of the queue 
- The queue has at least one other node, so the added node becomes the new tail
- The queue is full so the node will not get added because we don't want queue "overflow"

```python 
def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")

      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add 
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
```


## Queues Python Dequeue 
When removing items from a queue, this must be done by removing the current head of the queue. 
There are three scenarios that we will take into account. 

- The queue is empty, so we cannot remove or return any nodes lest we run into queue "underflow"
- The queue has one node, so when we remove it, the queue will be empty and we need to rset the queue's head and tail to None.
- The queue has more than one node, and we just remove the head node and reset te head to the following node

```python 
def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")
```