#!/usr/bin/python3
"""Function"""
import json


class Base():
    """Create class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__ + ".json"
        new = []
        if list_objs is not None:
            for i in list_objs:
                new.append(cls.to_dictionary(i))
        with open(file, "w") as myFile:
            myFile.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(5, 10)
        if cls.__name__ is "Square":
            dummy = cls(6)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        new = []
        try:
            with open(file, 'r') as myFile:
                new = cls.from_json_string(myFile.read())
            for i, j in enumerate(new):
                new[i] = cls.create(**new[i])
        except:
            pass
        return new
