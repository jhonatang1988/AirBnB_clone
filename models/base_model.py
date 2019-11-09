#!/usr/bin/python3
'''Base Class'''

import uuid
from datetime import datetime, date, time
import models


class BaseModel():
    ''' BaseModel - attributes and methods'''
    __nb_objects = 0

    def __init__(self, *args, **kwargs):
        '''__init__ - attributes'''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'id':
                    self.id = value
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'my_number':
                    self.my_number = value
                if key == 'name':
                    self.name = value
        else:
            BaseModel.__nb_objects += 1
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''__str__ - print instance'''
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        '''save - save changes of instance'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''to_dict - dictionary of the instance'''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return(new_dict)
