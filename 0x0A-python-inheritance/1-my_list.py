#!/usr/bin/python3
"""Function"""


class MyList(list):
    """Class Mylist"""
    def print_sorted(self):
        new_list = []
        for i in sorted(self):
            new_list.append(i)
        print(new_list)
