#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    key = a_dictionary.keys()
    values = a_dictionary.values()
    for j in key:
        for i in values:
            if i > 0:
                i= i*2
                print(f"{j: i}")
