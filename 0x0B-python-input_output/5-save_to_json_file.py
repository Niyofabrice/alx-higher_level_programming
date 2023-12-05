#!/usr/bin/python3
""" Contains function that write an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ Function that write an object to a text file using json representation
    Args:
        my_obj: the object to write to the file
        filename: the file to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
