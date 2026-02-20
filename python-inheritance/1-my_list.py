#!/usr/bin/python3
"""Module that defines MyList class inheriting from list"""

class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Print the list sorted ascendingly"""
        print(sorted(self))
