#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): public(general) size of squares
        """
        self.size = size

    @property
    def size(self):
        """getter: retreive the private size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter: set the value of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__area**2
