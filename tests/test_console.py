#!/usr/bin/python3
""" chech the new feature for the console """
# import console
import unittest
import os
import sys
sys.path.append(os.path.abspath('..'))
HBNBCommand = __import__('console').HBNBCommand


class test_Console(unittest.TestCase):
    """ class to chech the new feature for the console """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)

    def setUp(self):
        """ Set up test environment """

    def test_doCreate(self):
        """ """
        from models import storage
        line = 'Place city_id="0001" user_id="0001" name="My_little_house" \
            number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 \
            latitude=37.773972 longitude=-122.431297'
        HBNBCommand().do_create(line)
        new_object = None
        for k, v in storage.all(HBNBCommand.classes["Place"]).items():
            if v.city_id == "0001":
                new_object = v

        self.assertNotEqual(new_object, None)
        self.assertEqual(new_object.name, "My little house")
        self.assertEqual(new_object.number_rooms, 4)
        self.assertEqual(new_object.latitude, 37.773972)
