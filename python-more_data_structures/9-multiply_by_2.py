#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    key = a_dictionary.keys()
    multiply = a_dictionary[key] * 2 
    return print(f"{key: multiply}")
