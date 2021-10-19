# pylint: skip-file
"""
Checks the first profile saving function
"""

import unittest
from lab_1.main import save_profile


class SaveProfileTest(unittest.TestCase):
    """
    Tests profile saving function
    """

    def test_load_profile_ideal(self):
        """
        Ideal scenario
        """
        profile = {"name": "de", "freq": {"vorlesungen": 2, "bei": 1, "hause": 1,
                                          "studienbuch": 1, "auslande": 1,
                                          "verschiedenen": 1, "an": 4, "freunde": 1,
                                          "bin": 1, "gute": 1, "minuten": 1,
                                          "kantine": 1, "kommilitonen": 1, "deutsche": 1},
                   "n_words": 129}
        expected = 0
        actual = save_profile(profile)
        self.assertEqual(expected, actual)

    def test_save_profile_bad_input_type(self):
        """
        Bad input scenario
        """
        expected = 1

        bad_inputs = ['goodbye', (), None, 9, 9.34, True, [None], []]
        for bad_input in bad_inputs:
            actual = save_profile(bad_input)
            self.assertEqual(expected, actual)

    def test_save_profile_bad_input_complex(self):
        """
        Bad input complex scenario
        """
        expected = 1

        bad_inputs = ['goodbye', {}, None, 9, 9.34, True, [None], []]
        for index in range(len(bad_inputs) - 2):
            profile = {'name': bad_inputs[index],
                       'freq': bad_inputs[index+1],
                       'n_words': bad_inputs[index+2]}
        actual = save_profile(profile)
        self.assertEqual(expected, actual)
