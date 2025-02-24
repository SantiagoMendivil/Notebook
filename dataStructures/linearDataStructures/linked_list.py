"""Nodes and Linked Lists classes"""

class Node:
    """Node class representing a node"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        """Get the node's value"""
        return self.value
    def get_next_node(self):
        """Get the next node of the node"""
        return self.next_node
    def set_value(self, value):
        """Set the node's value"""
        if value is not None:
            self.value = value
    def set_next_node(self, next_node):
        """Set the next node of the node"""
        if next_node is not None and isinstance(next_node, Node):
            self.next_node = next_node

class LinkedList:
    """Class for linked lists"""
    def __init__(self, value=None):
        """Initialize a linked list"""
        self.head_node = Node(value)

    def get_head_node(self):
        """Get the actual head node"""
        return self.head_node

    def insert_beginning(self, new_value):
        """Inserts a new node at the beginning of the list"""
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        """Returns a string representation of the linked list"""
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    def remove_node(self, node_to_remove):
        """
        Remove a node with a specific value from the linked list.

        This method searches for a node with the given value and removes it from the list.
        If the node to remove is the head node, it updates the head of the list.
        If the node is not found, the list remains unchanged.
        """
        current_node = self.get_head_node()
        if current_node.get_value() == node_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == node_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
    def swap_nodes(self, value1, value2):
        """
        Swap two nodes in the linked list based on their values.

        This function searches for two nodes with the given values and swaps their positions
        in the linked list. If the values are the same or if one or both values are not found,
        the function will print a message and return without making any changes.
        """
        print(f"Swapping {value1} with {value2}")
        node1_prev = None
        node2_prev = None
        node1 = self.get_head_node()
        node2 = self.get_head_node()

        if value1 == value2:
            print("Elements are the same")
            return

        while node1 is not None:
            if node1.get_value() == value1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == value2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1 is None or node2 is None:
            print("One or both elements not found")
            return

        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self.head_node = node2
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)
    def nth_last_node(self, n):
        """
        Find the nth last node in the linked list.

        This method uses two pointers to find the nth last node in a single pass.
        It maintains a gap of n nodes between the two pointers.

        Args:
            n (int): The position from the end of the list (1-indexed).

        Returns:
            The value of the nth last node if it exists, None otherwise.
            For example, if n=1, it returns the last node's value.
            If n is greater than the list length, it returns None.
        """
        current = None
        tail_seeker = self.head_node
        count = 1
        while tail_seeker:
            tail_seeker = tail_seeker.get_next_node()
            count += 1
            if count >= n + 1:
                if current is None:
                    current = self.head_node
                else:
                    current = current.get_next_node()
        return current.get_value() if current else None
    def find_middle_node(self):
        """
        Find the middle node of the linked list using the two-pointer technique.

        This method uses a fast pointer that moves twice as fast as a slow pointer.
        When the fast pointer reaches the end, the slow pointer will be at the middle.

        Returns:
            The value of the middle node if the list is not empty, None otherwise.
            For lists with an even number of nodes, it returns the second middle node.
        """
        fast_pointer = self.head_node
        slow_pointer = self.head_node
        while fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            if fast_pointer: # Checks if is not null and moves it again
                fast_pointer = fast_pointer.get_next_node()
                slow_pointer = slow_pointer.get_next_node()
        return slow_pointer.get_value() if slow_pointer else None
