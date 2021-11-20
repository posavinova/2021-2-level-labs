# pylint: skip-file
"""
Tests for Language Profile (n-grams)
"""

import unittest

from lab_3.main import NGramTrie, \
    LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    tokenize_by_sentence


class CreateLanguageProfileNGramsTest(unittest.TestCase):
    """
    checks for Language Profile (n-grams).
    """

    def test_create_profile_ideal(self):
        """
        Create profile from data
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

        trie_threegrams = NGramTrie(n=3, letter_storage=storage)
        trie_threegrams.extract_n_grams(encoded_text)

        profile = LanguageProfile(letter_storage=storage, language_name='en')
        self.assertEqual(profile.tries, [])
        self.assertEqual(profile.n_words, [])
        self.assertEqual(profile.language, 'en')
        self.assertEqual(profile.storage, storage)

        self.assertEqual(profile.create_from_tokens(encoded_text, (2, 3)), 0)
        self.assertEqual(len(profile.tries), 2)
        self.assertEqual(len(profile.n_words), 2)
        self.assertEqual(profile.n_words, [78, 84])
        self.assertEqual(trie.n_grams, profile.tries[0].n_grams)
        self.assertEqual(trie_threegrams.n_grams, profile.tries[1].n_grams)
