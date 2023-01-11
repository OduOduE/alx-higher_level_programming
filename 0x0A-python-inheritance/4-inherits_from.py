#!/usr/bin/python3
""" checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Return true or false if object is instance of inherited class"""
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
