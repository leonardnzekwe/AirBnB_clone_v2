#!/usr/bin/python3
"""Test Base Model Module"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db", "test_class_for_file_storage_only"
)
class test_basemodel(unittest.TestCase):
    """Test Basemode Class"""

    def __init__(self, *args, **kwargs):
        """Init method"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """setUp method"""
        pass

    def tearDown(self):
        """tearDown method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """test_default method"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """test_kwargs method"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test_kwargs_int method"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """test_str method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """test_todict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """test_kwargs_none method"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """test_kwargs_one method"""
        n = {'name': 'ray'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """test_id method"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test_created method"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """test_updated method"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new_base = BaseModel(**n)
        new_base.save()
        self.assertNotEqual(new_base.created_at, new_base.updated_at)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import base_model

        self.assertIsNotNone(base_model.__doc__)
        self.assertGreater(len(base_model.__doc__), 5)

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertGreater(len(BaseModel.__doc__), 5)

        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertGreater(len(BaseModel.__init__.__doc__), 5)

        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertGreater(len(BaseModel.__str__.__doc__), 5)

        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertGreater(len(BaseModel.save.__doc__), 5)

        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 5)

        self.assertIsNotNone(BaseModel.delete.__doc__)
        self.assertGreater(len(BaseModel.delete.__doc__), 5)
