import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_push(self):
        self.s.Push(10)
        self.assertEqual(self.s.s[-1], 10)

    def test_pop(self):
        self.s.Push(5)
        val = self.s.Pop()
        self.assertEqual(val, 5)
