#!/usr/bin/python3
"""Defines the BaseModel class in the script base_model.py."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The baseModel to manage all other class"""

    def __init__(self, *args, **kwargs):
        """The function that initialize the Class Base Model.

        Args:
            *args (any): The argument pasased, with it unused.
            **kwargs (dict): Key-value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """The function to update the updated_at variable."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        The class name is added as key
        convert updated and created at to string.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """The function convert instance class, id and dict ot str."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
