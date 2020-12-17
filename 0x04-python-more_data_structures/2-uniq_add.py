#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = set(my_list)
    suma = 0
    for i in lis:
        suma = suma + i
    return(suma)
