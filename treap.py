from random import random
class Node:
    # Creates a Node with a value and possibly a left and right child
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._num = random()
        self._left = left
        self._right = right

    #How a node is displayed as a string
    def __str__(self):
        return str(self._value)

    #Sees if a key is in the Treap with normal search in a BST
    def get(self, key):
        if self._value > key:
            if self._left:
                return self._left.get(key)
            return False
        if self._value < key:
            if self._right:
                return self._right.get(key)
            return False
        else:
            return True

    #Rotates tree with this node as root to the left
    def rotateleft(self):
        A = self
        B = A._left
        C = A._right
        D = B._left
        E = B._right
        F = C._left
        G = C._right
        C._left = A
        A._right = F
        return C


    #Rotates tree with this node as root to the right
    def rotateright(self):
        A = self
        B = A._left
        E = B._right
        A._left = E
        B._right = A
        return B

    #Insert a new item into the Treap
    def insert(self, value, node = None):
        #Checks to see if the value is the node value
        if self._value == value:
            raise allreadyinthere
        #Insert into left subtree
        if self._value > value:
            if self._left:
                self._left.insert(value, node)
            else:
                self._left = node
            #Checks to see if Treap has max-value heap property
            if self._num < self._left._num:
                return self.rotateright()
            #Insert into right subtree case
            elif self._value < value:
                if self._right:
                   self._right.insert(value, node)
                else:
                   self._right = node
            #Checks to see if Treap has max-value heap property
            if self._num < self._right._num:
                return self.rotateleft()
        return self

    #Displays an in order Traversal with this node as root
    def display(self):
        if self._left:
            print('(',end='')
            self._left.display()
            print(')',end='')
        print(self,end=':')
        print(self._num, end='')
        if self._right:
            print('(',end='')
            self._right.display()
            print(')',end='')


class Treap:
    #Create a new instance of a Treap, takes no parameters and keeps the root node and its length
    def __init__(self):
        self._root = None
        self._length = 0

    #Insert a new item into the Treap
    def insert(self, value):
        node = Node(value)
        if self._root:
            self._root = self._root.insert(value, node)
        else:
            #Case if there is no root
            self._root = node
        #Increases length
        self._length += 1

    #Sees if a key is in the Treap with normal search in a BST
    def get(self, key):
        return self._root.get(key)

    #Displays an in order Traversal
    def display(self):
        self._root.display()

    #Deletes a node with the key value if it is in the Treap
    def delete(self, key):
        if self._root._value == key:
            if self._root._left == None:
                self._root = self._root._right
            if self._root._right == None:
                self._root = self._root._left

    #Returns length (amount of nodes) in the Treap
    def __len__(self):
        return self._length
if __name__ == '__main__':
    W = Treap()
    W.display()
