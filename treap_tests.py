from treap import *
import unittest
from random import random

class TestLabFunctions(unittest.TestCase):
    def testinsert(self):
        W = Treap()
        W.insert(2)
        self.assertTrue(W.get(2))

    def testinsert2(self):
        T = Treap()
        T.insert(10)
        T.insert(30)
        T.insert(2)
        T.insert(20)
        T.display()
        self.assertTrue(T.get(2))
        self.assertTrue(T.get(10))
        self.assertTrue(T.get(20))
        self.assertTrue(T.get(30))

    def testget(self):
        T = Treap()
        for i in range(100):
            T.insert(i)
        self.assertTrue(T.get(30))

    #Delete does not work properly yet
    def testdelete(self):
        R = Treap()
        R.insert(10)
        R.insert(20)
        R.insert(30)
        R.delete(20)
        self.assertFalse(R.get(20))

    def testlen(self):
        L = []
        M = Treap()
        for x in range(100):
            L.append(1000*random())
        for v in L:
            M.insert(v)
        M.display()
        self.assertEqual(len(M),100)

if __name__ == '__main__':
    unittest.main()
