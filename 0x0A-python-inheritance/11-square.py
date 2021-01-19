#!/usr/bin/python3
"""Function"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Create class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()

    def __str__(self):
        """str"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)