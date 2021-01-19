#!/usr/bin/python3
"""Function"""


def inherits_from(obj, a_class):
    """Validate"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
