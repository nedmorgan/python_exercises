import unittest
from numbers import fibonacci


class TestFibonacciSequence(unittest.TestCase):
    def test_list(self):
        self.assertEqual(fibonacci(0), None,
                         "Need to input numbers greater than 0")
        self.assertEqual(fibonacci(1), [0],
                         "Only has a list of 1")
        self.assertEqual(fibonacci(2), [0, 1],
                         "Only has a list of 1, 2")
        self.assertEqual(fibonacci(4), [0, 1, 1, 2],
                         "The list has 4 items")
        self.assertEqual(fibonacci(13), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],
                         "The list has 13 items")
