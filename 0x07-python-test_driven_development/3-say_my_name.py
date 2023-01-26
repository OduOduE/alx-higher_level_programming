#!/usr/bin/python3
""" Define a function that prints name """


def say_my_name(first_name, last_name=""):
    """ Represent a function that prints name.

    Args:
        first_name (str): Firstname.
        last_name (str): Lastname.
    Returns:
        No return.
    Raises:
        TypeError if first_name or last_name is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
