#!/usr/bin/python3
"""Test State Module"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test State Class"""

    def __init__(self, *args, **kwargs):
        """Init method"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test_name method"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import state

        self.assertIsNotNone(state.__doc__)
        self.assertGreater(len(state.__doc__), 5)

        self.assertIsNotNone(State.__doc__)
        self.assertGreater(len(State.__doc__), 5)

        self.assertIsNotNone(State.cities.__doc__)
        self.assertGreater(len(State.cities.__doc__), 5)
