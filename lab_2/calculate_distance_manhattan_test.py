"""
Checks the second lab calculating distance manhattan function
"""

import unittest
from lab_2.main import calculate_distance_manhattan


class CalculateDistanceManhattanTest(unittest.TestCase):
    """
    Tests calculating distance manhattan function
    """

    def test_calculate_distance_manhattan_ideal(self):
        """
        Ideal calculating distance manhattan scenario
        """
        first_text_vector = [0.1, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vector = [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0]
        expected = 1.79
        actual = calculate_distance_manhattan(first_text_vector, second_text_vector)
        self.assertEqual(expected, actual)

    def test_calculate_distance_bad_input(self):
        """
        Calculate distance manhattan invalid input vectors check
        """
        bad_inputs = ['hi', {}, (), None, 17, 99.14, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = calculate_distance_manhattan(bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_calculate_distance_manhattan_return_value(self):
        """
        Calculate distance manhattan return values check
        """
        first_text_vector = [0.1, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vector = [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0]
        actual = calculate_distance_manhattan(first_text_vector, second_text_vector)
        self.assertTrue(isinstance(actual, float))
