#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if val
