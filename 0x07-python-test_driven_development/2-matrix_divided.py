#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Represents a matrix dividing function:

    Args:
        matrix (list of ints of floats): matrix to be divided.
        div (int or float): divisor.
    Raises:
        TypeError: if matrix contains non-number,
                    if matrix contains rows of different sizes,
                    if div is 0.
    Return:
        New matrix or error message.
    """

    errmsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(errmsg)

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    errmsg1 = "Each row must have the same size"
    for elem in matrix:
        if not elem or not isinstance(elem, list):
            raise TypeError(errmsg)

        if not all(len(elem) == len(matrix[0]) for elem in matrix):
            raise TypeError(errmsg1)

        for num in elem:
            if not type(num) in (int, float):
                raise TypeError(errmsg)

    m = [list(map(lambda x: round(x / div, 2), elem)) for elem matrix]
    return (m)
