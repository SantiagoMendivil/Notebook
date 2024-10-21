# Table of contents
- [Table of contents](#table-of-contents)
- [Linked lists](#linked-lists)
  - [Common operations](#common-operations)
- [Linked Lists in Python](#linked-lists-in-python)
  - [Implement a Linked List](#implement-a-linked-list)

# Linked lists 
These are one of the basic data structures used in computer science. The list is comprised of a series of nodes where the **head node** is the node at the beginning of the list. Ecah node contains data and a link to the next node. The list is terminated when a **node's link is null**. 

## Common operations
- **Adding nodes**
- **Removing nodes**
- **Finding a node**
- **Traversing (Traveling through) the linked list**

# Linked Lists in Python 
In order to create a linked list in python we should first define the node class in python that contains the data and a link to the next node. This remembering to set the getters and the setter. 

## Implement a Linked List 
The main goals of creating a linked list are
- Get the head node of the list
- Add a new node to the beginning of the list
- Print out the list values in order 
- Remove a node that has a particular value

```Python 
class LinkedList():
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node
```

In the code above we generate a linked list with a value that can be None, and also inside of the constructor we set the head_node for that linked list to the first node with that value as argument. 

