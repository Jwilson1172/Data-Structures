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
import numpy as np
import hashlib as hl


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        return

    def pop(self):
        return self.storage.pop()

    def __str__(self):
        return str(np.array(self.storage))


s = Stack()
s.push("name")
s.push(1234)
s.push("")
print(s.pop())
print(s.pop())
print(s.pop())


class HashyNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.hash = None
        self.nextval = None
        self.nexthash = None
        self.lastval = None
        self.lasthash = None
        return

    def check_neighbors(self):
        """A function to check all of the neighbor hashes to make sure that
        they are responding with the right hashes, then check the hash of this node
        against the stored hash.
        Arguments:
        ---------------
        None
        Returns:
        ---------------
        verified: {bool} - will either be true or false for checksum verification
        may also return {str} 'WARN' which means that the neighbors checksums
        verified but that the content of this node is out of date of compromised
        """
        if self.nexthash == self.nextval.generate_hash() & (
            self.lasthash == self.lastval.generate_hash()
        ):
            if self.generate_hash() == self.hash:
                self.verified = True
            else:
                self.varified = "WARN"
        else:
            self.verified = False
        return

    def generate_hash(self):
        """Function returns the hash of the dataval
        """
        return hl.md5(self.dataval).hexdigest()

    def addNode(self, node: HashyNode):
        self.nextval = node
        self.nextval.lasthash = self.generate_hash()
        self.nexthash = self.nextval.generate_hash()
        return

    def __str__(self):
        return str(self.linked_list)


class LinkedListStack:
    def __init__(self):
        self.originNode = None

    def gen_OriginNode(self, node: HashyNode):
        self.originNode.nextval = node
        self.originNode.lastval = "Origin"



DBG = True
if DBG:
    print("making linked list object")
list1 = LinkedListStack()
list1.originNode = HashyNode("Mon")
if DBG:
    print("Setting headval of LL1 to Node('Mon')")
e2 = HashyNode("Tue")
e3 = HashyNode("Wed")
print("making nodes e2=Node('Tue') and e3=Node('Wed')")
print("Link first Node to second node")
# Link first Node to second node
list1.headval.nextval = e2
print("link second node to thrid node")
# Link second Node to third node
e2.nextval = e3
