#!/usr/bin/python3
"""The Framework script for Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """The class defination for place.

    Attributes:
        city_id (str): The City id of the place.
        user_id (str): The User id of the class place.
        name (str): The name of the place of the class place.
        description (str): The description of the place of the class place.
        number_rooms (int): The number of rooms of the class place.
        number_bathrooms (int): The number of bathrooms of the place class.
        max_guest (int): The coun of the guest.
        price_by_night (int): The value of the place per night.
        latitude (float): The geographiacal cordinate horz.
        longitude (float): The geo lat of the place.
        amenity_ids (list): A list containing amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
