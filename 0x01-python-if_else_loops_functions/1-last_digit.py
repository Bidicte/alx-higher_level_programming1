#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
ld = abs(n) % 10
if (n < 0):
    ld = -ld
    if (ld == 0):
        print(f"Last digit of {n:d} is {ld:d} and is 0")
    else:
        print(f"Last digit of {n:d} is {ld:d}"
        "and is less than 6 and not 0")
else:
    if (ld < 6 and ld != 0):
        print(f"Last digit of {n:d} is {ld:d} and is less than 6 and not 0")
    elif (ld > 5):
        print(f"Last digit of {n:d} is {ld:d} and is greater than 5")
    else:
        print(f"Last digit of {n:d} is {ld} and is 0")
