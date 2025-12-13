#!/usr/bin/python3

def best_score(a_dictionary):
    ndict = a_dictionary.copy()
    for key, value in a_dictionary.items():
        value > a_dictionary[value + 1]
        ndict.pop(a_dictionary[value + 1])

    return ndict