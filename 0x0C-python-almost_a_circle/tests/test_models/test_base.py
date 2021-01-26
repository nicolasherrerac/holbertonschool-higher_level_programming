#!/usr/bin/python3
"""module for use in testing
    base class
"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests"""

    def test_basic(self):
        """tests basic functionality
        """
        b = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id + 1, b3.id)

    def test_given_id(self):
        """tests id being set when given and not upticking default
        """
        b = Base()
        b2 = Base(24)
        b3 = Base(45)
        b4 = Base()
        self.assertEqual(45, b3.id)
        self.assertEqual(b.id + 1, b4.id)

    def test_json_method(self):
        """tests Base's to_json_string method
        """
        r1 = Rectangle(4, 5, 6, 7, 8)
        r2 = Rectangle(10, 11, 12, 13, 14)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_dict = Base.to_json_string([d1, d2])
        j_d = eval(json_dict)
        self.assertEqual(j_d[0]['id'], 8)
        self.assertEqual(j_d[1]['x'], 12)

    def test_fjs_empty(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """Tests from_json_string th an empty string"""
        self.assertEqual([], Base.from_json_string(None))

    def test_emty_to_json_string(self):
        """a"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_docstring(self):
        """test docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_from_json_empty(self):
        """tests base's from_json_string method with empty inputs
        """
        d_list = Base.from_json_string("")
        self.assertEqual(len(d_list), 0)
        d_list = Base.from_json_string(None)
        self.assertEqual(len(d_list), 0)

    def test_read_from_file(self):
        """tests the base class method read from file, for use in
            -> Rectangle and Square
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].y, 8)
        self.assertEqual(list_rectangles_output[1].height, 4)
