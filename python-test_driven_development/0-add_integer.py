#!/usr/bin/python3
"""
This module contains the add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.

    a and b must be integers or floats.
    Floats are casted to integers before addition.
    Raises TypeError if a or b are not integers or floats.
    Returns the sum as an integer.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
