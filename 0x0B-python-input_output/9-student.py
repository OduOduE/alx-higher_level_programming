#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """ defines a student."""

    def _init__(self, first_name, last_name, age):
        """Instantiation with;

        Args:
            first_name (str): First name of student,
            last_name (str): Lastname of student and
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
