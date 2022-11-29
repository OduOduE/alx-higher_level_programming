#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    p = number % 10
    if p > 5:
        print(f"Last digit of {number} is {p} and is greater than 5")
    elif p == 0:
        print(f"Last digit of {number} is {p} and is 0")
    else:
        print(f"Last digit of {number} is {p} and is less than 6 and not 0")
else:
    n = 10 - (number % 10)
    if n > 5 and n < 10:
        print(f"Last digit of {number} is {n} and is greater than 5")
    elif n == 10:
        print(f"Last digit of {number} is 0 and is 0")
    else:
        print(f"Last digit of {number} is {n} and is less than 6 and not 0")
