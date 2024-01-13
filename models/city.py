#!/usr/bin/python3
"""The Module of the city Class."""
from models.base_model import BaseModel


class City(BaseModel):
    """The class defination city.

    Attributes:
        state_id (str): The Attribute of state_id.
        name (str): A city parameter name.
    """

    state_id = ""
    name = ""
