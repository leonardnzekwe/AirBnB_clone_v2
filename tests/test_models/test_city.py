#!/usr/bin/python3
"""Test City Module"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test City Class"""

    def __init__(self, *args, **kwargs):
        """Init method"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test_state_id method"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test_name method"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import city

        self.assertIsNotNone(city.__doc__)
        self.assertGreater(len(city.__doc__), 5)

        self.assertIsNotNone(City.__doc__)
        self.assertGreater(len(City.__doc__), 5)
