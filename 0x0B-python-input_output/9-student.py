#!/usr/bin/python3
"""Function"""


class Student():
    """Create class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """same as 10-class_to_json.py"""
        return self.__dict__
