#!/usr/bin/python3

def best_score(a_dictionary):
    ndict = a_dictionary.copy()
    dicts = a_dictionary.values()
    
    print(f"Best score: {dicts[-1]}")