#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Def test"""
    def test_max_integer(self):
        """Tests"""
        self.assertEqual(max_integer([20, 15, 2]), 20)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer('Hola'), 'o')
        self.assertEqual(max_integer([-1, -15, -20]), -1)
        self.assertEqual(max_integer([0.1, 2.5, 34.5]), 34.5)

if __name__ == '__main__':
        unittest.main()