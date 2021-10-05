"""
Checks the second lab getting frequency dictionary function
"""

import unittest
from lab_2.main import get_freq_dict


class GetFreqDictTest(unittest.TestCase):
    """
    Tests getting frequency dictionary function
    """

    def test_get_freq_dict_ideal(self):
        """
        Ideal getting frequency dictionary scenario
        """
        expected = {'weather': 0.25, 'sunny': 0.25, 'man': 0.25, 'happy': 0.25}
        actual = get_freq_dict(['weather', 'sunny', 'man', 'happy'])
        self.assertEqual(expected, actual)

    def test_get_freq_dict_complex(self):
        """
        Get frequency dictionary with several same tokens
        """
        expected = {'weather': 0.33333, 'sunny': 0.16667,
                    'man': 0.33333, 'happy': 0.16667}
        actual = get_freq_dict(['weather', 'sunny', 'man', 'happy', 'weather', 'man'])
        self.assertEqual(expected, actual)

    def test_get_freq_dict_bad_input(self):
        """
        Get frequency dictionary invalid input tokens check
        """
        bad_inputs = ['string', {}, (), None, 9, 9.34, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = get_freq_dict(bad_input)
            self.assertEqual(expected, actual)

    def test_get_freq_dict_return_value(self):
        """
        Get frequency dictionary return values check
        """
        tokens = ['man', 'happy']
        expected = 2
        actual = get_freq_dict(tokens)
        self.assertEqual(expected, len(actual))
        for token in tokens:
            self.assertTrue(actual[token])
        self.assertTrue(isinstance(actual[tokens[0]], float))
