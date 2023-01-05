#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Prevents user fron instantiating new LockedClass
    attribute for anything but attributes called 'first_name'
    """
    __slots__ = "first_name"
