"""
Checks the second lab getting language features function
"""

import unittest
from lab_2.main import get_language_features


class GetLanguageFeaturesTest(unittest.TestCase):
    """
    Tests getting language features function
    """

    def test_get_language_features_ideal(self):
        """
        Ideal getting language features scenario
        """
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2,
                                    'fussball': 0.2, 'spielt': 0.2}}
        expected = ['boy', 'der', 'football', 'fussball',
                    'is', 'junge', 'playing', 'spielt', 'the']
        actual = get_language_features(language_profiles)
        self.assertEqual(expected, actual)

    def test_get_language_features_bad_input(self):
        """
        Get language features invalid input tokens check
        """
        bad_inputs = ['string', {}, (), None, 9, 9.34, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = get_language_features(bad_input)
            self.assertEqual(expected, actual)

    def test_get_language_features_return_value(self):
        """
        Get language features return values check
        """
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2,
                                    'fussball': 0.2, 'spielt': 0.2}}
        expected = 9
        actual = get_language_features(language_profiles)
        self.assertEqual(expected, len(actual))
        for language_profile in language_profiles.values():
            for word in language_profile:
                self.assertIn(word, actual)
        self.assertTrue(isinstance(actual[0], str))
