#!/usr/bin/python3
"""Module that contains a function to convert an object to JSON string."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: Any serializable Python object (list, dict, etc.).

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
