#!/usr/bin/python3
""" Base Model creation """

from datetime import datetime
import uuid


class BaseModel:
    """ Base model class """

    def __init__(self):
        """ Initialization instance attributes
            id: unique id
            created_at: current date and time
            updated_at: current date and time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Returning string representation of instance """
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Saving updated instance """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returning instance dictionnary """
        return self.__dict__
