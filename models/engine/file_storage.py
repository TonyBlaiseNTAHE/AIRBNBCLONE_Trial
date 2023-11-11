#!/usr/bin/python3
"""
file_store module
"""

import json
from models.base_model import BaseModel

"""
class file_store
"""


class FileStorage:
    """declaring private attributes"""
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def classes(self):
        """returns a dict that contains 
        """
        from models.base_model import BaseModel
        from models.user import User
        cls = {
            "BaseModel": BaseModel,
            "User": User
            
        }
        return cls

    def new(self, obj):
        """ sets in __objects the obj
            with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        """
        dt = {}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            for key, value in self.__objects.items():
                dt[key] = value.to_dict()
            json.dump(dt, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                loaded_data = json.load(file)
                for data in loaded_data.values():
                    class_name = data.get("__class__")
                    if class_name in self.classes():
                        cls_obj = self.classes()[class_name]
                        self.new(cls_obj(**data))
        except FileNotFoundError:
            pass
