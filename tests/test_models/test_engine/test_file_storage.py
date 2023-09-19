#!/usr/bin/python3
"""Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os

from models.user import User


class test_fileStorage(unittest.TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertTrue(os.path.exists('file.json'))

    def test_empty(self):
        """Data is saved to file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """Load from an empty file"""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """BaseModel save method calls storage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """Confirm __file_path is string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """FileStorage object storage created"""
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_delete(self):
        """Verify that the delete method removes objects from storage"""
        # Create a BaseModel object and add it to storage
        new = BaseModel()
        storage.new(new)
        storage.save()

        # Verify that the object is initially in storage
        self.assertIn(new, storage.all(BaseModel).values())

        # Delete the object from storage
        storage.delete(new)

        # Verify that the object is no longer in storage
        self.assertNotIn(new, storage.all(BaseModel).values())

    def test_all_with_filter(self):
        """Verify that all method returns objects of a specified class"""
        # Create two BaseModel objects and one User object
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        user1 = User()

        # Add the objects to storage
        storage.new(base_model1)
        storage.new(base_model2)
        storage.new(user1)
        storage.save()

        # Retrieve all BaseModel objects using the filter
        base_models = storage.all(BaseModel)

        # Retrieve all User objects using the filter
        user_models = storage.all(User)

        # Verify that both BaseModel objects are in the filtered result
        self.assertIn(base_model1, base_models.values())
        self.assertIn(base_model2, base_models.values())

        # Verify that the User object is not in the filtered result
        self.assertNotIn(base_model1, user_models.values())

    def test_all_without_filter(self):
        """
        Verify that all method returns all
        objects when no filter is provided
        """
        # Create two BaseModel objects and one User object
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        user = User()

        # Add the objects to storage
        storage.new(base_model1)
        storage.new(base_model2)
        storage.new(user)
        storage.save()

        # Retrieve all objects without a filter
        all_objects = storage.all()

        # Verify that all objects are in the result
        self.assertIn(base_model1, all_objects.values())
        self.assertIn(base_model2, all_objects.values())
        self.assertIn(user, all_objects.values())

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models.engine import file_storage
        from models.engine.file_storage import FileStorage

        self.assertIsNotNone(file_storage.__doc__)
        self.assertGreater(len(file_storage.__doc__), 5)

        self.assertIsNotNone(FileStorage.__doc__)
        self.assertGreater(len(FileStorage.__doc__), 5)

        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertGreater(len(FileStorage.all.__doc__), 5)

        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertGreater(len(FileStorage.new.__doc__), 5)

        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertGreater(len(FileStorage.save.__doc__), 5)

        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertGreater(len(FileStorage.reload.__doc__), 5)

        self.assertIsNotNone(FileStorage.delete.__doc__)
        self.assertGreater(len(FileStorage.delete.__doc__), 5)
