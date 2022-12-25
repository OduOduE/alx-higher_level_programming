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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size**2

    def my_print(self):
        """print the square with the character # in stdout"""
        for i in range(self.__size):
            for j in range(self.__size):
                if size == 0:
                    print()
                print("#", end="")
            print()
