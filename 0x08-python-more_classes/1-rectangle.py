#!/usr/bin/python3
"""Defining a class rectangle"""


class Rectangle:
    """Represents a class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle:

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the private width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
