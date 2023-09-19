#!/usr/bin/python3
"""Test Amenity Module"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity Class"""

    def __init__(self, *args, **kwargs):
        """Init Method"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test_name2 Method"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import amenity

        self.assertIsNotNone(amenity.__doc__)
        self.assertGreater(len(amenity.__doc__), 5)

        self.assertIsNotNone(Amenity.__doc__)
        self.assertGreater(len(Amenity.__doc__), 5)
