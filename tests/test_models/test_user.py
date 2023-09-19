#!/usr/bin/python3
"""Test User Module"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test User Class"""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test_first_name method"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test_last_name method"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test_email method"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test_password method"""
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import user

        self.assertIsNotNone(user.__doc__)
        self.assertGreater(len(user.__doc__), 5)

        self.assertIsNotNone(User.__doc__)
        self.assertGreater(len(User.__doc__), 5)
