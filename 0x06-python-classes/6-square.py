#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")

        [print("", end="") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[1])]
            [print("#", end="") for k in range(self.__size)]
            print("")

    @property
    def position(self):
        """Get the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if type(value) is tuple and len(value) is 2 and
        (value[0] and value[1]) >= 0 and
        (type(value[0]) and type(value[1])) is int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positie integers")
