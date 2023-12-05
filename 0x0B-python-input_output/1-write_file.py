#!/usr/bin/python3
""" Contains a function that writes string to a text file """


def write_file(filename="", text=""):
    """ Function that writes a string to a text file
    Args:
        filename: the name of the file to write to
        text: the text to write to the file
    Returns:
        number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
