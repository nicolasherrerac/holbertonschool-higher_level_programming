#!/usr/bin/python3
"""Function"""


def lookup(obj):
    """function that returns the list of available attributes and methods"""
    return list(dir(obj))
