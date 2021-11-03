# pylint: skip-file
"""
Tests for NGramTrie (frequencies calculation)
"""

import unittest

from lab_3.main import NGramTrie, LetterStorage, encode_corpus, tokenize_by_sentence


class CalculateThreeGramFrequenciesTest(unittest.TestCase):
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
        trie = NGramTrie(n=3, letter_storage=storage)
        trie.extract_n_grams(encoded_text)
        self.assertEqual(trie.get_n_grams_frequencies(), 0)

        expected = {(1, 2, 1): 7, (1, 3, 2): 5, (3, 2, 4): 5, (2, 4, 5): 5, (4, 5, 1): 5, (1, 6, 7): 2, (6, 7, 8): 2,
                    (7, 8, 9): 2, (8, 9, 10): 2, (9, 10, 1): 5, (1, 11, 5): 4, (11, 5, 9): 3, (5, 9, 1): 3,
                    (1, 5, 12): 1, (5, 12, 13): 1, (12, 13, 14): 1, (13, 14, 15): 1, (14, 15, 1): 1, (1, 16, 14): 1,
                    (16, 14, 17): 1, (14, 17, 9): 2, (17, 9, 2): 2, (9, 2, 1): 3, (1, 2, 11): 3, (2, 11, 4): 1,
                    (11, 4, 1): 1, (1, 4, 2): 1, (4, 2, 6): 1, (2, 6, 6): 1, (6, 6, 18): 2, (6, 18, 1): 2,
                    (1, 19, 14): 1, (19, 14, 17): 1, (1, 6, 2): 2, (6, 2, 20): 2, (2, 20, 9): 2, (20, 9, 10): 2,
                    (1, 3, 14): 3, (3, 14, 18): 2, (14, 18, 1): 2, (2, 11, 1): 2, (3, 14, 6): 1, (14, 6, 20): 2,
                    (6, 20, 4): 2, (20, 4, 2): 1, (4, 2, 1): 1, (1, 11, 14): 1, (11, 14, 6): 1, (20, 4, 14): 1,
                    (4, 14, 15): 1, (14, 15, 10): 1, (15, 10, 1): 1, (1, 3, 5): 2, (3, 5, 9): 1, (5, 9, 15): 1,
                    (9, 15, 1): 1, (1, 14, 13): 1, (14, 13, 1): 1, (1, 2, 15): 1, (2, 15, 11): 1, (15, 11, 16): 1,
                    (11, 16, 7): 1, (16, 7, 10): 1, (7, 10, 12): 1, (10, 12, 17): 1, (12, 17, 9): 1, (17, 9, 10): 1,
                    (1, 11, 7): 1, (11, 7, 1): 1, (1, 7, 15): 1, (7, 15, 9): 1, (15, 9, 2): 1, (11, 5, 7): 1,
                    (5, 7, 12): 1, (7, 12, 21): 1, (12, 21, 5): 1, (21, 5, 11): 1, (5, 11, 1): 1, (3, 5, 14): 1,
                    (5, 14, 11): 1, (14, 11, 1): 1, (1, 22, 7): 1, (22, 7, 6): 1, (7, 6, 6): 1, (1, 19, 12): 1,
                    (19, 12, 15): 1, (12, 15, 1): 1}

        self.assertEqual(expected, trie.n_gram_frequencies)
