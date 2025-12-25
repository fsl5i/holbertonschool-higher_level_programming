#!/usr/bin/python3
"""
Module that contains a function to read a UTF-8 text file
and print its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
