import hashlib
import numpy as np

# https://github.com/joeyajames/Python/blob/master/LinkedLists/LinkedList2.py
#
# Licensed Under:
# The MIT License (MIT)
# Copyright © 2020 <copyright holders>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# commented by https://github.com/Jwilson1172


class Node(object):
    def __init__(self, d, n=None):
        """Set the data value for the node, supply next_node
        Arguments:
        ----------
        d {type(None)} : Data to be stored in the node.
        n {Node} : node object to use as next node
        Returns:
        ----------
        type(None)
        """
        self.data = d
        self.next_node = n
        # adding a hash value for the data
        self.hash = self.generate_hash()
        return None

    def generate_hash(self):
        return hashlib.md5(self.data).hexdigest()

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def to_string(self):
        return "Node value: " + str(self.data)

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

    def compare_to(self, y):
        if self.to_string() < y.to_string():
            return -1
        elif self.to_string() > y.to_string():
            return 1
        return 0


class LinkedList(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def add_node(self, n):
        n.set_next(self.root)
        self.root = n
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                # removing node that is not the root
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                # removing root node
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                # data removed
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        # data not found
        return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def print_list(self):
        print("Print List..........")
        if self.root is None:
            return
        current = self.root
        print(current.to_string())
        while current.has_next():
            current = current.get_next()
            print(current.to_string())

    def sort(self):
        if self.size > 1:
            newlist = []
            current = self.root
            newlist.append(self.root)
            while current.has_next():
                current = current.get_next()
                newlist.append(current)
            newlist = sorted(newlist, key=lambda node: node.get_data(), reverse=True)
            newll = LinkedList()
            for node in newlist:
                newll.add_node(node)
            return newll
        return self


if __name__ == "__main__":
    myList = LinkedList()
    myList.add(5)
    myList.add(9)
    myList.add(3)
    myList.add(8)
    myList.add(9)
    print("size=" + str(myList.get_size()))
    myList.print_list()
    myList = myList.sort()
    myList.print_list()
    myList.remove(8)
    print("size=" + str(myList.get_size()))
    print(myList.remove(12))
    print("size=" + str(myList.get_size()))
