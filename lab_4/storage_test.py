# pylint: skip-file
"""
Tests Storage class
"""

import unittest
from unittest.mock import patch

from lab_4.storage import Storage


class StorageTest(unittest.TestCase):
    """
    check Storage class functionality.
    """

    def test_correct_instance_creation(self):
        """
        storage instance creates with correct attributes
        """
        storage = Storage()
        expected = {}
        self.assertEqual(storage.storage, expected)

    def test_ideal(self):
        """
        letter is added to storage
        """
        storage = Storage()
        letter = 'w'
        expected = 0
        actual = storage._put(letter)
        self.assertTrue(letter in storage.storage)
        self.assertEqual(expected, actual)

    def test_put_none(self):
        """
        none is not added to storage
        """
        storage = Storage()
        letter = None
        expected = -1
        actual = storage._put(letter)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)

    def test_put_not_str(self):
        """
        non string letter is not added to storage
        """
        storage = Storage()
        letter = 123
        expected = -1
        actual = storage._put(letter)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)

    def test_put_existing(self):
        """
        existing letter is not added to storage
        """
        storage = Storage()
        letter = 'w'
        storage._put(letter)
        storage_ = storage.storage
        expected = 0
        actual_exit_code = storage._put(letter)
        self.assertEqual(storage.storage, storage_)
        self.assertEqual(expected, actual_exit_code)

    def test_get_id_ideal(self):
        """
        ideal case for get_id
        """
        storage = Storage()
        storage._put('w')
        actual = storage.get_id('w')
        self.assertTrue(isinstance(actual, int))

    def test_storage_get_id_none(self):
        """
        get_id none
        """
        storage = Storage()
        storage.storage = {'w': 1}
        expected = -1
        actual = storage.get_id(None)
        self.assertEqual(expected, actual)

    def test_storage_get_id_not_str(self):
        """
        id is not str  get_id
        """
        storage = Storage()
        storage.storage = {'w': 1}
        expected = -1
        actual = storage.get_id(123)
        self.assertEqual(expected, actual)

    def test_storage_get_id_not_in_storage(self):
        """
        letter not in storage
        """
        storage = Storage()
        storage.storage = {'w': 1}
        expected = -1
        actual = storage.get_id('a')
        self.assertEqual(expected, actual)

    def test_storage_get_element(self):
        storage = Storage()
        storage.storage = {'w': 1}
        expected = 'w'
        actual = storage.get_element(1)
        self.assertEqual(expected, actual)

    def test_storage_get_element_bad_input(self):
        storage = Storage()
        storage.storage = {'w': 1}
        expected = -1
        actual = storage.get_element(None)
        self.assertEqual(expected, actual)

    def test_storage_get_element_not_existent(self):
        storage = Storage()
        storage.storage = {'w': 1}
        expected = -1
        actual = storage.get_element(3)
        self.assertEqual(expected, actual)

    def test_storage_update_ideal(self):
        """
        ideal case for update
        """
        storage = Storage()
        sentences = (
            (('_', 't', 'e', 's', 't', '_'),),
        )
        expected = 0
        actual = storage.update(sentences)
        self.assertEqual(len(storage.storage), 4)
        self.assertEqual(expected, actual)

    def test_storage_update_duplicates(self):
        """
        ideal case for update
        """
        storage = Storage()
        sentences = (
            (('_', 't', 'e', 's', 't', '_'),),
            (('_', 't', 'e', 's', 't', '_'),)
        )
        expected = 0
        actual = storage.update(sentences)
        self.assertEqual(len(storage.storage), 4)
        self.assertEqual(expected, actual)

    def test_storage_update_empty(self):
        """
        ideal case for update
        """
        storage = Storage()
        sentences = ()
        expected = 0
        actual = storage.update(sentences)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)

    def test_storage_update_none(self):
        """
        ideal case for update
        """
        storage = Storage()
        sentences = None
        expected = -1
        actual = storage.update(sentences)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)

    def test_storage_update_not_tuple(self):
        """
        ideal case for update
        """
        storage = Storage()
        sentences = [
            (('_', 't', 'e', 's', 't', '_'),),
            (('_', 's', 'e', 'c', 'o', 'n', 'd', '_'),)
        ]
        expected = -1
        actual = storage.update(sentences)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)

    @patch('lab_4.storage.Storage._put', side_effect=Storage()._put)
    def test_storage_update_calls_required_function(self, mock):
        """
        ideal case for update calling put_letter method
        """
        storage = Storage()
        sentences = (
            (('_', 't', 'e', 's', 't', '_'),),
        )
        storage.update(sentences)
        self.assertTrue(mock.called)
