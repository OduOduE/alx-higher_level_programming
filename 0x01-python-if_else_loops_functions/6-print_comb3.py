#!/usr/bin/python3
for dig1 in range(0, 9):
    for dig2 in range(1, 10):
        if dig1 < dig2:
            print(dig1, end="")
            print(dig2, end="\n" if dig1 == 8 and dig2 == 9 else ", ")
