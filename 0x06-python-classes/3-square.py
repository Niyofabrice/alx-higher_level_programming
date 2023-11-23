#!/usr/bin/python3
'''defines a class Square'''


class Square:
    '''Represents a square
    Attributes:
        __size (int): size of side ofsquare
    '''
    def __init__(self, size=0):
        '''initializes the square
        Args:
            size (int): size of side of square
        Returns:
            None
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        '''
        Calculate area of the square
        Returns: The square of the size
        '''

        return (self.__size ** 2)
