"""
Checks the second lab predicting language knn function
"""

import unittest
from mock import patch
from lab_2.main import predict_language_knn
from lab_2.main import calculate_distance
from lab_2.main import calculate_distance_manhattan


class PredictLanguageKnnTest(unittest.TestCase):
    """
    Tests predicting language knn function
    """

    def test_predict_language_knn_euclid_ideal(self):
        """
        Ideal predicting language knn with euclid metric scenario
        """
        first_text_vector = [0.55, 0.1, 0.2, 0.5, 0.4, 0.2, 0.29, 0.1, 0.18]
        second_text_vectors = [[0.4, 0.1, 0.4, 0.3, 0, 0.21, 0.11, 0.13, 0],
                               [0.11, 0.45, 0.4, 0.28, 0, 0.12, 0.62, 0.21, 0.35],
                               [0.11, 0.28, 0, 0.1, 0.11, 0.49, 0.23, 0.3, 0.43],
                               [0.13, 0, 0.24, 0.41, 0.12, 0.13, 0.56, 0.14, 0.1],
                               [0.18, 0, 0.2, 0.15, 0.1, 0.11, 0.35, 0.34, 0],
                               [0.15, 0, 0.4, 0.21, 0, 0.09, 0.24, 0.33, 0]]
        language_labels = ['en', 'en', 'de', 'de', 'de', 'de']
        expected = ['de', 0.57297]
        actual = predict_language_knn(first_text_vector, second_text_vectors,
                                      language_labels, 3, metric='euclid')
        self.assertEqual(expected, actual)

    def test_predict_language_knn_manhattan_ideal(self):
        """
        Ideal predicting language knn with manhattan metric scenario
        """
        first_text_vector = [0.13, 0.1, 0.1, 0, 0.17, 0, 0.1, 0, 0]
        second_text_vectors = [[0, 0.2, 0.5, 0.1, 0, 0.23, 0, 0.3, 0],
                               [0.12, 0, 0.4, 0, 0, 0, 0.6, 0.3, 0.35],
                               [0.3, 0.22, 0, 0.11, 0, 0.49, 0, 0.3, 0.35],
                               [0.11, 0, 0.34, 0.1, 0.12, 0.19, 0.8, 0.13, 0.1],
                               [0.11, 0.42, 0.2, 0.1, 0.1, 0.11, 0.34, 0.3, 0],
                               [0.1, 0, 0.44, 0.1, 0, 0, 0.34, 0.34, 0]]
        language_labels = ['la', 'la', 'la', 'la', 'de', 'de']
        expected = ['de', 1.26000]
        actual = predict_language_knn(first_text_vector, second_text_vectors,
                                      language_labels, 3, metric='manhattan')
        self.assertEqual(expected, actual)

    def test_predict_language_knn_complex(self):
        """
        Predict language knn with the same number of labels
        """
        first_text_vector = [0.13, 0, 0.1, 0, 0.1, 0, 0.1, 0, 0]
        second_text_vectors = [[0, 0.32, 0, 0.1, 0.5, 0.49, 0.83, 0.3, 0],
                               [0.34, 0.1, 0.4, 0, 0.29, 0, 0.6, 0.65, 0.35],
                               [0.5, 0.25, 0.5, 0.1, 0, 0.49, 0, 0.3, 0.35],
                               [0.12, 0.7, 0.34, 0.1, 0.12, 0, 0.18, 0.12, 0.1],
                               [0.15, 0, 0.2, 0.15, 0.1, 0.16, 0.34, 0.3, 0.14]]
        language_labels = ['en', 'la', 'en', 'la', 'de']
        expected = ['de', 0.47508]
        actual = predict_language_knn(first_text_vector, second_text_vectors,
                                      language_labels, 2, metric='euclid')
        self.assertEqual(expected, actual)

    @patch('lab_2.main.calculate_distance',
           side_effect=calculate_distance)
    def test_calculate_distance_called(self, mock):
        """
        Predict language knn call calculating distance function check
        """
        first_text_vector = [0.15, 0, 0.12, 0, 0.31, 0, 0.15, 0, 0]
        second_text_vectors = [[0.5, 0.2, 0, 0.1, 0, 0.49, 0, 0.35, 0],
                               [0, 0.5, 0.45, 0, 0, 0, 0.54, 0.3, 0.56],
                               [0.5, 0.22, 0.5, 0.1, 0.6, 0.51, 0, 0.3, 0.55],
                               [0.15, 0, 0.36, 0.16, 0.12, 0, 0.87, 0.12, 0.12],
                               [0.17, 0, 0.27, 0.1, 0.1, 0.15, 0.43, 0.33, 0]]
        language_labels = ['la', 'la', 'en', 'en', 'en']
        predict_language_knn(first_text_vector, second_text_vectors,
                             language_labels, 3, metric='euclid')
        self.assertTrue(mock.called)

    @patch('lab_2.main.calculate_distance_manhattan',
           side_effect=calculate_distance_manhattan)
    def test_calculate_distance_manhattan_called(self, mock):
        """
        Predict language knn call calculating distance manhattan function check
        """
        first_text_vector = [0.16, 0, 0.1, 0, 0.1, 0, 0.23, 0, 0]
        second_text_vectors = [[0, 0.2, 0.63, 0.1, 0, 0.49, 0, 0.35, 0.98],
                               [0, 0, 0.4, 0, 0.5, 0, 0.6, 0.3, 0.35],
                               [0, 0.2, 0.76, 0.12, 0, 0.49, 0, 0.3, 0.35],
                               [0.15, 0, 0.34, 0.1, 0.12, 0, 0.89, 0.12, 0.1],
                               [0.12, 0.63, 0.2, 0.17, 0.19, 0.21, 0.54, 0.38, 0],
                               [0.16, 0, 0.46, 0.1, 0, 0, 0.64, 0.38, 0.19]]
        language_labels = ['la', 'la', 'en', 'en', 'de', 'de']
        predict_language_knn(first_text_vector, second_text_vectors,
                             language_labels, 3, metric='manhattan')
        self.assertTrue(mock.called)

    def test_predict_language_knn_metric_bad_input(self):
        """
        Predict language knn invalid inputs check
        """
        bad_inputs = [None, 9, 9.34, 'string', {}, (), True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = predict_language_knn(bad_input, bad_input, bad_input,
                                          bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_predict_language_knn_incorrect_labels(self):
        """
        Predict language knn invalid number of language labels check
        """
        first_text_vector = [0.16, 0.53, 0.1, 0, 0.31, 0, 0.15, 0, 0]
        second_text_vectors = [[0, 0.26, 0, 0.1, 0.23, 0.49, 0, 0.32, 0],
                               [0.67, 0, 0.42, 0.64, 0, 0, 0.6, 0.35, 0.36],
                               [0, 0.22, 0, 0.1, 0.64, 0.49, 0.6, 0.3, 0.36],
                               [0.17, 0, 0.34, 0.15, 0.12, 0, 0.86, 0.12, 0.1],
                               [0.18, 0, 0.2, 0.16, 0.17, 0.11, 0.34, 0.3, 0.73]]
        language_labels = ['la', 'la', 'en']
        expected = None
        actual = predict_language_knn(first_text_vector, second_text_vectors,
                                      language_labels, 3, metric='euclid')
        self.assertEqual(expected, actual)

    def test_predict_language_knn_return_value(self):
        """
        Predict language knn return values check
        """
        first_text_vector = [0.5, 0, 0.12, 0, 0.14, 0, 0.12, 0.3, 0]
        second_text_vectors = [[0, 0.27, 0, 0.12, 0, 0.69, 0.64, 0.64, 0],
                               [0.3, 0, 0.4, 0, 0, 0.5, 0.6, 0.3, 0.35],
                               [0.5, 0.25, 0.6, 0.14, 0, 0.49, 0, 0.3, 0.35],
                               [0.1, 0, 0.39, 0.16, 0.12, 0.76, 0.17, 0.12, 0.1],
                               [0.15, 0, 0.2, 0.1, 0.16, 0.12, 0.34, 0.3, 0],
                               [0.17, 0, 0.64, 0.1, 0.9, 0, 0.36, 0.36, 0]]
        language_labels = ['en', 'la', 'en', 'de', 'de', 'la']
        actual = predict_language_knn(first_text_vector, second_text_vectors,
                                      language_labels, 3, metric='manhattan')
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(isinstance(actual[0], str))
        self.assertTrue(isinstance(actual[1], float))
