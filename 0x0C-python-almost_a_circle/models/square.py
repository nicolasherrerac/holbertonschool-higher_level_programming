#!/usr/bin/python3
"""Function"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    """setter"""
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the rectangle"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args is not None and args is not ():
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    setattr(self, "x", arg)
                if i == 3:
                    setattr(self, "y", arg)
        if kwargs is not None and kwargs is not ():
            for (key, value) in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary of a Square"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
