"""
File Name: Stack_Using_LinkedList.py

Description:
This program demonstrates the implementation of a **Stack data structure**
using a **Singly Linked List** in Python.

A stack follows the **LIFO (Last In, First Out)** principle.

Operations implemented:
- push(): Insert an element at the top of the stack
- pop(): Remove and return the top element of the stack
- isempty(): Check whether the stack is empty

This implementation is beginner-friendly and suitable for
DSA learning, practice, and interview preparation.

Time Complexity:
- push: O(1)
- pop: O(1)
- isempty: O(1)

Space Complexity:
- O(n), where n is the number of elements in the stack
"""


class Node:
    """
    Represents a single node in the linked list used for stack implementation.

    Attributes:
        value (int): Data stored in the node
        next (Node): Reference to the next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Represents a Stack implemented using a linked list.

    Attribute:
        top (Node): Reference to the top element of the stack
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Push an element onto the stack.

        Args:
            value (int): Value to be added to the stack
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Remove and return the top element of the stack.

        Returns:
            int: Value of the popped element
            None: If the stack is empty
        """
        if self.isempty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None

        popped_item = self.top.value
        self.top = self.top.next
        return popped_item

    def isempty(self):
        """
        Check whether the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise
        """
        return self.top is None


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    my_stack = Stack()

    print("Check if the stack is empty:", my_stack.isempty())

    # Push elements
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("Check if the stack is empty:", my_stack.isempty())

    # Pop elements
    print("Popped:", my_stack.pop())
    print("Popped:", my_stack.pop())
    print("Popped:", my_stack.pop())

    print("Check if the stack is empty:", my_stack.isempty())
