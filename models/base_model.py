#!/usr/bin/python3
""" importing uuid module
"""
from uuid import uuid4
from datetime import datetime
import models
""" class called BaseModel
"""


class BaseModel:
    """initializing the class
    """
    def __init__(self, *args, **kwargs):
        """class constructor
        """
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    d = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, d)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ returns the class name, id and the dictionary's contents
        """
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """ save the updated time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
           of __dict__ of the instance
        """
        dt = {}
        dt['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dt[key] = value.isoformat()
            else:
                dt[key] = value
        return dict(dt)