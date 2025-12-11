#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()
    for i in new_dict:
        if key == i:
            a_dictionary.pop(key)
        else:
            break
    return a_dictionary
