"""
Checks the second lab predicting language score function
"""

import unittest
from mock import patch
from lab_2.main import predict_language_score
from lab_2.main import calculate_distance


class PredictLanguageScoreTest(unittest.TestCase):
    """
    Tests predicting language score function
    """

    def test_predict_language_score_ideal(self):
        """
        Ideal predicting language score scenario
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [[0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
                               [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
                               [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35]]
        language_labels = ['en', 'de', 'en']
        expected = ['de', 0.45782]
        actual = predict_language_score(first_text_vector, second_text_vectors, language_labels)
        self.assertEqual(expected, actual)

    @patch('lab_2.main.calculate_distance',
           side_effect=calculate_distance)
    def test_calculate_distance_called(self, mock):
        """
        Predict language score call calculating distance function check
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [[0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
                               [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
                               [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35]]
        language_labels = ['en', 'de', 'en']
        predict_language_score(first_text_vector,
                               second_text_vectors,
                               language_labels)
        self.assertTrue(mock.called)

    def test_predict_language_score_bad_input(self):
        """
        Predict language score invalid input vectors check
        """
        bad_inputs = ['hello', None, 6, True, [None], {}, (), 1.65]
        expected = None
        for bad_input in bad_inputs:
            actual = predict_language_score(bad_input, bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_predict_language_score_incorrect_labels(self):
        """
        Predict language score invalid number of language labels check
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [[0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
                               [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
                               [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35]]
        language_labels = ['en', 'de']
        expected = None
        actual = predict_language_score(first_text_vector, second_text_vectors, language_labels)
        self.assertEqual(expected, actual)

    def test_predict_language_score_return_value(self):
        """
        Predict language score return values check
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [[0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
                               [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
                               [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35]]
        language_labels = ['en', 'de', 'en']
        actual = predict_language_score(first_text_vector, second_text_vectors, language_labels)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(isinstance(actual[0], str))
        self.assertTrue(isinstance(actual[1], float))
