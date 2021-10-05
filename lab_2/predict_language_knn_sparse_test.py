"""
Checks the second lab predicting language knn sparse function
"""

import unittest
from mock import patch
from lab_2.main import predict_language_knn_sparse
from lab_2.main import calculate_distance_sparse


class PredictLanguageKnnSparseTest(unittest.TestCase):
    """
    Tests predicting language knn sparse function
    """

    def test_predict_language_knn_sparse_ideal(self):
        """
        Ideal predicting language knn sparse scenario
        """
        first_text_vector = [[0, 0.2], [2, 0.2], [4, 0.2], [6, 0.2]]
        second_text_vectors = [[[1, 0.2], [3, 0.1], [5, 0.49], [7, 0.3]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [6, 0.34], [7, 0.3]],
                               [[1, 0.2], [3, 0.1], [5, 0.49],
                                [7, 0.3], [8, 0.35]],
                               [[0, 0.11], [2, 0.34], [3, 0.1],
                                [4, 0.12], [6, 0.8], [7, 0.12], [8, 0.1]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [4, 0.1], [5, 0.11], [6, 0.34], [7, 0.3]],
                               [[2, 0.4], [6, 0.6], [7, 0.3], [8, 0.35]]]
        language_labels = ['en', 'de', 'en', 'en', 'de', 'de']
        expected = ['de', 0.43784]
        actual = predict_language_knn_sparse(first_text_vector,
                                             second_text_vectors,
                                             language_labels, 3)
        self.assertEqual(expected, actual)

    def test_predict_language_knn_sparse_complex(self):
        """
        Predict language knn sparse with the same number of labels
        """
        first_text_vector = [[0, 0.2], [2, 0.2], [4, 0.2], [6, 0.2]]
        second_text_vectors = [[[1, 0.2], [3, 0.1], [5, 0.49], [7, 0.3]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [6, 0.34], [7, 0.3]],
                               [[1, 0.2], [3, 0.1], [5, 0.49],
                                [7, 0.3], [8, 0.35]],
                               [[0, 0.11], [2, 0.34], [3, 0.1],
                                [4, 0.12], [6, 0.8], [7, 0.12], [8, 0.1]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [4, 0.1], [5, 0.11], [6, 0.34], [7, 0.3]]]
        language_labels = ['en', 'de', 'en', 'en', 'de']
        expected = ['de', 0.43784]
        actual = predict_language_knn_sparse(first_text_vector,
                                             second_text_vectors,
                                             language_labels, 3)
        self.assertEqual(expected, actual)

    @patch('lab_2.main.calculate_distance_sparse',
           side_effect=calculate_distance_sparse)
    def test_calculate_distance_called(self, mock):
        """
        Predict language knn sparse call calculating distance function check
        """
        first_text_vector = [[0, 0.2], [2, 0.2], [4, 0.2], [6, 0.2]]
        second_text_vectors = [[[1, 0.2], [3, 0.1], [5, 0.49], [7, 0.3]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [6, 0.34], [7, 0.3]],
                               [[1, 0.2], [3, 0.1], [5, 0.49],
                                [7, 0.3], [8, 0.35]],
                               [[0, 0.11], [2, 0.34], [3, 0.1],
                                [4, 0.12], [6, 0.8], [7, 0.12], [8, 0.1]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [4, 0.1], [5, 0.11], [6, 0.34], [7, 0.3]]]
        language_labels = ['en', 'en', 'en', 'de', 'de']
        predict_language_knn_sparse(first_text_vector,
                                    second_text_vectors,
                                    language_labels, 3)
        self.assertTrue(mock.called)

    def test_predict_language_knn_sparse_bad_input(self):
        """
        Predict language knn sparse invalid inputs check
        """
        bad_inputs = ['string', {}, (), None, 9, 9.34, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = predict_language_knn_sparse(bad_input, bad_input,
                                                 bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_predict_language_knn_sparse_incorrect_labels(self):
        """
        Predict language knn sparse invalid number of language labels check
        """
        first_text_vector = [[0, 0.2], [2, 0.2], [4, 0.2], [6, 0.2]]
        second_text_vectors = [[[1, 0.2], [3, 0.1], [5, 0.49], [7, 0.3]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [6, 0.34], [7, 0.3]],
                               [[1, 0.2], [3, 0.1], [5, 0.49],
                                [7, 0.3], [8, 0.35]],
                               [[0, 0.11], [2, 0.34], [3, 0.1],
                                [4, 0.12], [6, 0.8], [7, 0.12], [8, 0.1]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [4, 0.1], [5, 0.11], [6, 0.34], [7, 0.3]]]
        language_labels = ['en', 'en']
        expected = None
        actual = predict_language_knn_sparse(first_text_vector,
                                             second_text_vectors,
                                             language_labels, 3)
        self.assertEqual(expected, actual)

    def test_predict_language_knn_sparse_return_value(self):
        """
        Predict language knn sparse return values check
        """
        first_text_vector = [[0, 0.2], [2, 0.2], [4, 0.2], [6, 0.2]]
        second_text_vectors = [[[1, 0.2], [3, 0.1], [5, 0.49], [7, 0.3]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [6, 0.34], [7, 0.3]],
                               [[1, 0.2], [3, 0.1], [5, 0.49],
                                [7, 0.3], [8, 0.35]],
                               [[0, 0.11], [2, 0.34], [3, 0.1],
                                [4, 0.12], [6, 0.8], [7, 0.12], [8, 0.1]],
                               [[0, 0.1], [2, 0.4], [3, 0.1],
                                [4, 0.1], [5, 0.11], [6, 0.34], [7, 0.3]]]
        language_labels = ['en', 'en', 'en', 'de', 'de']
        actual = predict_language_knn_sparse(first_text_vector,
                                             second_text_vectors,
                                             language_labels, 3)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(isinstance(actual[0], str))
        self.assertTrue(isinstance(actual[1], float))
