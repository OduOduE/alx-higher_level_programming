#!/usr/bin/python3
"""Defining a text file-reading function"""


def read_file(filename=""):
    """Print the text in the file to the stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
