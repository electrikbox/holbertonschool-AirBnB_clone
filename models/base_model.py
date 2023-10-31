#!/usr/bin/python3
""" Base Model creation """

from datetime import datetime
import uuid


class BaseModel:
    """ Base model class """

    def __init__(self):
        """ Initialization instance attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ String representation of instance
        Returns:
            str: string representation of instance
        """
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updated the public instance attribute
            updated_at : with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returning instance dictionnary
        Returns:
            dict: Instance dictionary
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
