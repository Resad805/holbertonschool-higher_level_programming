#!/usr/bin/python3

def best_score(a_dictionary):
    ndict = a_dictionary.copy()
    for key, value in a_dictionary.items():
        for x in a_dictionary.value():
            if value > x:
                ndict.pop(x)

    return ndict