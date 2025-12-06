#!/usr/bin/python3
"""
This module contains the add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.

    a and b must be integers or floats.
    Floats are casted to integers unless they are NaN or infinity.
    """

    # Check for valid types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN (NaN != NaN is True)
    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float NaN to integer")

    # Check for infinity
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")

    # Normal conversion
    a = int(a)
    b = int(b)

    return a + b
