#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary:
        if key == i:
            a_dictionary.pop(key)
        else:
            break
    return a_dictionary
