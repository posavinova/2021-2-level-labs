# pylint: skip-file
"""
Tests for NGramTrie (log probabilities calculation)
"""

import unittest

from lab_3.main import NGramTrie, \
    LetterStorage, \
    encode_corpus, \
    tokenize_by_sentence


class CalculateLogProbabilitiesThreeGramsTest(unittest.TestCase):
    """
    Tests for NGramTrie (log probabilities calculation)
    """

    def test_calculate_log_probabilities_ideal(self):
        """
        Calculate log probability
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
        trie.get_n_grams_frequencies()
        self.assertEqual(trie.calculate_log_probabilities(), 0)

        expected = {(1, 2, 1): -0.3101549283038396, (1, 3, 2): -0.6931471805599453,
                    (3, 2, 4): 0.0, (2, 4, 5): 0.0, (4, 5, 1): 0.0,
                    (1, 6, 7): -0.6931471805599453, (6, 7, 8): 0.0,
                    (7, 8, 9): 0.0, (8, 9, 10): 0.0, (9, 10, 1): 0.0,
                    (1, 11, 5): -0.40546510810816444, (11, 5, 9): -0.2876820724517809,
                    (5, 9, 1): -0.2876820724517809, (1, 5, 12): 0.0,
                    (5, 12, 13): 0.0, (12, 13, 14): 0.0, (13, 14, 15): 0.0,
                    (14, 15, 1): -0.6931471805599453, (1, 16, 14): 0.0,
                    (16, 14, 17): 0.0, (14, 17, 9): 0.0, (17, 9, 1): -0.40546510810816444,
                    (1, 2, 11): -1.6094379124341003, (2, 11, 4): -1.0986122886681098,
                    (11, 4, 1): 0.0, (1, 4, 2): 0.0, (4, 2, 6): 0.0, (2, 6, 6): 0.0,
                    (6, 6, 18): 0.0, (6, 18, 1): 0.0, (1, 19, 14): -0.6931471805599453,
                    (19, 14, 17): 0.0, (1, 6, 2): -0.6931471805599453, (6, 2, 20): 0.0,
                    (2, 20, 9): 0.0, (20, 9, 10): 0.0, (1, 3, 14): -1.2039728043259361,
                    (3, 14, 18): -0.40546510810816444, (14, 18, 1): 0.0,
                    (2, 11, 1): -0.40546510810816444, (3, 14, 6): -1.0986122886681098,
                    (14, 6, 20): 0.0, (6, 20, 4): 0.0, (20, 4, 1): 0.0,
                    (1, 11, 14): -1.791759469228055, (11, 14, 6): 0.0,
                    (1, 14, 15): -0.6931471805599453, (14, 15, 10): -0.6931471805599453,
                    (15, 10, 1): 0.0, (1, 3, 5): -1.6094379124341003,
                    (3, 5, 9): -0.6931471805599453, (5, 9, 15): -1.3862943611198906,
                    (9, 15, 1): 0.0, (1, 14, 13): -0.6931471805599453, (14, 13, 1): 0.0,
                    (1, 2, 15): -2.70805020110221, (2, 15, 11): 0.0, (15, 11, 16): 0.0,
                    (11, 16, 7): 0.0, (16, 7, 10): 0.0, (7, 10, 12): 0.0, (10, 12, 17): 0.0,
                    (12, 17, 9): 0.0, (17, 9, 10): -1.0986122886681098,
                    (1, 11, 7): -1.791759469228055, (11, 7, 1): 0.0,
                    (1, 7, 15): 0.0, (7, 15, 9): 0.0, (15, 9, 1): 0.0,
                    (11, 5, 7): -1.3862943611198906, (5, 7, 12): 0.0,
                    (7, 12, 21): 0.0, (12, 21, 5): 0.0, (21, 5, 11): 0.0,
                    (5, 11, 1): 0.0, (3, 5, 14): -0.6931471805599453,
                    (5, 14, 11): 0.0, (14, 11, 1): 0.0, (1, 22, 7): 0.0,
                    (22, 7, 6): 0.0, (7, 6, 6): 0.0, (1, 19, 12): -0.6931471805599453,
                    (19, 12, 15): 0.0, (12, 15, 1): 0.0}
        self.assertEqual(expected, trie.n_gram_log_probabilities)

    def test_calculate_log_probabilities_empty(self):
        """
        Empty frequencies
        """
        storage = LetterStorage()
        trie = NGramTrie(n=3, letter_storage=storage)
        self.assertEqual(trie.calculate_log_probabilities(), 1)

        self.assertEqual({}, trie.n_gram_log_probabilities)
