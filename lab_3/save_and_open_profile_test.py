# pylint: skip-file
"""
Tests for Language Profile (saving & opening)
"""

import os
import unittest

from lab_3.main import NGramTrie, \
    LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    tokenize_by_sentence

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))


class SaveLanguageProfileTest(unittest.TestCase):
    """
    checks for Language Profile (saving).
    """

    def test_save_and_open_profile_ideal(self):
        """
        Save & open profile
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

        profile.create_from_tokens(encoded_text, (2, 3))
        self.assertEqual(profile.save(os.path.join(PATH_TO_LAB_FOLDER, 'eng_profile.json')), 0)

        profile_tries = profile.tries
        profile_storage = profile.storage
        profile_n_words = profile.n_words
        lang = profile.language

        # Clear the profile
        profile.tries = []
        profile.n_words = []
        profile.storage = LetterStorage()

        self.assertEqual(profile.open(os.path.join(PATH_TO_LAB_FOLDER, 'eng_profile.json')), 0)

        self.assertEqual(lang, profile.language)
        self.assertEqual(len(profile_storage.storage), len(profile.storage.storage))
        self.assertEqual(profile_n_words, profile.n_words)
        self.assertEqual(len(profile_tries), len(profile.tries))
        self.assertEqual(len(profile_tries[0].n_gram_frequencies), len(profile.tries[0].n_gram_frequencies))
        self.assertEqual(len(profile_tries[1].n_gram_frequencies), len(profile.tries[1].n_gram_frequencies))

    def test_save_and_open_profile_bad_inputs(self):
        """
        Save & open profile bad inputs
        """
        storage = LetterStorage()

        profile = LanguageProfile(letter_storage=storage, language_name='en')

        self.assertEqual(profile.save(None), 1)


        self.assertEqual(profile.open(123), 1)