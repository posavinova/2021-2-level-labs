# pylint: skip-file
"""
Checks the first lab language detection function
"""

import unittest
from main import detect_language


class DetectLanguageTest(unittest.TestCase):
    """
    Tests language detection function
    """

    def test_detect_language_ideal(self):
        """
        Ideal scenario
        """

        unknown_profile = {'name': 'unk',
                           'freq': {'happy': 5, 'she': 2, 'man': 1},
                           'n_words': 3}

        en_profile = {'name': 'en',
                      'freq': {'happy': 2, 'he': 1, 'man': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        expected = en_profile['name']
        actual = detect_language(unknown_profile, en_profile, de_profile, 2)
        self.assertEqual(expected, actual)

    def test_detect_language_deutsch_ideal(self):
        """
        Ideal scenario with deutsch
        """

        unknown_profile = {'name': 'unk',
                           'freq': {'weiß': 5, 'überlegen': 2, 'nicht': 1},
                           'n_words': 3}

        en_profile = {'name': 'en',
                      'freq': {'happy': 2, 'he': 1, 'man': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        expected = de_profile['name']
        actual = detect_language(unknown_profile, en_profile, de_profile, 2)
        self.assertEqual(expected, actual)

    def test_detect_language_alphabetical(self):
        """
        Detect language when scores are the same
        """

        unknown_profile = {'name': 'unk',
                           'freq': {'computer': 5, 'the': 2, 'world': 1},
                           'n_words': 3}

        en_profile = {'name': 'en',
                      'freq': {'computer': 2, 'she': 1, 'woman': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'sie': 3, 'haben': 1, 'viel': 1, 'computer': 2},
                      'n_words': 4}

        expected = de_profile['name']
        actual = detect_language(unknown_profile, en_profile, de_profile, 2)
        self.assertEqual(expected, actual)

    def test_detect_language_bad_input(self):
        """
        Bad input scenario
        """

        unknown_profile = []

        en_profile = {'name': 'en',
                      'freq': {'happy': 2, 'he': 1, 'man': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        expected = None
        actual = detect_language(unknown_profile, en_profile, de_profile, 2)
        self.assertEqual(expected, actual)

    def test_detect_language_bad_input_profile(self):
        """
        Bad input scenario
        """

        unknown_profile = {'name': 'de',
                           'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                                    'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                           'n_words': 8}

        en_profile = 123

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        expected = None
        actual = detect_language(unknown_profile, en_profile, de_profile, 2)
        self.assertEqual(expected, actual)
