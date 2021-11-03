# pylint: skip-file
"""
Tests for Language Profile (bi-grams)
"""

import unittest

from lab_3.main import NGramTrie, LetterStorage, encode_corpus, LanguageProfile


class CreateLanguageProfileBiGramsTest(unittest.TestCase):
    """
    checks for Language Profile (bi-grams).
    """

    def test_create_profile_ideal(self):
        """
        Create profile from data
        """

        text = (
            (('_', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_')),
        )
        storage = LetterStorage()
        storage.update(text)
        encoded_text = encode_corpus(storage, text)
        trie = NGramTrie(n=2, letter_storage=storage)
        trie.extract_n_grams(encoded_text)

        profile = LanguageProfile(letter_storage=storage, language_name='en')
        self.assertEqual(profile.tries, [])
        self.assertEqual(profile.n_words, [])
        self.assertEqual(profile.language, 'en')
        self.assertEqual(profile.storage, storage)

        self.assertEqual(profile.create_from_tokens(encoded_text, (2,)), 0)
        self.assertEqual(len(profile.tries), 1)
        self.assertEqual(len(profile.n_words), 1)
        self.assertEqual(profile.n_words, [11])
        self.assertEqual(trie.n_grams, profile.tries[0].n_grams)

    def test_create_profile_bad_input(self):
        """
        Tests with bad inputs
        """

        text = (
            (('_', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_')),
        )
        storage = LetterStorage()
        storage.update(text)

        profile = LanguageProfile(letter_storage=storage, language_name='en')

        bad_inputs = [None, 123, 'asd', LetterStorage]
        for bad_input in bad_inputs:
            self.assertEqual(profile.create_from_tokens(bad_input, (2,)), 1)
            self.assertEqual(profile.tries, [])
            self.assertEqual(profile.n_words, [])

        for bad_input in bad_inputs:
            self.assertEqual(profile.create_from_tokens((
                (('_', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_')),
            ), bad_input), 1)
            self.assertEqual(profile.tries, [])
            self.assertEqual(profile.n_words, [])
