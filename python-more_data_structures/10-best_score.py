#!/usr/bin/python3

def best_score(a_dictionary):
    ndict = a_dictionary.copy()
    dicts = a_dictionary.values()
    for i in dicts:
        for j in range(dicts[i+1], dicts):
            if i > j:
                ndict.pop(j)
            else:
                ndict.pop(i)
    return ndict