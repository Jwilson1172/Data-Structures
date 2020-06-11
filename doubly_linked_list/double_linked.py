import hashlib
import numpy as np
import datetime

# https://github.com/joeyajames/Python/blob/master/LinkedLists/DoublyLinkedList2.py
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
# commented and edited by https://github.com/Jwilson1172


class Node:
    def __init__(self, d, n=None, p=None):
        # set the data and the neighbor node pointers
        self.data = d
        self.next_node = n
        self.prev_node = p
        # adding hash values to atributes of a Node
        self.hash = hashlib.md5(self.data).hexdigest()

    def get_next(self):
        # return the next_node object
        return self.next_node

    def set_next(self, n):
        # set next_node object
        self.next_node = n

    def get_prev(self):
        # get pevious node object
        return self.prev_node

    def set_prev(self, p):
        # set the previous node object
        self.prev_node = p

    def get_data(self):
        # return the data value
        return self.data

    def set_data(self, d):
        """Set the data value and recompute the hash of this Node
        Arguments:
        ----------
        d {all} : the data that is going to get stored by the node
        returns:
        ----------
        None
        """
        # set the data value
        self.data = d
        self.hash = hashlib.md5(self.data).hexdigest()
        return

    def to_string(self):
        # return the value of the node in str form
        return f"Node value: {str(self.data)}\tHash(md5): {self.hash}"

    def has_next(self):
        # test if the node has a next node object
        if self.get_next() is None:
            return False
        return True


class DoublyLinkedList(object):
    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        """Checks is the list has any nodes if not then the first None in the
        list is the Node that is passed to the method.
        Arguments:
        ----------
        `d` {any} : Data to add to the Node object.
        Returns:
        --------
        None
        """
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.set_prev(new_node)
            self.root = new_node
        # add one to the len of the list
        self.size += 1

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                if this_node.get_prev() is not None:
                    # delete a middle node
                    if this_node.has_next():
                        this_node.get_prev().set_next(this_node.get_next())
                        this_node.get_next().set_prev(this_node.get_prev())
                    # delete last node
                    else:
                        this_node.get_prev().set_next(None)
                        self.last = this_node.get_prev()
                # delete root node
                else:
                    self.root = this_node.get_next()
                    this_node.get_next().set_prev(self.root)
                self.size -= 1
                # data removed
                return True
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == self.root:
                return False
            else:
                this_node = this_node.get_next()

    def print_list(self):
        print("Print List..........")
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())

    def to_numpy(self):
        this_node = self.root
        hashes = []
        values = []
        while this_node.has_next():
            this_node = this_node.get_next()
            values.append(self.root.data)
            hashes.append(self.root.hash)
        a = []
        for v, h in zip(values, hashes):
            a.append([v, h])

        return np.array(a)


def main() -> bool:
    try:
        myList = DoublyLinkedList()
        print("Example of using a doubly linked list")
        # making a structer of nodes that hold dictonary objects
        # the dictionary objects are transactions at a finacial institution
        myList.add(
            # add a deposit transaction as the first node to the list
            d=dict(
                {
                    "date": f"{datetime.date()}",
                    "trans_type": "depo",
                    "from_acc": 2,
                    "to_acc": 2,
                    "amt": 650.57,
                    "currency": "USD",
                }
            )
        )
        myList.add(
            # add a transfer as the next node in the list
            d=dict(
                {
                    "date": datetime.date(),
                    "trans_type": "xfer",
                    "from_acc": 3,
                    "to_acc": 22,
                    "amt": 350.00,
                    "currency": "USD",
                }
            )
        )
        myList.add(
            # add a withdrawl transaction
            d=dict(
                {
                    "date": datetime.date(),
                    "trans_type": "wthd",
                    "from_acc": 15,
                    "to_acc": 15,
                    "amt": 100.00,
                    "currency": "USD",
                }
            )
        )

        myList.add(
            # add a wiretransfer transaction
            d=dict(
                {
                    "date": datetime.date(),
                    "trans_type": "wire",
                    "from_acc": 2,
                    "to_acc": 1156,
                    "amt": 60.00,
                    "currency": "USD",
                }
            )
        )
        # now the data structure of the list in string should look like this but
        # neater
        # account_name:
        #  index, trans_type,     from_acc, amt,    to_acc,    hash
        #  [0],  'deposit',       acc[2],   650.57, acc[2],    HASH:str(hex(<md5sum>))
        #  [1],  'transfer',      acc[22],  350.00, acc[22],   HASH:str(hex(<md5sum>)
        #  [2],  'withdrawl',     acc[15],  100.00, acc[15],   HASH:str(hex(<md5sum>)
        #  [3],  'wire_transfer', acc[2],   60.00,  acc[1156], HASH:str(hex(<md5sum>)

        # should return 4
        print("size=" + str(myList.get_size()))
        myList.print_list()
        myList.remove(
            dict(
                {
                    "date": datetime.date(),
                    "trans_type": "wire",
                    "from_acc": 2,
                    "to_acc": 1156,
                    "amt": 60.00,
                    "currency": "USD",
                }
            )
        )
        print("size=" + str(myList.get_size()))
        print("Remove 15", myList.remove(15))

        # add a desposit
        myList.add(
            d=dict(
                {
                    "date": datetime.date(),
                    "trans_type": "deposit",
                    "from_acc": 2,
                    "to_acc": 2,
                    "amt": 100.00,
                    "currency": "USD",
                }
            )
        )

        # remove a withdrawl
        myList.remove(
            dict(
                {
                    "date": datetime.date(),
                    "trans_type": "wthd",
                    "from_acc": 15,
                    "to_acc": 15,
                    "amt": 100.00,
                    "currency": "USD",
                }
            )
        )
        myList.print_list()
        print("size=" + str(myList.get_size()))
        print(myList.last.get_prev().to_string())
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    main()
