# pylint: skip-file
"""
Tests decode_corpus function
"""

import unittest

from lab_3.main import LetterStorage
from lab_3.main import decode_corpus, encode_corpus


class DecodeCorpusTest(unittest.TestCase):
    """
    checks for decode_corpus function.
    """

    def test_decode_corpus_ideal(self):
        """
        decode ideal case
        """
        letter_storage = LetterStorage()

        original_corpus = (
            (('_', 't', 'e', 's', 't', '_'),),
            (('_', 's', 'e', 'c', 'o', 'n', 'd', '_'),)
        )

        letter_storage.update(original_corpus)

        encoded = encode_corpus(letter_storage, original_corpus)

        actual = decode_corpus(letter_storage, encoded)
        self.assertEqual(original_corpus, actual)
        for text in actual:
            for sentence in text:
                for character in sentence:
                    self.assertTrue(isinstance(character, str))

    def test_decode_corpus_inappropriate_sentence(self):
        """
        Incorrect input
        """
        letter_storage = LetterStorage()
        bad_inputs = [None, 123, 'test', [], {}]

        expected = ()
        for bad_input in bad_inputs:
            actual = decode_corpus(letter_storage, bad_input)
            self.assertEqual(expected, actual)

    def test_decode_corpus_inappropriate_storage_instance(self):
        """
        Incorrect letter storage
        """
        bad_inputs = [None, 123, 'test', [], {}]

        sentences = (
            ((1, 3, 4, 1),),
            ((1, 3, 4, 1, 2),)
        )

        expected = ()
        for bad_input in bad_inputs:
            actual = decode_corpus(bad_input, sentences)
            self.assertEqual(expected, actual)

    def test_decode_corpus_empty_sentence(self):
        """
        Empty input corpus
        """
        letter_storage = LetterStorage()
        sentences = ()

        expected = ()
        actual = decode_corpus(letter_storage, sentences)
        self.assertEqual(expected, actual)
