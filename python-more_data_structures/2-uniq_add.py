#!/usr/bin/python3
my_list = [1, 2, 3, 1, 4, 2, 5]


def uniq_add(my_list=[]):
    result = 0
    new_list = []
    for i in my_list:
        if i not in new_list:
            result += i
            new_list.append(i)
    return print(f'Result: {result}')
