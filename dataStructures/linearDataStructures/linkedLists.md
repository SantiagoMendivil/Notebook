# Table of contents
- [Table of contents](#table-of-contents)
- [Linked lists](#linked-lists)
  - [Common operations](#common-operations)
- [Linked Lists in Python](#linked-lists-in-python)
  - [Implement a Linked List](#implement-a-linked-list)
    - [First step](#first-step)
    - [Second step](#second-step)
    - [Third step](#third-step)

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
### First step
The main goals of creating a linked list are
- Get the head node of the list
- Add a new node to the beginning of the list
- Print out the list values in order 
- Remove a node that has a particular value

```Python 
class LinkedList():
  def __init__(self, value=None):
    """ Generates a new node that represents the head """
    self.head_node = Node(value)

  def get_head_node(self):
    """ Returns the head node """
    return self.head_node
```

In the code above we generate a linked list with a value that can be None, and also inside of the constructor we set the head_node for that linked list to the first node with that value as argument. 



### Second step
In the first step we can create a linked list and get its head_node. Now let's see how to insert a new head_node and return all the nodes in the list as a string

```Python
class LinkedList:
  def __init__(self, value=None):
    """ Generates a new node that represents the head """
    self.head_node = Node(value)
  
  def get_head_node(self):
    """ Returns the head node """
    return self.head_node
  
  def insert_beginning(self, new_value):
    """ Generates a new node. Links it to the current head and sets
        the new node as the new head node.
    """
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    """ Takes the current head node. Verifies if the value is different than none, if so, adds the value to the string. Then moves into the next node. 
    """
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list


```
### Third step
Now we have to implement how to remove an arbitrary node with a particular value. 

```Python
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.head_node

    if self.head_node.get_value() == value_to_remove:
      self.head_node = self.head_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
```