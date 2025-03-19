# Table of contents
- [Table of contents](#table-of-contents)
- [Key factors of data structure selection](#key-factors-of-data-structure-selection)
  - [What type of data are you working with?](#what-type-of-data-are-you-working-with)
  - [What operations will you be performing most frequently](#what-operations-will-you-be-performing-most-frequently)
  - [How much data are you dealing with](#how-much-data-are-you-dealing-with)
- [Alternative structures](#alternative-structures)
  - [Deque](#deque)
  - [Heapq (Priority queue)](#heapq-priority-queue)
  - [Collections.Counter](#collectionscounter)

# Key factors of data structure selection
## What type of data are you working with? 
- **Ordered Data**: Maintains a specific sequence. **Lists and tuples** are good choices. 
- **Unordered Data**: The order doesn't matter, such as a collection of users ID's. **Sets** are useful for this.
- **Mutable Data**: Can be changed after it's created, like a shopping cart. **Lists and dictionaties** are mutable. 
- **Immutable Data**: Cannot be changed once created, suchs as days of a week. **Tuples** are immutable. 

## What operations will you be performing most frequently
- **Adding/Removing**: **Lists** are great for adding/removing at the end, while **sets** and **dictionaries** provide fast addition/removal of unique items.
- **Searching**: **Dictionaries** excel at fast lookups by key, while **sets** are efficient for checking membership. 
- **Sorting**: If you need to keep your data in a specific order, consider structures like **lists** that support efficient sorting algorithms. 

## How much data are you dealing with
- **Small datasets**: The performance between data structures might not be noticeable. Any struture that accomplish the goal the easier way is good.
- **Large dataset**: Performance becomes critical. Carefully the time complexity of operations to avoid bottlenecks. For example, searching in a list can be much slower than searching in a dictionary. 

# Alternative structures

## Deque
A list but you can efficiently add or remove items from either end. It can be used when: 

- Implementing queues or stacks where you need to add/remove from both ends
- Simulating real-world scenarios like lines, decks of cards, undo/redo functionality.

## Heapq (Priority queue)
List that prioritize the smallest item (or the item with highest priority) putting it at the front of the queue 

- Task scheduling, where you need to prioritize tasks based on urgency or importance
- Dijkastra's algorithm for finding the shortest path in a graph
- Implementing priority-based system. 

## Collections.Counter
This module takes an iterable (list or string) and counts the occurences of each unique item. 

- Analyzing word frequency in a text
- Counting the occurence of items in a list
- Finding the most common elements in a dataset.

```python 
from collections import deque, Counter 

queue = deque()
queue.append("Task 1")
queue.append("Task 2")
print(queue.popleft())

text = "This is a sample text with some repeated words words"
word_counts = Counter(text.split())
print(word_counts)
```