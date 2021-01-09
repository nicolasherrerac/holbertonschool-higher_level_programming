#!/usr/bin/python3
"""Print Square"""


def print_square(size):
    """Conditions"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    """Print Square"""
    for r in range(size):
        for c in range(size):
            print("#", end="")
        print()
