#!/usr/bin/python3
"""Defines a function that writes an Object to a
    text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file:

    Args:
        my_obj (str): Object to be saved.
        filename (str): The file name.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
