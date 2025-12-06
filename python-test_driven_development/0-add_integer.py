#!/usr/bin/python3
"""
This module defines the function add_integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    a and b must be integers or floats, otherwise TypeError
    Floats must be casted to int unless they are NaN
    """

    # Validate types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle NaN: cannot convert float NaN to int
    if isinstance(a, float) and (a != a):  # NaN check
        raise ValueError("cannot convert float NaN to integer")

    if isinstance(b, float) and (b != b):  # NaN check
        raise ValueError("cannot convert float NaN to integer")

    # Handle overflow when converting to int
    try:
        a = int(a)
    except OverflowError:
        raise OverflowError("a is too large")

    try:
        b = int(b)
    except OverflowError:
        raise OverflowError("b is too large")

    return a + b
