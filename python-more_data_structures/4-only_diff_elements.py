#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    z = set_1.copy()
    new = []
    for i in z:
        if i in set_2:
            new.append(i)
    for i in new:
        z.remove(i)
    return print(sorted(list(z)))
