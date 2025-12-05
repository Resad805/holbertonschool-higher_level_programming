#!/usr/bin/python3
def no_c(mystr):
    newstr = ""
    for char in mystr:
        if char != 'C' and char != 'c':
            newstr += char
    return newstr
