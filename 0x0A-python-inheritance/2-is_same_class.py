#!/usr/bin/python3
""" Contains function that checks if a class is a subclass or not """


def is_same_class(obj, a_class):
    """ Function that checks if an object is an instance of a class
    Args:
        obj: object you want to check for
        a_class: class which is the base class
    Returns:
        True: if obj is an instance of a_class
        False: if obj is not an instance of a_class
    """
    return type(obj) == a_class
