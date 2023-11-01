#!/usr/bin/python3
""" Defines FileStorage class """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import json


class FileStorage():
    """ Represents a FileStorage class
    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Show all object from __objects """
        return self.__objects

    def new(self, obj):
        """ Add new object in __objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def reload(self):
        """ Deserialize __objects from the JSON file"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    instance = eval(class_name)(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
