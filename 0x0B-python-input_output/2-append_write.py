#!/usr/bin/pytohn3
""" Contains function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file
    Args:
        filename: the name of the file to append to
        text: the text to append at the end of the file
    Returns:
        number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
