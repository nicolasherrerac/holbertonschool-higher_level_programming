#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """This function adds two integers"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
