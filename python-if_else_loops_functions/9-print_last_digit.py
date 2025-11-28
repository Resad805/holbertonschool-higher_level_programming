#!/usr/bin/python3
def print_last_digit(number):
    if number>0:
        lastdigit = number % 10
    elif number<0:
        lastdigit = (number * -1) %10
    else:
        lastdigit = 0
    return print(lastdigit,end = "")

