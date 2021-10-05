"""
Checks the second lab getting language profiles function
"""

import unittest
from mock import patch
from lab_2.main import get_language_profiles
from lab_2.main import get_freq_dict


class GetLanguageProfilesTest(unittest.TestCase):
    """
    Tests getting language profiles function
    """

    def test_get_language_profiles_ideal(self):
        """
        Ideal getting language profiles scenario
        """
        corpus = [['the', 'boy', 'is', 'playing', 'football'],
                  ['der', 'junge', 'der', 'fussball', 'spielt']]
        labels = ['en', 'de']
        expected = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2, 'playing': 0.2, 'football': 0.2},
                    'de': {'der': 0.4, 'junge': 0.2, 'fussball': 0.2, 'spielt': 0.2}}
        actual = get_language_profiles(corpus, labels)
        self.assertEqual(expected, actual)

    @patch('lab_2.main.get_freq_dict',
           side_effect=get_freq_dict)
    def test_get_freq_dict_called(self, mock):
        """
        Get language profiles call getting frequency dictionary function check
        """
        corpus = [['the', 'boy', 'is', 'playing', 'football'],
                  ['der', 'junge', 'der', 'fussball', 'spielt']]
        labels = ['en', 'de']
        get_language_profiles(corpus, labels)
        self.assertTrue(mock.called)

    def test_get_language_profiles_bad_input(self):
        """
        Get language profiles invalid input corpus or labels check
        """
        bad_inputs = ['string', {}, (), None, 9, 9.34, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = get_language_profiles(bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_get_language_profiles_return_values(self):
        """
        Get frequency dictionary return values check
        """
        corpus = [['the', 'boy', 'is', 'playing', 'football'],
                  ['der', 'junge', 'der', 'fussball', 'spielt']]
        labels = ['en', 'de']
        expected = 2
        actual = get_language_profiles(corpus, labels)
        self.assertEqual(expected, len(actual))
        for label in labels:
            self.assertTrue(actual[label])
        self.assertTrue(isinstance(actual[labels[0]], dict))
