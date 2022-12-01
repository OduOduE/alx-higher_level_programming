#!/usr/bin/python3
def uppercase(str):
    tr = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            tr += chr(ord(i) - 32)
        else:
            tr += i
    print("{:s}".format(tr))
