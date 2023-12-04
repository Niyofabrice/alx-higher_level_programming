#!/usr/bin/python3
""" Contains the lookup function """

def lookup(obj):
    """ function that returns list of available attributes
    and methods of an object
    Args:
        obj (class): object
    Returns:
        lsit: list of available attributes and methods of an object """

    return dir(obj)
