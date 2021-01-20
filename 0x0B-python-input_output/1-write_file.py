#!/usr/bin/python3
"""Function"""


def write_file(filename="", text=""):
    """Write in a file"""
    with open(filename, mode='w', encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
