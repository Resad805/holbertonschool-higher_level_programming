#!/usr/bin/env python3
"""sa"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    :param data: Python dictionary to serialize
    :param filename: Name of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    :param filename: Name of the input JSON file
    :return: Python dictionary with deserialized data
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
