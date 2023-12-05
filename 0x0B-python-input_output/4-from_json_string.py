#!/usr/bin/python3
""" Contains function that returns an object represented by a json string """
import json


def from_json_string(my_str):
    """ Function that returns an object represented by a json string
    Args:
        my_str: the string to be returned as an object
    Returns:
        an object(python data structure)
    """
    return json.loads(my_str)
