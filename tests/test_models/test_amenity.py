#!/usr/bin/python3
'''
tests for amenity model
'''

from models.amenity import Amenity
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    ''' TestUser Class - to test cases'''
    my_model = Amenity()
    my_model.name = "LaParrillo"

    def test_isinstance(self):
        '''test for is instance'''
        self.assertIsInstance(self.my_model, Amenity)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(
            self.my_model.created_at, datetime)
        self.assertIsInstance(
            self.my_model.updated_at, datetime)

    def test_attr_types(self):
        '''test for types'''
        self.assertEqual(type(self.my_model.name), str)
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(type(self.my_model.created_at), datetime)

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
        self.assertIsNotNone(Amenity.__doc__)

if __name__ == '__main__':
    '''for import'''
    unittest.main()
