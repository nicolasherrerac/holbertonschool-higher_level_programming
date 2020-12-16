#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    var1 = len(tuple_a)
    if var1 >= 2:
        var1 = 2
    var2 = len(tuple_b)
    if var2 >= 2:
        var2 = 2

    for i in range(var1):
        a[i] += tuple_a[i]

    for c in range(var2):
        b[c] += tuple_b[c]

    return(a[0] + b[0], a[1] + b[1])
