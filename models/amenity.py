#!/usr/bin/python3
"""Define the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity.

   Attributes:
        name (str): The name of Amenity.
    """

    name = ""
