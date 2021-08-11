#!/usr/bin/python3
""" Module for testing file storage"""

from models import storage
from os import getenv
import MySQLdb
from models.state import State
import unittest
import os
import sys
sys.path.append(os.path.abspath('../../../'))


print(getenv("HBNB_TYPE_STORAGE"))
if getenv("HBNB_TYPE_STORAGE") == "db":
    class test_dbStorage(unittest.TestCase):
        """ Class to test the file storage method """

        def setUp(self):
            """ Set up test environment """
            """del_list = []
            for key in storage.all().keys():
                del_list.append(key)
            for key in del_list:
                storage.delete(storage.all()[key])"""
            self.host = getenv("HBNB_MYSQL_HOST")
            self.user = getenv("HBNB_MYSQL_USER")
            self.paswd = getenv("HBNB_MYSQL_PWD")
            self.db = getenv("HBNB_MYSQL_DB")

        def test_obj_list_empty(self):
            """ __objects is initially empty """
            self.assertEqual(len(storage.all()), 0)

        def test_new(self):
            """ New object is correctly added to __objects """
            new = State(name="California")
            new.save()
            for obj in storage.all().values():
                temp = obj
            self.assertTrue(temp is obj)

        def test_all(self):
            """ __objects is properly returned """
            new = State(name="California")
            temp = storage.all()
            self.assertIsInstance(temp, dict)

        def test_base_model_instantiation(self):
            """ File is not created on BaseModel save """
            db = MySQLdb.connect(
                host=self.host, user=self.user, passwd=self.paswd, db=self.db)
            cursor = db.cursor()
            sqlStatement = "SELECT COUNT(id) AS count FROM states"
            cursor.execute(sqlStatement)
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            db.close()
            new = State(name="California")
            new.save()

        def test_empty(self):
            """ Data is saved to file """
            new = State(name="California")
            thing = new.to_dict()
            new.save()
            new2 = State(name="California")
            self.assertNotEqual(os.path.getsize('file.json'), 0)

        def test_save(self):
            """ FileStorage save method """
            new = State(name="California")
            storage.save()
            self.assertTrue(os.path.exists('file.json'))

        def test_reload(self):
            """ Storage file is successfully loaded to __objects """
            new = State(name="California")
            storage.save()
            storage.reload()
            for obj in storage.all().values():
                loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

        def test_reload_empty(self):
            """ Load from an empty file """
            with open('file.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()

        def test_reload_from_nonexistent(self):
            """ Nothing happens if file does not exist """
            self.assertEqual(storage.reload(), None)

        def test_type_path(self):
            """ Confirm __file_path is string """
            self.assertEqual(type(storage._FileStorage__file_path), str)

        def test_type_objects(self):
            """ Confirm __objects is a dict """
            self.assertEqual(type(storage.all()), dict)

        def test_key_format(self):
            """ Key is properly formatted """
            new = State(name="California")
            _id = new.to_dict()['id']
            for key in storage.all().keys():
                temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

        def test_storage_var_created(self):
            """ FileStorage object storage created """
            from models.engine.file_storage import FileStorage
            print(type(storage))
            self.assertEqual(type(storage), FileStorage)
