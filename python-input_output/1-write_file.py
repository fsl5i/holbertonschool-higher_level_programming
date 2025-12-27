#!/usr/bin/python3
"""Module that contains a function to write text to a file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8).

    The function returns the number of characters written.

    Args:
        filename (str): Name of the file.
        text (str): Text to write into the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
