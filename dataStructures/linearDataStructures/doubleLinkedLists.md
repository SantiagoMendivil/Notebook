# Table of contents 
- [Table of contents](#table-of-contents)
- [Doubly Linked Lists Introduction (Conceptual)](#doubly-linked-lists-introduction-conceptual)
  - [Common operations](#common-operations)
  - [Adding to the head](#adding-to-the-head)
  - [Adding to the tail](#adding-to-the-tail)
  - [Removing the head](#removing-the-head)
  - [Removing the tail](#removing-the-tail)
  - [Removin from the middle of the list](#removin-from-the-middle-of-the-list)
- [Nodes in double linked lists (Implementation)](#nodes-in-double-linked-lists-implementation)
- [Definition of double linked list](#definition-of-double-linked-list)
  - [Adding to the head](#adding-to-the-head-1)


# Doubly Linked Lists Introduction (Conceptual)
Is comprised of a series of nodes. Each node contains data and two links (or pointers) to the next and previous nodes in the list. 

The head node is the node at the beginning of the list, and the tail node is the node at the end of the list. 
The head node's previous pointer is set to null and the tail node's pointer is set to null. 
 
 ## Common operations 
 - **Adding nodes to both ends of the list**
 - **Removing nodes from both ends of the list**
 - **Finding, and removing a node from anywhere in the list**
 - **Traversing (or traveling through) the list**

## Adding to the head
If the list is empty
- Check if there is a current head to the list.
- Make our new node both the head and tail to the list and set both pointers to null

If the list is not empty, then: 
- Set the current head's previous pointer to our new head 
- Set the new head's next pointer to the current head
- Set the new head's previous pointer to null 

## Adding to the tail 
If the list is empty
- Make the new node the head and tail of the list and set the pointers to null

If the list is not empty
- Set the current tail's next pointer to the new tail 
- Set the new tail's previous pointer to the current tail 
- Set the new tail's next pointer to null. 

## Removing the head
This involves updating the pointer at the beginning of the list. We will set the previous pointer of the new head to null, and update the head property of the list. If the head was also the tail, the tail removal process will occur as well. 

## Removing the tail
Similarly, removing the tail involves updating the pointer at the end of the list. We will set the next pointer of the new tail (the element directly before the tail) to null, and update the tail property of the list. If the tail was also the head, the head removal process will occur as well. 

## Removin from the middle of the list 
- We must set the removed node’s preceding node’s next pointer to its following node
- We must set the removed node’s following node’s previous pointer to its preceding node


# Nodes in double linked lists (Implementation)
The node is slightly different in a double linked lists. In this case you need a value, a pointer to the previous node and a pointer to the next node. 
The methods for this kind of node are 
- Add a new node to the head (beginning) of the list 
- Add a new node to the tail (end) of the list 
- Remove a node from the head of the list 
- Remove a node from the tail of the list 
- Find and remove a specific node by its value 
- Print out the nodes in the list in order from head to tail 

```Python 
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
```


# Definition of double linked list 
In the constructor we won't receive any parameter because a double linked list will start as an empty list. 

```Python 
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
```

## Adding to the head
- Start by checking to see if there is a current head to the list 
- If there is, then we want to reset the pointers at the head of the list
- Set the current head's previous node to the new head 
- Set the new head's next node to the current head 
- Update the head property to be the new head 
- Finally, if there isn't a current tail to the list (meaning the list was empty)
- Update the tail property to be the new head since that node will be both the head and tail of the list. 