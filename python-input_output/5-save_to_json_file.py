#!/usr/bin/python3
"""Module that contains a function to save an object to a file using JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj: Python object (list, dict, etc.) to save.
        filename (str): Name of the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
