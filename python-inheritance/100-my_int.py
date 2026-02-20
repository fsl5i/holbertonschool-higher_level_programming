#!/usr/bin/python3
"""
Module that defines MyInt class inheriting from int
with inverted == and !=
"""


class MyInt(int):
    """MyInt: rebel integer with inverted equality"""

    def __eq__(self, other):
        """Invert == operator"""
        return int(self) != other

    def __ne__(self, other):
        """Invert != operator"""
        return int(self) == other
