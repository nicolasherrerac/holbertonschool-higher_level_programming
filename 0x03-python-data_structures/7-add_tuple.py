#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]

    if len(tuple_a) > 2:
        tuple_a = 2

    if len(tuple_b) > 2:
        tuple_b = 2

    for i in range(len(tuple_a)):
        a[i] += tuple_a[i]

    for c in range(len(tuple_b)):
        b[c] += tuple_b[c]

    return(a[0] + b[0], a[1] + b[1])
