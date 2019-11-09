#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os.path

class FileStorage(BaseModel):
    '''FileStorage - file storage'''
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}
    def all(self):
        return (self.__objects)

    def new(self, obj):
        id1 = getattr(obj, 'id')
        self.__objects['BaseModel.' + id1] = obj

    def save(self):
        dict2 = {}
        for key, value in self.__objects.items():
            dict2[key] = value.to_dict()
            with open(self.__file_path, mode='w', encoding="utf-8") as f:
                f.write(json.dumps(dict2))

    def reload(self):
        import os.path
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding="utf-8", mode='r') as f:
                json_string = f.read()
                dict1 = json.loads(json_string)
                for key, value in dict1.items():
                    self.__objects[key] = BaseModel(**value)
