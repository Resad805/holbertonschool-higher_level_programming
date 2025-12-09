#!/usr/bin/python3


def common_elements(set_1, set_2):
    z = set_1.copy()
    new = []
    for i in z:
        if i not in set_2:
            new.remove(i)
    for i in new:
        z.append(i)
    return print(sorted(list(z)))
