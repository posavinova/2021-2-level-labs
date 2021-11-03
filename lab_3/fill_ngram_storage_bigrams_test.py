# pylint: skip-file
"""
Tests for NGramTrie (bi-grams)
"""

import unittest

from lab_3.main import NGramTrie, LetterStorage, encode_corpus


class FillNgramStorageWithBiGramsTest(unittest.TestCase):
    """
    checks for NGram storage (bi-grams).
    """

    def test_extract_ngrams_ideal(self):
        """
        Extract bi-grams from the given data
        """

        text = (
            (('_', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_')),
        )
        storage = LetterStorage()
        storage.update(text)
        encoded_text = encode_corpus(storage, text)
        trie = NGramTrie(n=2, letter_storage=storage)
        self.assertEqual(trie.extract_n_grams(encoded_text), 0)

        expected = (
            (
                (
                    (1, 2), (2, 3), (3, 1)
                ), (
                    (1, 4), (4, 5), (5, 1)
                ), (
                    (1, 2), (2, 6), (6, 7), (7, 7), (7, 8), (8, 1)
                )
            ),
        )

        self.assertEqual(expected, trie.n_grams)

    def test_extract_ngrams_bad_input(self):
        """
        Tests with bad inputs
        """

        storage = LetterStorage()
        trie = NGramTrie(n=2, letter_storage=storage)
        bad_inputs = (None, 123, 'ads', LetterStorage)
        for bad_input in bad_inputs:
            self.assertTrue(trie.extract_n_grams(bad_input), -1)
            self.assertTrue(not trie.n_grams)

    def test_extract_ngrams_empty(self):
        """
        Test with empty input
        """

        storage = LetterStorage()
        trie = NGramTrie(n=2, letter_storage=storage)
        empty_encoded_text = ()
        self.assertEqual(trie.extract_n_grams(empty_encoded_text), 0)
        self.assertTrue(not trie.n_grams)
