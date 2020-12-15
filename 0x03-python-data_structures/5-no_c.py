#!/usr/bin/python3
def no_c(my_string):
    w = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            w += i
    return w
