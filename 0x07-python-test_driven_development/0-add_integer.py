#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Returns the addition of two integers
    Raise: TypeError when either a or be are not integers
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integesr")
    return (int(a)) + (int(b))
