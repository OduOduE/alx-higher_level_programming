#!/usr/bin/python3
"""Define function that appends string at end of text file"""


def append_write(filename="", text=""):
    """Write a function that appends a string:

    Args:
        filename (str): The name of file to be written.
        text (str): The text to write.
    Return:
        the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
