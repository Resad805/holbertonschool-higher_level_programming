#!/usr/bin/python3
my_list = [1, 2, 3, 1, 4, 2, 5]


def uniq_add(my_list=[]):
    result = 0

    for i in my_list:
        if i not in my_list:
            result += i
    return print("Result: {:d}".format(result))
