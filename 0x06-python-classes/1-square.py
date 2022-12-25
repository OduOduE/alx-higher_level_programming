#!/usr/bin/python3
"""defines a square by:
        Private instance attribute: size
        Instantiation with size (no type/value verification)
    """


class Square:
    """Represent a square"""

    def __init__(self, size):
        """Initilize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
