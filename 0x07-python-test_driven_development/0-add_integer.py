#!/usr/bin/python3
"""Defines a function that adds two integers"""


def add_integer(a, b=98):
    """function that adds two integers.

    Float arguments are typecasted to ints before addition

    Raise TypeError if a or b is not integer or not float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
