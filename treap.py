class Node:
    def __init__(self, value, left, right):
        self._value = value
        self._num = rand()
        self._left = left
        self._right = right


class Treap:
    def __init__(self):
        self._root = None
