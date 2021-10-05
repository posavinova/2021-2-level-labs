"""
Checks the second lab getting sparse vector function
"""

import unittest
from mock import patch
from lab_2.main import get_sparse_vector
from lab_2.main import get_language_features


class GetSparseVectorTest(unittest.TestCase):
    """
    Tests getting sparse vector function
    """

    def test_get_sparse_vector_ideal(self):
        """
        Ideal getting sparse vector scenario
        """
        tokens = ['the', 'german', 'tech', 'specialist', 'is', 'playing', 'games']
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2, 'fussball': 0.2, 'spielt': 0.2}}
        expected = [[4, 0.2], [6, 0.2], [8, 0.2]]
        actual = get_sparse_vector(tokens, language_profiles)
        for element in expected:
            self.assertIn(element, actual)
        self.assertEqual(len(actual), len(expected))

    @patch('lab_2.main.get_language_features',
           side_effect=get_language_features)
    def test_get_language_features_called(self, mock):
        """
        Get sparse vector call getting language features function check
        """
        tokens = ['the', 'german', 'tech', 'specialist', 'is', 'playing', 'games']
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2, 'fussball': 0.2, 'spielt': 0.2}}
        get_sparse_vector(tokens, language_profiles)
        self.assertTrue(mock.called)

    def test_get_sparse_vector_bad_input(self):
        """
        Get sparse vector invalid inputs check
        """
        bad_inputs = [{}, (), None, 9, 'string', 9.34, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = get_sparse_vector(bad_input, bad_input)
            self.assertEqual(expected, actual)

    def test_get_sparse_vector_return_value(self):
        """
        Get sparse vector return values check
        """
        tokens = ['the', 'german', 'tech', 'specialist', 'is', 'playing', 'games']
        language_profiles = {'en': {'the': 0.2, 'boy': 0.2, 'is': 0.2,
                                    'playing': 0.2, 'football': 0.2},
                             'de': {'der': 0.4, 'junge': 0.2, 'fussball': 0.2, 'spielt': 0.2}}
        actual = get_sparse_vector(tokens, language_profiles)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(isinstance(actual[0], list))
        self.assertTrue(isinstance(actual[0][0], int))
        self.assertTrue(isinstance(actual[0][1], float))
