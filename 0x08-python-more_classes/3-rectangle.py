#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """Represesents the created rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation of the rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an intiger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of the triangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Return the printable representation of the rectangle.

        Represents the rectangle with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
