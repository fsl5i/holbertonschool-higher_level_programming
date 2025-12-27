#!/usr/bin/python3
"""Module that contains a function to convert JSON string to Python object."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string representation of an object.

    Returns:
        object: Python data structure (list, dict, etc.).
    """
    return json.loads(my_str)
