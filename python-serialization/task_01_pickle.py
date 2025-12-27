#!/usr/bin/python3
"""
Module for pickling and unpickling custom Python objects.
"""

import pickle


class CustomObject:
    """
    Custom Python class to demonstrate serialization with pickle.
    
    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Whether the object represents a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject instance.

        Args:
            name (str): Name of the object.
            age (int): Age of the object.
            is_student (bool): Is student flag.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file using pickle.

        Args:
            filename (str): The output filename.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a pickle file.

        Args:
            filename (str): The input filename.

        Returns:
            CustomObject or None: The deserialized instance, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError):
            return None
