#!/usr/bin/python
"""
This is module 2-matrix_divided
function that divides all elements of a matrix.
matrix must be a list of lists of integers or floats.
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    new_matrix = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError(message)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(message)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in i:
            if type(n) is not int and type(n) is not float:
                raise TypeError(message)
        new_matrix += [(list(map(lambda x: round((x / div), 2), i)))]
    return new_matrix
