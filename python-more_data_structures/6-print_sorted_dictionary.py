#!/usr/bin/python3
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }


def print_sorted_dictionary(a_dictionary):
    keys_list = sorted(a_dictionary.keys())

    for keys in keys_list:
        value = a_dictionary[keys]
        print(f"{keys}: {value}")

