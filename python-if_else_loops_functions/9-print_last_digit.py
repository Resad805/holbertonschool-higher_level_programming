#!/usr/bin/python3
def print_last_digit(number):
    if i>0:
        lastdigit = number % 10
    elif i<0:
        lastdigit = (number * -1) %10
    if i == 0:
        lastdigit = 0
    return lastdigit

