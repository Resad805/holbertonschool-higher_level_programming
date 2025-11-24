#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ls = number%10

if number < 0:
    ls = -1*(10-ls)

last_print = print(f"Last digit of {number} is {ls} and is",end=" ")

if ls > 5:
	print("greater than 5")
elif ls == 0:
        print("0") 
elif ls < 6 and not 0:
        print("less than 6 and not 0")
