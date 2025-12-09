#!/usr/bin/python3
my_list = [1, 2, 3, 1, 4, 2, 5]


def uniq_add(my_list=[]):
    for i in range(len(my_list)):
        for j in range(i , len(my_list)):
            if i == j:
                my_list.remove(j)
    return my_list