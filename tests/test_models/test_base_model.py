#!/usr/bin/python3

""" 
import unittest module
"""
import unittest
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    
    def test_init(self):
        obj1 = BaseModel()
        self.assertIsInstance(obj1, BaseModel)
    

if __name__ == '__main__':
    unittest.main()