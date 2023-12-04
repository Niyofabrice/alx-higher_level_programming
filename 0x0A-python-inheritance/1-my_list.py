#!/usr/bin/python3
""" Contains class Mylist that inherits from list """


class Mylist(list):
    """" subclass of list """
    def __init__(self):
        """ initializing the object """
        super().__init__()

    def print_sorted(self):
        """ function that sorts list """
        print(sorted(self))
