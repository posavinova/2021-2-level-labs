"""
Checks the second lab getting text vector function
"""

import unittest
from lab_2.main import get_text_vector


class GetTextVectorTest(unittest.TestCase):
    """
    Tests getting text vector function
    """

    def test_get_text_vector_ideal_english(self):
        """
        Ideal getting english text vector scenario
        """

        original_text = ['this', 'boy', 'is', 'playing', 'football']
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2,
                                    'fussball': 0.2, 'spielt': 0.2}}
        expected = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        actual = get_text_vector(original_text, language_profiles)
        self.assertEqual(expected, actual)

    def test_get_text_vector_ideal_german(self):
        """
        Ideal getting german text vector scenario
        """

        original_text = ['der', 'junge', 'der', 'fussball', 'spielt']
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2,
                                    'fussball': 0.2, 'spielt': 0.2}}
        expected = [0, 0.4, 0, 0.2, 0, 0.2, 0, 0.2, 0]
        actual = get_text_vector(original_text, language_profiles)
        self.assertEqual(expected, actual)

    def test_get_text_vector_bad_input(self):
        """
        Get text vector invalid input text and language profiles check
        """
        bad_inputs = ['string', {}, (), None, 9, 9.34, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = get_text_vector(bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_get_text_vector_return_value(self):
        """
        Get text vector return values check
        """
        original_text = ['this', 'boy', 'is', 'playing', 'football']
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2,
                                    'fussball': 0.2, 'spielt': 0.2}}
        expected_length = 9
        expected_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        actual = get_text_vector(original_text, language_profiles)
        self.assertEqual(expected_length, len(actual))
        for index, element in enumerate(expected_vector):
            self.assertEqual(actual[index], element)
        self.assertTrue(isinstance(actual[0], float))
