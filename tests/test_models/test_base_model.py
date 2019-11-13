#!/usr/bin/python3
'''Unittest module for Base Model Class'''

import uuid
from datetime import datetime, date, time
import models
from models.base_model import BaseModel
import json
import os.path
import re


class TestBaseModel(unittest.TestCase):
    '''Unittest module for Base Model Class'''
    def setUp(self):
        """ create instances of Base and setup tests"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model2 = BaseModel()

    def teardown(self):
            """End tests and del instances"""
        del my_model
        del my_model2
        os.remove("file.json")

    def test_instantiation(self):
        '''Unittest module for Base Model Class'''
        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(my_model, Basemodel)
        self.assertTrue(issubclass(type(b), BaseModel))

     def test_unique_id(self):
         '''Check unique Id por instances'''
        self.assertNotEqual(self.my_model.id, self.my_model2.id)

    def test_str_check(self):
        '''Test if the output is ok'''
        str1 = "[BaseModel] ({}) {}".format(self.my_model.id,
                                            self.my_model.__dict__)
        self.assertEqual(str1, str(self.my_model))

    def test_save(self):
        '''Test if is saving the changes'''
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)
    def test_to_dict(self):
        '''Test to dictionary'''
        d_format = %Y-%m-%dT%H:%M:%S.%f
        model
