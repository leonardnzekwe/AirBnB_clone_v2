#!/usr/bin/python3
"""Test Review Module"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test Review Class"""

    def __init__(self, *args, **kwargs):
        """Init method"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test_place_id method"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test_user_id method"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test_text method"""
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import review

        self.assertIsNotNone(review.__doc__)
        self.assertGreater(len(review.__doc__), 5)

        self.assertIsNotNone(Review.__doc__)
        self.assertGreater(len(Review.__doc__), 5)
