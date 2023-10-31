#!/usr/bin/python3
""" Unit tests for the FileStorage class """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """ Test class for the FileStorage class """

    def test_file_path(self):
        """  Test file path """
        model = BaseModel()
        model.save()
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        os.remove("file.json")

    def test_objects_dict(self):
        """ Test objects dictionary """
        model = BaseModel()
        model.save()
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        os.remove("file.json")

    def test_all(self):
        """ Test all filestorage """
        storage = FileStorage()
        instance = storage.all()
        self.assertIsNotNone(instance)
        self.assertIsInstance(instance, dict)

    def test_new(self):
        """ Test new filestorage """
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        FileStorage.new(FileStorage, model)
        self.assertNotEqual(
            objects[f"{model.__class__.__name__}.{model.id}"], None)

    def test_save(self):
        """ Test save filestorage """
        bm = BaseModel()
        storage = FileStorage()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as file:
            self.assertIn("BaseModel." + bm.id, file.read())

    def test_reload(self):
        """ Test reload filestorage """
        bm = BaseModel()
        storage = FileStorage()
        storage.new(bm)
        storage.save()
        storage.reload()
        FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, FileStorage._FileStorage__objects)
