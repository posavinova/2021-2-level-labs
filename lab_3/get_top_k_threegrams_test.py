# pylint: skip-file
"""
Tests for Language Profile (get top frequencies)
"""

import unittest

from lab_3.main import NGramTrie, \
    LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    tokenize_by_sentence


class GetTopKThreeGramsTest(unittest.TestCase):
    """
    Tests for Language Profile (get top frequencies)
    """

    def test_get_top_k_ideal(self):
        """
        Get top k by frequency
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

        profile = LanguageProfile(letter_storage=storage, language_name='en')
        self.assertEqual(profile.tries, [])
        self.assertEqual(profile.n_words, [])
        self.assertEqual(profile.language, 'en')
        self.assertEqual(profile.storage, storage)

        profile.create_from_tokens(encoded_text, (2, 3))

        actual = profile.get_top_k_n_grams(3, 3)
        self.assertEqual(len(actual), 3)
        expected = ((1, 2, 1), (1, 3, 2), (3, 2, 4))
        for top_ngram in actual:
            self.assertIn(top_ngram, expected)
