#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    od_set = set_1.copy()
    new = []
    for i in od_set:
        if i in set_2:
            new.append(i)
    for i in new:
        od_set.remove(i)
    return print(sorted(list(od_set)))
