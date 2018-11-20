from treap import *
import unittest

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

    def testget(self):
        T = Treap()
        for i in range(100):
            T.insert(i)
        self.assertTrue(T.get(30))


    def testdelete(self):
        pass

if __name__ == '__main__':
    unittest.main()
