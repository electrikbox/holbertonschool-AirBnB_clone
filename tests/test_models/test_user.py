#!/usr/bin/python3
""" Unittest for BaseModel """

import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
import os


class testUser(unittest.TestCase):
    """ Test class for User """

    def setUp(self):
        """ Set up for test """
        self.model = User()

    # def test_init(self):
    #     """ Test init """
    #     self.assertIsInstance(self.model, User)
    #     self.assertIsInstance(self.model.id, str)
    #     self.assertIsInstance(self.model.created_at, datetime)
    #     self.assertIsInstance(self.model.updated_at, datetime)

    # def test_save(self):
    #     """ Test save """
    #     first_updated_at = self.model.updated_at
    #     self.model.save()
    #     self.assertNotEqual(first_updated_at, self.model.updated_at)
    #     os.remove("file.json")

    # def test_to_dict(self):
    #     """ Test to dict"""
    #     model_dict = self.model.to_dict()
    #     self.assertIsInstance(model_dict, dict)
    #     self.assertIn('id', model_dict)
    #     self.assertIn('created_at', model_dict)
    #     self.assertIn('updated_at', model_dict)
    #     self.assertIn('__class__', model_dict)

    # def test_str(self):
    #     """ Test string rep """
    #     model_str = str(self.model)
    #     self.assertIsInstance(model_str, str)
    #     self.assertIn('[User]', model_str)
    #     self.assertIn('id', model_str)
    #     self.assertIn(str(self.model.id), model_str)
    #     self.assertIn(str(self.model.__dict__), model_str)

    def test_class(self):
        """ Validate the types of the attributes an class. """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)
