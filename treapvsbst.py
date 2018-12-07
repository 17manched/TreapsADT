from treap import TreapNode, Treap
from BST import BSTNode, BST
from random import random
def heightrandom():
    for i in range(2,10,2):
        L = [100*random() for x in range((2**i)-1)]
        BSTTree = BST()
        TreapTree = Treap()
        for x in L:
            BSTTree.insert(x)
            TreapTree.insert(x)
        print("Complete Tree would have height of", i-1)
        print("Height of BST is: ", BSTTree.height())
        print("Height of Treap is: ", TreapTree.height())

def heightcorrelatedrandom():
    for i in range(2,10,2):
        L = [x*100*random() for x in range((2**i)-1)]
        BSTTree = BST()
        TreapTree = Treap()
        for x in L:
            BSTTree.insert(x)
            TreapTree.insert(x)
        print("Complete Tree would have height of", i-1)
        print("Height of BST is: ", BSTTree.height())
        print("Height of Treap is: ", TreapTree.height())

def heightordered():
    for i in range(2,10,2):
        L = [x*100 for x in range((2**i)-1)]
        BSTTree = BST()
        TreapTree = Treap()
        for x in L:
            BSTTree.insert(x)
            TreapTree.insert(x)
        print("Complete Tree would have height of", i-1)
        print("Height of BST is: ", BSTTree.height())
        print("Height of Treap is: ", TreapTree.height())
if __name__ == '__main__':
    print("***********************************")
    print("Random Height Test")
    heightrandom()
    print("***********************************")
    print("***********************************")
    print("Correlated Height Test")
    heightcorrelatedrandom()
    print("***********************************")
    print("***********************************")
    print("Ordered Height Test")
    heightordered()
    print("***********************************")
