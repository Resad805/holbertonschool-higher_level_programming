#!/usr/bin/python3
"""sa"""


def write_file(filename="", text=""):
    """write"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
