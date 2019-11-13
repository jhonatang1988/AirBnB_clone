#!/usr/bin/python3
'''
tests for user model
'''

from models.user import User
from datetime import datetime
import unittest
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    ''' TestUser Class - to test cases'''
    my_model = User()
    my_model.name = "jhonatan"

    def test_isinstance(self):
        '''test for is instance'''
        self.assertTrue(isinstance(self.my_model, User))
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(isinstance(
            self.my_model.created_at, datetime))
        self.assertTrue(isinstance(
            self.my_model.updated_at, datetime))

    def test_attr_types(self):
        self.assertTrue(type(self.my_model.email), str)
        self.assertTrue(type(self.my_model.password), str)
        self.assertTrue(type(self.my_model.first_name), str)
        self.assertTrue(type(self.my_model.last_name), str)
        self.assertTrue(type(self.my_model.id), str)
        self.assertTrue(type(self.my_model.updated_at), datetime)
        self.assertTrue(type(self.my_model.created_at), datetime)
        self.assertTrue(type(self.my_model.__class__), str)

    def test_has_attr(self):
        self.assertTrue(hasattr(self.my_model, 'email'))
        self.assertTrue(hasattr(self.my_model, 'password'))
        self.assertTrue(hasattr(self.my_model, 'first_name'))
        self.assertTrue(hasattr(self.my_model, 'last_name'))
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, '__class__'))

if __name__ == '__main__':
    unittest.main()
