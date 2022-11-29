#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

msg = "Last digit of"
p = number % 10

if p == 0:
    print(f"Last digit of {number} is {p} and is 0")

else:
    if number >= 0:
        if p > 5:
            print(f"{msg} {number} is {p} and is greater than 5")
        else:
            print(f"{msg} {number} is {p} and is less than 6 and not 0")
    else:
        n = 10 - (number % 10)
        if n > 5:
            print(f"{msg} {number} is {n} and is greater than 5")
        else:
            print(f"{msg} {number} is {n} and is less than 6 and not 0")
