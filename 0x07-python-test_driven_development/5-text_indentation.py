#!/usr/bin/python3
"""Change Caracters"""


def text_indentation(text):
    """Replace '.' '?' ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c in '.?:':
            print('\n')
        else:
            print(c, end="")
