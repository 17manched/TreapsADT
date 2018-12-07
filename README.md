# TreapsADT
ADT for Treaps
This project is an implementation of the Treap abstract data type. The purpose of a Treap ADT is to to keep a binary search tree that also maintains a heap priority status where each node is given a random priority when it is inserted.

The key functions of the Treap ADT are:

Insert(key): Inserts a new node into the tree as long as the key is not already in the Treap while maintaining BST and random priority status.

Delete(key): Removes the node with a given key from the Treap while mantating BST and heap status.

Display: Prints out an in order traversal of the tree with indentation to indicate levels

Height: Returns the height of the tree, which is the maximum number of nodes from the root to a leaf

__contains__(key): Returns True if a given key is in the Treap and returns False otherwise

__len__: Returns the number of nodes in the Treap

