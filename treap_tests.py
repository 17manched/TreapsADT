from treap import *
import unittest
from random import random

class TestLabFunctions(unittest.TestCase):
    def testinsert(self):
        W = Treap()
        W.insert(2)
        self.assertTrue(2 in W)

    def testinsert2(self):
        T = Treap()
        T.insert(10)
        T.insert(30)
        T.insert(2)
        T.insert(20)
#        T.display()
        self.assertTrue(2 in T)
        self.assertTrue(10 in T)
        self.assertTrue(20 in T)
        self.assertTrue(30 in T)

    def testcontains(self):
        T = Treap()
        for i in range(100):
            T.insert(i)
        self.assertTrue(30 in T)

    #Delete does not work properly yet
    def testdelete(self):
        R = Treap()
        R.insert(1)
        R.insert(2)
        R.insert(3)
        R.insert(4)
        R.insert(5)
#        R.display()
        R.delete(2)
#        R.display()
        self.assertFalse(2 in R)

    def testlen(self):
        L = []
        M = Treap()
        for x in range(100):
            L.append(1000*random())
        for v in L:
            M.insert(v)
#        M.display()
        self.assertEqual(len(M),100)
        M.insert(25)
        self.assertEqual(len(M),101)
        M.delete(25)
        self.assertEqual(len(M),100)

if __name__ == '__main__':
    unittest.main()
