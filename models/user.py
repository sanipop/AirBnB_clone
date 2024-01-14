#!/usr/bin/python3
"""A remplate fotr the class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class that inherits from the BaseModel.

    Attributes:
        email (str): the email fiven to auser.
        password (str): The value of password for a user account.
        first_name (str): The first name the user sign in with.
        last_name (str): the last namea ythe user signs in with.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
