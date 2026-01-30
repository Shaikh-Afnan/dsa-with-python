"""
File Name: Queue_Using_LinkedList.py

Description:
This program demonstrates the implementation of a **Queue data structure**
using a **Singly Linked List** in Python.

A queue follows the **FIFO (First In, First Out)** principle.

Operations implemented:
- enqueue(): Insert an element at the rear of the queue
- dequeue(): Remove and return the front element of the queue
- isempty(): Check whether the queue is empty

This implementation is beginner-friendly and suitable for
DSA practice and interview preparation.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- IsEmpty: O(1)

Space Complexity:
- O(n), where n is the number of elements in the queue
"""


class Node:
    """
    Represents a single node in the linked list used for queue implementation.

    Attributes:
        value (int): Data stored in the node
        next (Node): Reference to the next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Represents a Queue implemented using a linked list.

    Attributes:
        front (Node): Points to the front of the queue
        back (Node): Points to the rear of the queue
        size (int): Number of elements in the queue
    """

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def isempty(self):
        """
        Check whether the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise
        """
        return self.size == 0

    def enqueue(self, value):
        """
        Add an element to the rear of the queue.

        Args:
            value (int): Value to be added to the queue
        """
        new_node = Node(value)

        if self.isempty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

        self.size += 1

    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Returns:
            int: Value of the dequeued element
            None: If the queue is empty
        """
        if self.isempty():
            print("Queue is Empty")
            return None

        removed_item = self.front.value
        self.front = self.front.next
        self.size -= 1

        # If queue becomes empty after dequeue
        if self.isempty():
            self.back = None

        return removed_item


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    q1 = Queue()

    print("Is queue empty?", q1.isempty())

    # Enqueue elements
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)

    print("Is queue empty?", q1.isempty())

    # Dequeue elements
    print("Dequeued:", q1.dequeue())
    print("Dequeued:", q1.dequeue())
    print("Dequeued:", q1.dequeue())
    print("Dequeued:", q1.dequeue())

    print("Is queue empty?", q1.isempty())
