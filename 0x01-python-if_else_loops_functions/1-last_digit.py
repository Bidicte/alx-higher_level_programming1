#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
the_last_digit = number % 10
if(the_last_digit > 5):
        print(f"Last digit of {number:d} is"
        "{the_last_digit:d} and is greater than 5")
elif(the_last_digit < 6 and the_last_digit != 0):
        print(f"Last digit of {number:d} is -{the_last_digit}"
        "and is less than 6 and not 0")
else:
        print(f"Last digit of {number:d} is {the_last_digit} and is 0")
