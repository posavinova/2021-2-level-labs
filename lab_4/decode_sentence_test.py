# pylint: skip-file
"""
Tests decode_sentence function
"""

import unittest

from lab_4.main import LetterStorage
from lab_4.main import decode_sentence, encode_corpus


class DecodeSentenceTest(unittest.TestCase):
    """
    checks for decode_sentence function.
    """

    def test_ideal(self):
        """
        decode ideal case
        """
        letter_storage = LetterStorage()

        original_corpus = (
            ('_', 't', 'e', 's', 't', '_'),
            ('_', 's', 'e', 'c', 'o', 'n', 'd', '_')
        )

        letter_storage.update(original_corpus)

        encoded = encode_corpus(letter_storage, original_corpus)

        actual = decode_sentence(letter_storage, encoded)
        self.assertEqual(original_corpus, actual)
        for text in actual:
            for character in text:
                self.assertTrue(isinstance(character, str))

    def test_inappropriate_sentence(self):
        """
        Incorrect input
        """
        letter_storage = LetterStorage()
        bad_inputs = [None, 123, 'test', [], {}]

        expected = ()
        for bad_input in bad_inputs:
            actual = decode_sentence(letter_storage, bad_input)
            self.assertEqual(expected, actual)

    def test_inappropriate_storage_instance(self):
        """
        Incorrect letter storage
        """
        bad_inputs = [None, 123, 'test', [], {}]

        sentences = (
            (1, 3, 4, 1),
            (1, 3, 4, 1, 2)
        )

        expected = ()
        for bad_input in bad_inputs:
            actual = decode_sentence(bad_input, sentences)
            self.assertEqual(expected, actual)

    def test_empty_sentence(self):
        """
        Empty input corpus
        """
        letter_storage = LetterStorage()
        sentences = ()

        expected = ()
        actual = decode_sentence(letter_storage, sentences)
        self.assertEqual(expected, actual)
