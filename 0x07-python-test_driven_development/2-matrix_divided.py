#!/usr/bin/python3
"""Defines a function that divides all elements in a matrix"""

def matrix_divided(matrix, div):
    """divides each element with div and return a new matrix
    raise: TypeError if matrix is not a list of lists of integers or floats
    raise: TypeError if each row in matrix are not the same size
    raise: TypeError if div is not an integer or float
    raise: ZeroDivisionErro if div is 0
    """
    
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for l in matrix:
        if type(l) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
