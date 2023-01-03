#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """Establishing a class rectangle"""

    def ___init__(self, width=0, height=0):
        """Instantiation of the class args.

        args:
            width (int): the width of the rectangle.
            height (int): the height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the width accordingly"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height accordingy"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that Returns area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Public instance method that returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
