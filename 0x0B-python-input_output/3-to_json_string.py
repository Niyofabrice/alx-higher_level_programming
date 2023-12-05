#!/usr/bin/python3
""" Contains function that returns JSON representation of an object """
import json


def to_json_string(my_obj):
    """ Function that returns json representation of an odject
    Args:
        my_obj: the object to represent in json
    Returns:
        json representation of the object
    """
    return json.dumps(my_obj)
