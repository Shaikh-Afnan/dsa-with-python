"""
File Name: Doubly_Linked_List.py

Description:
This program demonstrates the implementation of a **Doubly Linked List**
using Python. It supports common operations such as:

- Appending elements to the end of the list
- Prepending elements to the beginning of the list
- Displaying the entire list
- Deleting the first occurrence of a given value

Each node in a doubly linked list contains:
- A reference to the previous node
- A reference to the next node
- A value/data field

This implementation is beginner-friendly and suitable for
DSA learning and interview preparation.

Time Complexity:
- Append: O(1)
- Prepend: O(1)
- Delete: O(n)
- Display: O(n)

Space Complexity:
- O(n) for storing n nodes
"""


class Node:
    """
    Represents a single node in a Doubly Linked List.

    Attributes:
        value (int): Data stored in the node
        prev (Node): Reference to the previous node
        next (Node): Reference to the next node
    """

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Doubly_LinkedList:
    """
    Represents a Doubly Linked List.

    Attributes:
        head (Node): First node of the list
        tail (Node): Last node of the list
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Add a node at the end of the doubly linked list.

        Args:
            value (int): Value to be added to the list
        """
        new_node = Node(value)

        # If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Attach new node at the end
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, value):
        """
        Add a node at the beginning of the doubly linked list.

        Args:
            value (int): Value to be added to the list
        """
        new_node = Node(value)

        # If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Attach new node at the beginning
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """
        Display the elements of the doubly linked list
        from head to tail.
        """
        if not self.head:
            print("List is Empty")
            return

        current_node = self.head
        elements = []

        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next

        print("Head ->", " <-> ".join(elements), "<- Tail")

    def delete(self, value):
        """
        Delete the first occurrence of a value from the doubly linked list.

        Args:
            value (int): Value to be deleted
        """
        if not self.head:
            print("List is empty!")
            return

        current_node = self.head

        while current_node:
            if current_node.value == value:

                # If node has a previous node
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    # Deleting the head node
                    self.head = current_node.next

                # If node has a next node
                if current_node.next:
                    current_node.next.prev = current_node.prev

                # If deleting the tail node
                if current_node == self.tail:
                    self.tail = current_node.prev

                return

            current_node = current_node.next


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    dll = Doubly_LinkedList()

    # Append elements
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.print_list()

    # Append and prepend more elements
    dll.append(5)
    dll.append(6)
    dll.append(7)
    dll.prepend(0)
    dll.prepend(-1)
    dll.print_list()

    # Delete operations
    dll.delete(3)
    dll.print_list()

    dll.delete(-1)
    dll.delete(7)
    dll.print_list()

