"""
Checks the second lab calculating distance sparse function
"""

import unittest
from lab_2.main import calculate_distance_sparse


class CalculateDistanceSparseTest(unittest.TestCase):
    """
    Tests calculating distance sparse function
    """

    def test_calculate_distance_sparse_ideal(self):
        """
        Ideal calculating distance sparse scenario
        """
        first_text_vector = [[0, 0.4], [2, 0.2], [4, 0.2], [6, 0.2]]
        second_text_vector = [[1, 0.1], [3, 0.1], [5, 0.49], [7, 0.3]]
        expected = 0.79379
        actual = calculate_distance_sparse(first_text_vector, second_text_vector)
        self.assertEqual(expected, actual)

    def test_calculate_distance_sparse_bad_input(self):
        """
        Calculate distance sparse invalid input vectors check
        """
        bad_inputs = [{}, (), None, 'string', True, [None], 9, 9.34]
        expected = None
        for bad_input in bad_inputs:
            actual = calculate_distance_sparse(bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_calculate_distance_sparse_return_value(self):
        """
        Calculate distance sparse return values check
        """
        first_text_vector = [[0, 0.4], [2, 0.2], [4, 0.2], [6, 0.2]]
        second_text_vector = [[1, 0.1], [3, 0.1], [5, 0.49], [7, 0.3]]
        actual = calculate_distance_sparse(first_text_vector, second_text_vector)
        self.assertTrue(isinstance(actual, float))
