#!/usr/bin/python3
"""
This module defines the function add_integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    a and b must be integers or floats, otherwise TypeError
    Floats must be casted to int
    """
    # Validate types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle float overflow while casting
    try:
        a = int(a)
    except OverflowError:
        raise OverflowError("a is too large")

    try:
        b = int(b)
    except OverflowError:
        raise OverflowError("b is too large")

    return a + b
