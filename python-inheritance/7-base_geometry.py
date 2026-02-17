#!/usr/bin/python3
"""Module BaseGeometry with area and integer_validator"""


class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Public instance method that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as integer > 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
