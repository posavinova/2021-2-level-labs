# pylint: skip-file
"""
Checks the first lab language profile creation function
"""

import unittest
from main import create_language_profile


class CreateLanguageProfileTest(unittest.TestCase):
    """
    Tests language profile creation function
    """

    STOP_WORDS_EN = ['the', 'a', 'is']
    STOP_WORDS_DE = ['muss', 'das', 'was']

    def test_create_profile_ideal(self):
        """
        Ideal scenario
        """
        expected = {'name': 'en',
                    'freq': {'happy': 2, 'he': 1, 'man': 1},
                    'n_words': 3}
        language_name = 'en'
        text = 'he is a happy happy man'
        actual = create_language_profile(language_name, text, CreateLanguageProfileTest.STOP_WORDS_EN)
        self.assertEqual(expected, actual)

    def test_create_profile_no_stop_words(self):
        """
        Ideal scenario with no stop words
        """
        expected = {'name': 'en',
                    'freq': {'happy': 2, 'he': 1, 'man': 1, 'is': 1, 'a': 1},
                    'n_words': 5}
        language_name = 'en'
        text = 'he is a happy happy man'
        actual = create_language_profile(language_name, text, [])
        self.assertEqual(expected, actual)

    def test_create_profile_deutsch_ideal(self):
        """
        Ideal scenario with deutsch
        """
        expected = {'name': 'de',
                    'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                             'möchte': 1, 'vielleicht': 1, 'überlegen': 1},
                    'n_words': 7}
        language_name = 'de'
        text = 'Ich weiß nicht was ich machen möchte. Vielleicht ich muss das überlegen'
        actual = create_language_profile(language_name, text, CreateLanguageProfileTest.STOP_WORDS_DE)
        self.assertEqual(expected, actual)

    def test_create_profile_bad_input(self):
        """
        Bad input scenario
        """
        expected = None
        language_name = 'de'
        text = []
        actual = create_language_profile(language_name, text, CreateLanguageProfileTest.STOP_WORDS_DE)
        self.assertEqual(expected, actual)

    def test_create_profile_bad_input_lang_name(self):
        """
        Bad input scenario, language name
        """
        expected = None
        language_name = 123
        text = 'Ich weiß nicht was ich machen möchte. Vielleicht ich muss das überlegen'
        actual = create_language_profile(language_name, text, CreateLanguageProfileTest.STOP_WORDS_DE)
        self.assertEqual(expected, actual)

    def test_create_profile_bad_input_stop_words(self):
        """
        Bad input scenario, language name
        """
        expected = None
        language_name = 'de'
        text = 'Ich weiß nicht was ich machen möchte. Vielleicht ich muss das überlegen'
        actual = create_language_profile(language_name, text, None)
        self.assertEqual(expected, actual)
