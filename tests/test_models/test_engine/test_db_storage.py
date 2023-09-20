#!/usr/bin/python3
"""Module for testing db storage"""
import unittest
import os
from models.engine.db_storage import DBStorage


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db", "test_class_for_db_storage_only"
)
class TestDBStorage(unittest.TestCase):
    """Class to test the db storage method"""
    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class, and methods.
        """
        from models.engine import db_storage

        self.assertIsNotNone(db_storage.__doc__)
        self.assertGreater(len(db_storage.__doc__), 5)

        self.assertIsNotNone(DBStorage.__doc__)
        self.assertGreater(len(DBStorage.__doc__), 5)

        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertGreater(len(DBStorage.__init__.__doc__), 5)

        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertGreater(len(DBStorage.all.__doc__), 5)

        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertGreater(len(DBStorage.new.__doc__), 5)

        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertGreater(len(DBStorage.save.__doc__), 5)

        self.assertIsNotNone(DBStorage.reload.__doc__)
        self.assertGreater(len(DBStorage.reload.__doc__), 5)

        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertGreater(len(DBStorage.delete.__doc__), 5)


if __name__ == '__main__':
    unittest.main()
