#!/usr/bin/python3
'''
tests for state model
'''

from models.state import State
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    ''' TestUser Class - to test cases'''
    my_model = State()
    my_model.name = "LaCundi"

    def test_isinstance(self):
        '''test for is instance'''
        self.assertIsInstance(self.my_model, State)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(
            self.my_model.created_at, datetime)
        self.assertIsInstance(
            self.my_model.updated_at, datetime)

    def test_attr_types(self):
        '''test for types'''
        self.assertEqual(type(self.my_model.name) is str, True)
        self.assertEqual(type(self.my_model.id) is str, True)
        self.assertEqual(type(self.my_model.updated_at) is datetime, True)
        self.assertEqual(type(self.my_model.created_at) is datetime, True)
        self.assertEqual(type(self.my_model.__class__) is str, False)

    def test_has_attr(self):
        '''test for attributes'''
        self.assertEqual(hasattr(self.my_model, 'email'), False)
        self.assertEqual(hasattr(self.my_model, 'password'), False)
        self.assertEqual(hasattr(self.my_model, 'first_name'), False)
        self.assertEqual(hasattr(self.my_model, 'last_name'), False)
        self.assertEqual(hasattr(self.my_model, 'id'), True)
        self.assertEqual(hasattr(self.my_model, 'updated_at'), True)
        self.assertEqual(hasattr(self.my_model, 'created_at'), True)
        self.assertEqual(hasattr(self.my_model, '__class__'), True)
        self.assertEqual(hasattr(self.my_model, 'name'), True)

    def test_doc(self):
        '''test for doc'''
        self.assertIsNotNone(State.__doc__)

if __name__ == '__main__':
    '''for import'''
    unittest.main()
