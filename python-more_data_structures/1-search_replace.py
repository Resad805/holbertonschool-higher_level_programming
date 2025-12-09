#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]

def search_replace(my_list, search, replace):
    new_list= []
    new_list = my_list.copy()
    for i,value in new_list:
        if value == search:
            new_list[i] = replace
    return new_list