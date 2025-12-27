#!/usr/bin/python3
"""
Module that defines a function to convert a class instance
to a dictionary for JSON serialization.
"""

def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance
    with only simple data structures (list, dict, str, int, bool).

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary containing all serializable attributes.
    """
    return obj.__dict__.copy()
