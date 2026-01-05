"""
File Name: Middle_of_LinkedList.py

Problem:
Find the middle node of a Singly Linked List.

Description:
This program implements a Singly Linked List in Python and demonstrates
how to find the middle node using the **slow and fast pointer technique**.

Key Concepts Covered:
- Singly Linked List implementation
- Append and Prepend operations
- Displaying a linked list
- Removing a node
- Reversing a linked list
- Finding the middle node efficiently

Approach Used for Middle Node:
- Use two pointers (slow and fast)
- Slow pointer moves one step at a time
- Fast pointer moves two steps at a time
- When fast reaches the end, slow will be at the middle

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Node:
    """
    Represents a single node in the linked list.

    Attributes:
        value (int): Data stored in the node
        next (Node): Reference to the next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Represents a Singly Linked List.

    Attributes:
        head (Node): First node of the linked list
        tail (Node): Last node of the linked list
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Add a node at the end of the linked list.

        Args:
            value (int): Value to be added
        """
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """
        Add a node at the beginning of the linked list.

        Args:
            value (int): Value to be added
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if not self.tail:
            self.tail = new_node

    def display(self):
        """
        Display the elements of the linked list.
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
        first_node = current  # Will become the tail after reversal

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        self.tail = first_node

        print("Linked List Reversed:")
        self.display()

    def middle_node(self):
        """
        Find and return the middle node of the linked list.
        If there are 2 miidle nodes it returns the second middle node.

        Returns:
            Node: Middle node of the linked list
        """
        if not self.head:
            print("Linked List Empty")
            return None

        slow = fast = self.head     # Uses the slow and fast pointer technique to find the middle node.

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


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

    print(f"Middle Node of the Linked List: {ll.middle_node().value}")

    # Prepend elements
    ll.prepend(6)
    ll.prepend(7)
    ll.prepend(8)
    ll.display()

    print(f"Middle Node of the Linked List: {ll.middle_node().value}")
