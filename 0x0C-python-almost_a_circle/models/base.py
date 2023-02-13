#!/usr/bin/python3
""" A module contain the base class of other classes """


class Base:
    """ The class Base on which all others get their attributes """

    __nb_objects = 0


    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
