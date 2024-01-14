#!/usr/bin/python3
"""Script containing the  class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class defination Review that inherits a class Basemodel.

    Attributes:
        place_id (str): the value assigned to the id.
        user_id (str): the value assigned to the user.
        text (str): a string text for review.
    """

    place_id = ""
    user_id = ""
    text = ""
