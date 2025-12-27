#!/usr/bin/python3
"""Defines a Student class with reload capability."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student.
        If attrs is a list, return only selected attributes.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
