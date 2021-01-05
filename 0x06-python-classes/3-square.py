#!/usr/bin/python3
"""This class define the area"""


class Square:
    """Class of square"""
    __size = 0

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area of the square"""
        return self.__size ** 2
