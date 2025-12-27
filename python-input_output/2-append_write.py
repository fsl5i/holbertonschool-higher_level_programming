#!/usr/bin/python3
"""Module that contains a function to append text to a file."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8).

    The function returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
