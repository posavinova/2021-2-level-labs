# pylint: skip-file
"""
Checks the first lab language detection function
"""

import unittest
from main import detect_language_advanced


class DetectLanguageAdvancedTest(unittest.TestCase):
    """
    Tests language detection advanced function
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

        profiles = [en_profile, de_profile]

        expected = en_profile['name']
        actual = detect_language_advanced(unknown_profile, profiles, [], 2)
        self.assertEqual(expected, actual)

    def test_detect_language_ideal_deutsch(self):
        """
        Ideal scenario
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

        profiles = [en_profile, de_profile]

        expected = de_profile['name']
        actual = detect_language_advanced(unknown_profile, profiles, [], 2)
        self.assertEqual(expected, actual)

    def test_detect_language_from_en(self):
        """
        Choose from en only
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

        profiles = [en_profile, de_profile]

        expected = en_profile['name']
        actual = detect_language_advanced(unknown_profile, profiles, ['en'], 2)
        self.assertEqual(expected, actual)

    def test_detect_language_from_third(self):
        """
        Choose from two out of three profiles only
        """

        unknown_profile = {'name': 'unk',
                           'freq': {'weiß': 5, 'überlegen': 2, 'nicht': 1, 'machen': 1},
                           'n_words': 4}

        en_profile = {'name': 'en',
                      'freq': {'happy': 2, 'he': 1, 'man': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        second_de_profile = {'name': 'de_austria',
                             'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1},
                             'n_words': 4}

        profiles = [en_profile, de_profile, second_de_profile]

        expected = second_de_profile['name']
        actual = detect_language_advanced(unknown_profile, profiles, ['en', 'de_austria'], 2)
        self.assertEqual(expected, actual)

    def test_detect_language_bad_input(self):
        """
        Bad input scenario
        """

        unknown_profile = [{'name': 'unk',
                           'freq': {'weiß': 5, 'überlegen': 2, 'nicht': 1, 'machen': 1},
                           'n_words': 4}]

        en_profile = {'name': 'en',
                      'freq': {'happy': 2, 'he': 1, 'man': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        second_de_profile = {'name': 'de_austria',
                             'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1},
                             'n_words': 4}

        profiles = [en_profile, de_profile, second_de_profile]

        expected = None
        actual = detect_language_advanced(unknown_profile, profiles, ['en', 'de_austria'], 2)
        self.assertEqual(expected, actual)

    def test_detect_language_bad_input_lang_profiles(self):
        """
        Bad input scenario
        """

        unknown_profile = {'name': 'unk',
                           'freq': {'weiß': 5, 'überlegen': 2, 'nicht': 1, 'machen': 1},
                           'n_words': 4}

        en_profile = {'name': 'en',
                      'freq': {'happy': 2, 'he': 1, 'man': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        second_de_profile = {'name': 'de_austria',
                             'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1},
                             'n_words': 4}

        profiles = None

        expected = None
        actual = detect_language_advanced(unknown_profile, profiles, ['en', 'de_austria'], 2)
        self.assertEqual(expected, actual)

    def test_detect_language_not_existing_lang(self):
        """
        Bad input with non-existing language
        """

        unknown_profile = {'name': 'unk',
                           'freq': {'weiß': 5, 'überlegen': 2, 'nicht': 1, 'machen': 1},
                           'n_words': 4}

        en_profile = {'name': 'en',
                      'freq': {'happy': 2, 'he': 1, 'man': 1},
                      'n_words': 3}

        de_profile = {'name': 'de',
                      'freq': {'ich': 3, 'weiß': 1, 'nicht': 1, 'machen': 1,
                               'möchte': 1, 'vielleicht': 1, 'überlegen': 1, 'man': 1},
                      'n_words': 8}

        profiles = [en_profile, de_profile]

        expected = None
        actual = detect_language_advanced(unknown_profile, profiles, ['de_austria'], 2)
        self.assertEqual(expected, actual)
