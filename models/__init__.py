#!/usr/bin/python3
""" Create a new instance """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()

classes = ["BaseModel"]
