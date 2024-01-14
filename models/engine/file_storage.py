#!/usr/bin/python3
"""The class that models the file storage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A storage class template.

    Attributes:
        __file_path (str): File name that obj is saved to.
        __objects (dict): An obj dictionay.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """function  that return the the dict."""
        return FileStorage.__objects

    def new(self, obj):
        """mark __objects obj to key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """File to save the file to JSON."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Function that return the json back to obj."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
