#!/usr/bin/python3
"""Test Place Module"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test Place Class"""

    def __init__(self, *args, **kwargs):
        """Init Method"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test_city method"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test_user method"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test_name method"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test_description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test_number_room method"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test_number_bathrooms method"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test_max_guest method"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test_price_by_night method"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test_latitude method"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test_longitude method"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test_amenity method"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import place

        self.assertIsNotNone(place.__doc__)
        self.assertGreater(len(place.__doc__), 5)

        self.assertIsNotNone(Place.__doc__)
        self.assertGreater(len(Place.__doc__), 5)

        self.assertIsNotNone(Place.amenities.__doc__)
        self.assertGreater(len(Place.amenities.__doc__), 5)

        self.assertIsNotNone(Place.reviews.__doc__)
        self.assertGreater(len(Place.reviews.__doc__), 5)
