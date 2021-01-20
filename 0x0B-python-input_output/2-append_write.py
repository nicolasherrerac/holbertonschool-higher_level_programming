#!/usr/bin/python3
"""Function"""


def append_write(filename="", text=""):
    """Append text in a file"""
    with open(filename, mode='a', encoding="utf-8") as myfile:
        return myfile.write(text)