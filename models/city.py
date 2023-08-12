#!/usr/bin/python3
"""Define the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City.

   Attributes:
        state_id (str): The state id.
        name (str): The name of city.
    """

    state_id = ""
    name = ""
