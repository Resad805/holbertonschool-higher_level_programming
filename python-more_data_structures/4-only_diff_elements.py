#!/usr/bin/python3
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
def only_diff_elements(set_1, set_2):
    final = []
    for i in set_1:
        if i not in set_2:
            final.append(i)
    for i in set_2:
        if i not in set_1:
            final.append(i)

    return final
