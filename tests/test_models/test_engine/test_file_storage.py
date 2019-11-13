#!/usr/bin/python3
'''Unittest module for Storage File'''

from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
import json
import os
import unittest


class TestFileStorage(unittest.TestCase):
    '''Unittest module for Base Model Class'''
    def setUp(self):
        """ create instances of Base and setup tests"""
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89

    def teardown(self):
            """End tests and del instances"""
            del self.my_model
            try:
                os.remove("file.json")
            except:
                pass

    def test_all_FileStorage(self):
        '''Test all method'''
        s = FileStorage()
        all_obj = s.all()
        self.assertIs(all_obj, s._FileStorage__objects)
        self.assertIsNotNone(all_obj)
        self.assertEqual(type(all_obj), dict)
        obj = self.my_model.__class__.__name__ + "." + self.my_model.id
        str1 = "[BaseModel] ({}) {}".format(self.my_model.id,
                                            self.my_model.__dict__)

    def test_new_FileStorage(self):
        '''Test if the output is ok'''
        s = FileStorage()
        all_obj = s.all()
        my_model2 = State()
        my_model2.name = "Chía"
        s.new(my_model2)
        self.assertEqual(type(all_obj), dict)
        self.assertIsNotNone(all_obj)
        self.assertIs(all_obj, s._FileStorage__objects)
        obj = my_model2.__class__.__name__ + "." + my_model2.id
        self.assertIsNotNone(all_obj[obj])
        p_obj = all_obj[obj]
        str1 = "[State] ({}) {}".format(my_model2.id,
                                        my_model2.__dict__)
        self.assertEqual(str1, str(p_obj))

    def test_save_FileStorage(self):
        '''Test if is saving the changes'''
        dic1 = self.my_model.to_dict()
        key = dic1['__class__'] + "." + dic1['id']
        s = FileStorage()
        s.save()
        with open("file.json", mode='r') as f:
            str1 = json.load(f)

if __name__ == '__main__':
    unittest.main()
