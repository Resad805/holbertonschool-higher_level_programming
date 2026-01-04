#!/usr/bin/python3
"""sa"""


def class_to_json(obj):
    """Returns a dictionary description with simple data structures."""
    return obj.__dict__.copy()
