# Table of contents
- [Table of contents](#table-of-contents)
- [Nodes](#nodes)
  - [Node detail](#node-detail)
  - [Node linking](#node-linking)
- [Nodes in Python](#nodes-in-python)
  - [Nodes Python Getters](#nodes-python-getters)
  - [Nodes Python Setter](#nodes-python-setter)

# Nodes 
Nodes are the fundamental building blocks of many computer science data structures. An individual node contains data and links to other nodes. 

## Node detail
The data contained within a node can be a variety of types, depending on the language you are using. 
The links within the node are sometimes referred as pointers. 

## Node linking
When you have more that one node linked to each other, suppose we have node_a, node_b and node_c. If tou delete node_b without specifying the connection between node_a and node_c, then node_c will be lost because there is no longer a connection to that memory address. 

# Nodes in Python
Nodes in python are classes that hold the value that the node contains and the links for that node, that by default will always be None. 

```Python
class Node():
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
```

## Nodes Python Getters 
In order to access the node's data we have to set som getters for getting the node's value and the node's links. 

```Python
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node
``` 

## Nodes Python Setter
We are receiving a link to a default None parameter, but what if we want to connect it with another node? Here we implement the setters. 

```Python
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node

  def set_link_node(self, link_node):
    self.link_node = link_node
```