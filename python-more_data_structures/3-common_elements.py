#!/usr/bin/python3

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }


def common_elements(set_1, set_2):
    z = set_1.copy()
    new = []
    for i in z:
        if i not in set_2:
            new.append(i)
    for i in new:
        z.remove(i)
    return print(list(z))
