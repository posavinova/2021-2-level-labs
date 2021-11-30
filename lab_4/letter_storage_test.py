# pylint: skip-file
"""
Tests LetterStorage class
"""

import unittest

from lab_4.main import LetterStorage


class StorageTest(unittest.TestCase):
    """
    check LetterStorage class functionality.
    """

    def test_storage_update_ideal(self):
        """
        ideal case for update
        """
        storage = LetterStorage()
        sentences = (
            ('_', 't', 'e', 's', 't', '_'),
        )
        expected = 0
        actual = storage.update(sentences)
        self.assertEqual(len(storage.storage), 4)
        self.assertEqual(expected, actual)
        self.assertEqual(storage.get_letter_count(), 4)

    def test_storage_update_duplicates(self):
        """
        ideal case for update
        """
        storage = LetterStorage()
        sentences = (
            ('_', 't', 'e', 's', 't', '_'),
            ('_', 't', 'e', 's', 't', '_')
        )
        expected = 0
        actual = storage.update(sentences)
        self.assertEqual(len(storage.storage), 4)
        self.assertEqual(expected, actual)

    def test_storage_update_empty(self):
        """
        ideal case for update
        """
        storage = LetterStorage()
        sentences = ()
        expected = 0
        actual = storage.update(sentences)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)

    def test_storage_update_none(self):
        """
        ideal case for update
        """
        storage = LetterStorage()
        sentences = None
        expected = -1
        actual = storage.update(sentences)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)
        self.assertEqual(storage.get_letter_count(), -1)

    def test_storage_update_not_tuple(self):
        """
        ideal case for update
        """
        storage = LetterStorage()
        sentences = [
            (('_', 't', 'e', 's', 't', '_'),),
            (('_', 's', 'e', 'c', 'o', 'n', 'd', '_'),)
        ]
        expected = -1
        actual = storage.update(sentences)
        self.assertEqual(storage.storage, {})
        self.assertEqual(expected, actual)
