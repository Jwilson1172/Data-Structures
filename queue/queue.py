"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
        return

    def __str__(self):
        return str(self.storage)

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        print(f"size before: {self.size}")

        self.size = self.size + 1

        print(f"size after: {self.size}")

        self.storage.append(value)

        print(f"New object in storage:\n\t{self.__str__()}")
        return

    def dequeue(self):

        print(f"size before: {self.size}")
        print(f"Storage:\n\t{self.__str__()}")

        self.size = self.size - 1

        print(f"size after: {self.size}")
        if self.size == 0:
            return None
        else:
            value = self.storage.pop(0)

        print(f"Value that was popped: {value}")
        return value


if __name__ == "__main__":
    q = Queue()
    print("ADDING ITEMS TO THE QUEUE")
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(1)
    print(f"PRINTING QUEUE:\n{q}\nREMOVING QUEUED ITEMS")
    assert q.dequeue() == 1
    q.dequeue()
    q.dequeue()
