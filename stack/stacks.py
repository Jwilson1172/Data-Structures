# Stack
from collections import deque
stack = deque()
print("Stack:")
print(stack)
stack.append(1)
stack.append(2)
stack.appendleft(3)
print(stack)

# Queues
from queue import Queue
q = Queue()
print("Queue:\n")
print(f"max size: {q.maxsize}", end="\n\n")
