"""
Checks the second lab calculating distance function
"""

import unittest
from lab_2.main import calculate_distance


class CalculateDistanceTest(unittest.TestCase):
    """
    Tests calculating distance function
    """

    def test_calculate_distance_ideal(self):
        """
        Ideal calculating distance scenario
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vector = [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0]
        expected = 0.73491
        actual = calculate_distance(first_text_vector, second_text_vector)
        self.assertEqual(expected, actual)

    def test_calculate_distance_bad_input(self):
        """
        Calculate distance invalid input vectors check
        """
        bad_inputs = ['bye', {}, (), None, 2, 1.54, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = calculate_distance(bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_calculate_distance_return_value(self):
        """
        Calculate distance return values check
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vector = [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0]
        actual = calculate_distance(first_text_vector, second_text_vector)
        self.assertTrue(isinstance(actual, float))
