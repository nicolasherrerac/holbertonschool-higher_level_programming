#!/usr/bin/python3
"""Divide Elements Of Matrix"""


def matrix_divided(matrix, div):
    """Divide Elements"""
    new = []
    if matrix:
        for r in range(len(matrix)):
            lista = []
            for c in matrix[r]:
                if type(c) not in (int, float):
                    raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
                if len(matrix[r]) != len(matrix[0]):
                    raise TypeError("Each row of the matrix \
must have the same size")
                if type(div) not in (int, float):
                    raise TypeError("div must be a number")
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                lista.append(round(c / div, 2))
            new.append(lista)
        return new
