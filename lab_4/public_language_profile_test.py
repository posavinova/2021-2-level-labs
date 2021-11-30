# pylint: skip-file
"""
Tests PublicLanguageProfile class
"""

import unittest
import os

from lab_4.main import PublicLanguageProfile, LetterStorage, tokenize_by_letters, encode_corpus, decode_sentence

CURRENT_DIR_PATH = os.path.dirname(__file__)
PATH_TO_PROFILE = os.path.join(CURRENT_DIR_PATH, 'fi')


class PublicLanguageProfileTest(unittest.TestCase):
    """
    check PublicLanguageProfile class functionality.
    """

    def test_ideal(self):
        """
        ideal case
        """
        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)

        letter_id = storage.get_id('w')
        volume = storage.get_letter_count()

        profile = PublicLanguageProfile(letter_storage=storage, language_name='fi')
        self.assertEqual(profile.open(PATH_TO_PROFILE), 0)
        self.assertEqual(profile.n_words, [15184556, 16912812, 13033049])
        self.assertEqual(profile.language, 'fi')
        self.assertEqual(len(profile.tries), 3)

        letter_id_after_update = profile.storage.get_id('w')
        self.assertEqual(letter_id_after_update, letter_id)

        self.assertGreater(len(profile.storage.storage), volume)

        expected_uni_gram_frequencies = (174458, 1217244, 43435)
        expected_bi_gram_frequencies = (97283, 61263, 66763)
        expected_three_gram_frequencies = (2281, 2388, 2153)

        for expected_uni, expected_bi, expected_three in zip(expected_uni_gram_frequencies,
                                                             expected_bi_gram_frequencies,
                                                             expected_three_gram_frequencies):
            self.assertIn(expected_uni, profile.tries[0].n_gram_frequencies.values())
            self.assertIn(expected_bi, profile.tries[1].n_gram_frequencies.values())
            self.assertIn(expected_three, profile.tries[2].n_gram_frequencies.values())

    def test_bad_input(self):
        """
        ideal case
        """
        text = '''I wish I loved the Human Race'''.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)

        profile = PublicLanguageProfile(letter_storage=storage, language_name='fi')
        bad_inputs = [None, 123, storage, []]
        for bad_input in bad_inputs:
            self.assertEqual(profile.open(bad_input), 1)
