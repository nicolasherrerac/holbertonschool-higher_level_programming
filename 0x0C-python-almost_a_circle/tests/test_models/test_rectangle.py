#!/usr/bin/python3
"""module for use in testing
    rectangle class
"""
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class for test case for rectangle class
    """

    def test_basic_id(self):
        """tests basic functionality
        """
        b = Rectangle(10, 2)
        b2 = Rectangle(2, 10)
        b3 = Rectangle(3, 10)
        self.assertEqual(b2.id + 1, b3.id)

    def test_given_id(self):
        b = Rectangle(10, 2)
        b2 = Rectangle(10, 3)
        b3 = Rectangle(10, 4)
        b4 = Rectangle(10, 5, 0, 0, 42)
        self.assertEqual(b2.id + 1, b3.id)
        self.assertEqual(42, b4.id)

    def test_input_types(self):
        with self.assertRaises(TypeError):
            n = Rectangle("hello", "world")
        with self.assertRaises(TypeError):
            n = Rectangle(5.4, 3.8)
        with self.assertRaises(TypeError):
            n = Rectangle(4, 8, "hello", "world")
        with self.assertRaises(TypeError):
            n = Rectangle(4, 8, 5.12, 5.9)
        with self.assertRaises(TypeError):
            n = Rectangle(True, False, True, False)

    def test_area(self):
        r = Rectangle(4, 8)
        self.assertEqual(r.area(), 32)

    def test_dictionary(self):
        """tests rectangle's to_dictionary method
        """
        r = Rectangle(4, 5, 6, 7, 33)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict['id'], 33)
        self.assertEqual(r_dict['width'], 4)
        self.assertEqual(r_dict['height'], 5)
        self.assertEqual(r_dict['x'], 6)
        self.assertEqual(r_dict['y'], 7)
