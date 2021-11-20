# pylint: skip-file
"""
Tests for NGramTrie (frequencies calculation)
"""

import unittest

from lab_3.main import NGramTrie, LetterStorage, encode_corpus, tokenize_by_sentence


class CalculateNgramFrequenciesTest(unittest.TestCase):
    """
    checks for NGram storage (frequencies calculation).
    """

    def test_calculate_ngram_frequencies_ideal(self):
        """
        Calculate n-gram frequencies
        """

        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()
        text = tokenize_by_sentence(text)
        storage = LetterStorage()
        storage.update(text)
        encoded_text = encode_corpus(storage, text)
        trie = NGramTrie(n=2, letter_storage=storage)
        trie.extract_n_grams(encoded_text)
        self.assertEqual(trie.get_n_grams_frequencies(), 0)

        expected = {(1, 2): 15, (2, 1): 11, (1, 3): 10, (3, 2): 5, (2, 4): 5,
                    (4, 5): 5, (5, 1): 5, (1, 6): 4, (6, 7): 2, (7, 8): 2,
                    (8, 9): 2, (9, 10): 5, (10, 1): 6, (1, 11): 6, (11, 5): 4,
                    (5, 9): 4, (9, 1): 6, (1, 5): 1, (5, 12): 1, (12, 13): 1,
                    (13, 14): 1, (14, 15): 2, (15, 1): 3, (1, 16): 1, (16, 14): 1,
                    (14, 17): 2, (17, 9): 3, (2, 11): 3, (11, 4): 1, (4, 1): 3,
                    (1, 4): 1, (4, 2): 1, (2, 6): 1, (6, 6): 2, (6, 18): 2,
                    (18, 1): 4, (1, 19): 2, (19, 14): 1, (6, 2): 2, (2, 20): 2,
                    (20, 9): 2, (3, 14): 3, (14, 18): 2, (11, 1): 4, (14, 6): 2,
                    (6, 20): 2, (20, 4): 2, (11, 14): 1, (1, 14): 2, (15, 10): 1,
                    (3, 5): 2, (9, 15): 1, (14, 13): 1, (13, 1): 1, (2, 15): 1,
                    (15, 11): 1, (11, 16): 1, (16, 7): 1, (7, 10): 1, (10, 12): 1,
                    (12, 17): 1, (11, 7): 1, (7, 1): 1, (1, 7): 1, (7, 15): 1,
                    (15, 9): 1, (5, 7): 1, (7, 12): 1, (12, 21): 1, (21, 5): 1,
                    (5, 11): 1, (5, 14): 1, (14, 11): 1, (1, 22): 1, (22, 7): 1,
                    (7, 6): 1, (19, 12): 1, (12, 15): 1}

        self.assertEqual(expected, trie.n_gram_frequencies)

    def test_calculate_ngram_frequencies_empty(self):
        """
        Test with empty input
        """

        storage = LetterStorage()
        trie = NGramTrie(n=2, letter_storage=storage)
        empty_encoded_text = ()
        trie.extract_n_grams(empty_encoded_text)
        self.assertEqual(trie.get_n_grams_frequencies(), 1)
        self.assertTrue(not trie.n_gram_frequencies)
