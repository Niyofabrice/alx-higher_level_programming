#!/usr/bin/python3
""" Contains function that reads a text file """


def read_file(filename=""):
    """ Function that reads a text file
    Args:
    filename: the name of the file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data)
