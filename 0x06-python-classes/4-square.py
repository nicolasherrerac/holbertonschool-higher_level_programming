#!/usr/bin/python3
"""This class update private attribute"""


class Square:
    """Class of square"""
    __size = 0

    def __init__(self, size=0):
        """Size"""
        self.__size = size

    def area(self):
        """Global Area"""
        return self.__size ** 2

    @property
    def size(self):
        """Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Errors"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
