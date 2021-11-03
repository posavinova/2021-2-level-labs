# pylint: skip-file
"""
Tests for NGramTrie (five-grams)
"""

import unittest

from lab_3.main import NGramTrie, \
    LetterStorage, \
    encode_corpus, \
    tokenize_by_sentence


class FillNgramStorageWithFiveGramsTest(unittest.TestCase):
    """
    checks for NGram storage (five-grams).
    """

    def test_extract_ngrams_ideal(self):
        """
        Extract (five-grams) from the given data
        """

        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        text = tokenize_by_sentence(text)
        storage = LetterStorage()
        storage.update(text)
        encoded_text = encode_corpus(storage, text)
        trie = NGramTrie(n=5, letter_storage=storage)
        self.assertEqual(trie.extract_n_grams(encoded_text), 0)

        expected = ((((1, 4, 5, 6, 1),), ((1, 7, 8, 9, 1),), ((1, 10, 11, 11, 12), (10, 11, 11, 12, 1)),
                     ((1, 13, 2, 12, 14), (13, 2, 12, 14, 1)), (
                         (1, 12, 15, 2, 6), (12, 15, 2, 6, 10), (15, 2, 6, 10, 16), (2, 6, 10, 16, 14),
                         (6, 10, 16, 14, 1)),
                     ((1, 8, 9, 17, 1),), (
                         (1, 17, 2, 18, 8), (17, 2, 18, 8, 18), (2, 18, 8, 18, 12), (18, 8, 18, 12, 11),
                         (8, 18, 12, 11, 15), (18, 12, 11, 15, 1)), ((1, 8, 9, 17, 1),),
                     ((1, 12, 15, 11, 8), (12, 15, 11, 8, 12), (15, 11, 8, 12, 1)),
                     ((1, 12, 14, 5, 18), (12, 14, 5, 18, 11), (14, 5, 18, 11, 1)), ((1, 12, 13, 5, 1),), (
                         (1, 2, 10, 16, 5), (2, 10, 16, 5, 18), (10, 16, 5, 18, 12), (16, 5, 18, 12, 5),
                         (5, 18, 12, 5, 15),
                         (18, 12, 5, 15, 18), (12, 5, 15, 18, 1)), ((1, 19, 6, 18, 12), (19, 6, 18, 12, 1)),
                     ((1, 12, 14, 11, 1),), ((1, 18, 8, 10, 11), (18, 8, 10, 11, 1))),)

        self.assertEqual(expected, trie.n_grams)
