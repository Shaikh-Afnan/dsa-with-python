"""
File Name: leetcode_Challenge_Reversing_a_LinkedList.py

Problem:
Reverse a Singly Linked List.

Description:
This program implements a Singly Linked List in Python and demonstrates
how to reverse the linked list using an iterative approach.

The implementation includes:
- Creating a Node
- Appending elements to the list
- Prepending elements to the list
- Removing an element
- Reversing the linked list
- Displaying the linked list

This is a beginner-friendly implementation with clear logic and comments.
"""


class Node:
    """
    A Node represents a single element in the linked list.

    Attributes:
        value (int): The data stored in the node
        next (Node): Reference to the next node in the linked list
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    A class to represent a Singly Linked List.

    Attributes:
        head (Node): The first node of the linked list
        tail (Node): The last node of the linked list
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Add a node to the end of the linked list.

        Args:
            value (int): Value to be added to the list
        """
        new_node = Node(value)

        # If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """
        Add a node to the beginning of the linked list.

        Args:
            value (int): Value to be added to the list
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        # If the list was empty
        if not self.tail:
            self.tail = new_node

    def display(self):
        """
        Display all elements of the linked list.
        """
        if not self.head:
            print("Linked List Empty!")
            return

        iterator = self.head
        elements = []

        while iterator:
            elements.append(str(iterator.value))
            iterator = iterator.next

        print(" -> ".join(elements))

    def remove(self, value):
        """
        Remove the first occurrence of a value from the linked list.

        Args:
            value (int): Value to be removed
        """
        if not self.head:
            print("Linked List Empty")
            return

        # If the head node contains the value
        if self.head.value == value:
            self.head = self.head.next

            # If list becomes empty after removal
            if not self.head:
                self.tail = None

            print(f"{value} removed from the linked list")
            return

        current = self.head

        while current.next:
            if current.next.value == value:
                current.next = current.next.next

                # Update tail if last node is removed
                if not current.next:
                    self.tail = current

                print(f"{value} removed from the linked list")
                return

            current = current.next

        print(f"{value} not found in the linked list")

    def reverse(self):
        """
        Reverse the linked list using an iterative approach.
        """
        if not self.head:
            print("Linked List Empty!")
            return

        current = self.head
        prev = None
        first_node = current  # Will become the new tail after reversal

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        self.tail = first_node

        print("Linked List Reversed:")
        self.display()


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Append elements
    ll.append(5)
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(1)
    ll.display()

    # Prepend elements
    ll.prepend(6)
    ll.prepend(7)
    ll.prepend(8)
    ll.display()

    print(
        f"Head of Linked List: {ll.head.value}, "
        f"Tail of Linked List: {ll.tail.value}"
    )

    # Reverse the linked list
    ll.reverse()

    print(
        f"Head of Linked List: {ll.head.value}, "
        f"Tail of Linked List: {ll.tail.value}"
    )
