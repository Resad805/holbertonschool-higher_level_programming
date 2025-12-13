#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    current_best_key = None
    current_best_score = -1 
    for key, value in a_dictionary.items():
        if value > current_best_score:
            current_best_score = value
            current_best_key = key
    return current_best_key
