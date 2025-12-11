#!/usr/bin/python3
def update_dictionary(a_dictionary, key:str, value):
    sorted_keys = sorted(a_dictionary.keys())
    sorted_dict = sorted(a_dictionary)
    for i in sorted_dict:
        if sorted_keys == key:
            a_dictionary.update({i:value})
        else:
            a_dictionary[key] = value
        print(f"{key}: {value}")
