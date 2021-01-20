#!/usr/bin/python3
"""Create function"""


def read_file(filename=""):
    """Read file txt"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
