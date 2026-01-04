#!/usr/bin/env python3
"""sa"""

import pickle


class CustomObject:
    """Custom object that supports pickle serialization."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        :param filename: File to save the serialized object
        :return: None if an error occurs
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a pickle file.

        :param filename: File containing the serialized object
        :return: CustomObject instance or None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None
        return None
