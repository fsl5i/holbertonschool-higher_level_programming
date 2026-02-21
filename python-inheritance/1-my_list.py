#!/usr/bin/python3
"""Module that defines a MyList class."""


class MyList(list):
    """MyList inherits from list and adds print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
