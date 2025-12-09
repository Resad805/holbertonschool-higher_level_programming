#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]

def search_replace(my_list, search, replace):
    new_list= []
    new_list.copy(my_list)
    for i in new_list:
        if i == search:
            new_list[i] = replace
    return new_list