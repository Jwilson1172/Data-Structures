"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# from collections import deque


class Stack:
    def __init__(self):
        self.d = []
        self.size = 0
        return

    def push(self, d):
        self.d.append(d)
        self.size = self.size + 1
        return

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size = self.size - 1
            return self.d.pop()

    def __str__(self):
        return str(self.d)

    def __len__(self):
        return self.size

    def has_next(self) -> bool:
        if len(self.d) > 0:
            return True
        else:
            return False


# class Node:

# class LinkedListStack:


if __name__ == "__main__":
    s = Stack()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    while s.has_next():
        print(s.dequeue())
