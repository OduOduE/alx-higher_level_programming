#!/usr/bin/python3
""" Defines a function that prints a square with the character # """


def print_square(size):
    """ Represents a square printing function """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for n in range(size):
            print("#", end="")
        print()
