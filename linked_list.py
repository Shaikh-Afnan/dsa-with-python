"""
Linked List Implementation in Python

This module demonstrates a simple implementation of a
singly linked list along with common operations such as:
- append
- prepend
- remove
- display

Author: Shaikh Afnan
"""

class Node:
    """
    Represents a single node in a linked list.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Add a node to the end of the linked list.
        """
        new_node = Node(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """
        Add a node to the beginning of the linked list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if not self.tail:
            self.tail = new_node

    def display(self):
        """
        Display all elements of the linked list.
        """
        if not self.head:
            print("Linked List is empty")
            return

        current = self.head
        elements = []

        while current:
            elements.append(str(current.value))
            current = current.next

        print(" -> ".join(elements))

    def remove(self, value):
        """
        Remove the first occurrence of a value from the linked list.
        """
        if not self.head:
            print("Linked List is empty")
            return

        # If head needs to be removed
        if self.head.value == value:
            self.head = self.head.next
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


# ------------------ Example Usage ------------------

if __name__ == "__main__":
    ll = LinkedList()

    ll.append(5)
    ll.append(4)
    ll.append(3)
    ll.display()

    ll.remove(3)
    ll.display()

    print("Prepending values...")
    ll.prepend(6)
    ll.prepend(7)
    ll.display()

    ll.remove(4)
    ll.display()
