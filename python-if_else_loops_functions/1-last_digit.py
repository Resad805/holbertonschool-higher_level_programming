#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ls = number%10
last_print = print(f"Last digit of {number} is {ls} and is")

if ls > 5:
	print(f"{last_print} greater than 5")
elif ls == 0:
        print(f"{last_print} and is 0")
elif ls < 6 and not 0:
        print(f"{last_print} less than 6 and not 0")
