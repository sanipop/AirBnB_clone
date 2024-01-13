#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class Amenity that inherits from BaseModel.

    Attributes:
        name (str): the name assigned to the varaiable.
    """

    name = ""
