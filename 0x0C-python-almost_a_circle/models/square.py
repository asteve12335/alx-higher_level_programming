#!/usr/bin/python3
'''
Module contains the class Square
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    The class Square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''
        Size getter method
        '''
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        Args:
            *args : A list of arguments
        '''
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for arg, value in kwargs.items():
                setattr(self, arg, value)

    def to_dictionary(self):
        '''
        Returns a dictionary representation of the Rectangle instance
        '''
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
