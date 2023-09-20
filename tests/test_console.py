#!/usr/bin/python3
"""
Test module for HBNBCommand class:
a class that contains the entry point of the command interpreter.
"""


import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    TestHBNBCommand class:
    Test suite for the HBNBCommand class in console.py
    """
    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        import console

        self.assertIsNotNone(console.__doc__)
        self.assertGreater(len(console.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertGreater(len(HBNBCommand.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertGreater(len(HBNBCommand.do_all.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertGreater(len(HBNBCommand.do_count.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertGreater(len(HBNBCommand.do_create.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertGreater(len(HBNBCommand.do_destroy.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertGreater(len(HBNBCommand.do_EOF.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_help.__doc__)
        self.assertGreater(len(HBNBCommand.do_help.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertGreater(len(HBNBCommand.do_quit.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertGreater(len(HBNBCommand.do_update.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertGreater(len(HBNBCommand.emptyline.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertGreater(len(HBNBCommand.do_show.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertGreater(len(HBNBCommand.do_quit.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertGreater(len(HBNBCommand.do_EOF.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertGreater(len(HBNBCommand.emptyline.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_help.__doc__)
        self.assertGreater(len(HBNBCommand.do_help.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.help_all.__doc__)
        self.assertGreater(len(HBNBCommand.help_all.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.help_count.__doc__)
        self.assertGreater(len(HBNBCommand.help_count.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.help_create.__doc__)
        self.assertGreater(len(HBNBCommand.help_create.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.help_destroy.__doc__)
        self.assertGreater(len(HBNBCommand.help_destroy.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.help_show.__doc__)
        self.assertGreater(len(HBNBCommand.help_show.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.help_update.__doc__)
        self.assertGreater(len(HBNBCommand.help_update.__doc__), 5)
