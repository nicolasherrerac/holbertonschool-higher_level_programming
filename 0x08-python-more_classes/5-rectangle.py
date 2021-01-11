#!/usr/bin/python3
"""This function define the recangle"""


class Rectangle:
    """Class of rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area"""
        return self.height * self.width

    def perimeter(self):
        """perimeter"""
        return (self.height + self.width) * 2

    def __str__(self):
        """Print Rectangule"""
        if self.width == 0 or self.height == 0:
            return ""
        rec = ""
        for i in range(self.height):
            rec += "#" * self.width + "\n"
        return rec[:-1]

    def __repr__(self):
        """Print str"""
        return "Rectangle(" + str(self.__width)\
            + ", " + str(self.__height) + ")"
