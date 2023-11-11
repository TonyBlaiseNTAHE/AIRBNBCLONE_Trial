#!/usr/bin/python3
"""
importing modules 
"""

from models.base_model import BaseModel

class User(BaseModel):
    """this class inherit from
       BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
