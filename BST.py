class BSTNode:
    # Creates a Node with a value and possibly a left and right child
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right
        self._height = 0

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

    def updateheight(self):
        if self._left is None and self._right is None:
            self._height = 0
            return self._height
        if self._left is None:
            self._height = 1 + self._right.updateheight()
            return self._height
        if self._right is None:
            self._height = 1 + self._left.updateheight()
            return self._height
        self._height = 1 + max(self._left.updateheight(), self._right.updateheight())
        return self._height
    #Rotates tree with this node as root to the left

    #Insert a new item into the Treap
    def insert(self, value, node = None):
        #Checks to see if the value is the node value
        if self._value == value:
            raise allreadyinthere
        #Insert into left subtree
        if self._value > value:
            if self._left:
                self._left = self._left.insert(value, node)
            else:
                self._left = node
            #Checks to see if Treap has max-value heap property
            return self
            #Insert into right subtree case
        elif self._value < value:
            if self._right:
                self._right = self._right.insert(value, node)
            else:
                self._right = node
            return self

    #Displays an in order Traversal with this node as root
    def display(self, offset=0):
        offset += 2
        if self._left:
            self._left.display(offset)
        print(' ' * offset, end='')
        print(self,end=' : ')
        print(self._num)
        if self._right:
            self._right.display(offset)

    def delete(self, key):
        if self._value > key:
            if self._left:
                self._left = self._left.delete(key)
                return self
            return None
        elif self._value < key:
            if self._right:
                self._right = self._right.delete(key)
                return self
            return None
        elif self._value == key:
            self = self.deletethisnode()
            return self

    def deletethisnode(self):
        if self._left is None:
            self = self._right
            return self
        elif self._right is None:
            self = self._left
            return self
        elif self._left._num > self._right._num:
            self._right = self._right.deletethisnode()
            return self
        else:
            self._left = self._left.deletethisnode()
            return self

    def height(self):
        self.updateheight()
        return self._height
class BST:
    #Create a new instance of a Treap, takes no parameters and keeps the root node and its length
    def __init__(self):
        self._root = None
        self._length = 0

    #Insert a new item into the Treap
    def insert(self, value):
        node = BSTNode(value)
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
        if len(self) == 0:
            return None
        self._root.updateheight()
        self._root.display()

    #Deletes a node with the key value if it is in the Treap
    def delete(self, key):
        if self._root:
            self._root = self._root.delete(key)

    #Returns length (amount of nodes) in the Treap
    def __len__(self):
        return self._length

    def height(self):
        return self._root.height()
