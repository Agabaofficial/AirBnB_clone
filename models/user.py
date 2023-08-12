#!/usr/bin/python3
"""Define the user class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.

    Attributes:
        Email (str): The user email.
        Password (str): The user password.
        first_name (str): The user first name.
        last_name (str): The user last name.
    """

    Email = ""
    Password = ""
    first_name = ""
    last_name = ""
