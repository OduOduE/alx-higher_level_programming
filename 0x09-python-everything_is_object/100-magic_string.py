#!/usr/bin/python3
def magic_string():
    """
    setattr(magic_string, "i", getattr(magic_string, "i", -1) + 1)
    return "BestSchool" + ", BestSchool" * getattr(magic_string, "i", 0)
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
