# pylint: skip-file
"""
Tests for tokenize_by_letters_function
"""

import unittest

from lab_4.main import tokenize_by_letters


class TokenizeByLettersTest(unittest.TestCase):
    """
    checks for tokenize_by_letters function.
    """

    def test_ideal(self):
        """
        Tests that tokenize_by_letters function
            can handle ideal two sentence input
        """
        text = 'She is happy. He is happy.'
        expected = (('_', 's', 'h', 'e', '_'),
                    ('_', 'i', 's', '_'),
                    ('_', 'h', 'a', 'p', 'p', 'y', '_'),
                    ('_', 'h', 'e', '_'),
                    ('_', 'i', 's', '_'),
                    ('_', 'h', 'a', 'p', 'p', 'y', '_'))
        actual = tokenize_by_letters(text)
        self.assertEqual(expected, actual)

    def test_marks_ideal(self):
        """
        Tests that tokenize_by_letters function
            can process and ignore different punctuation marks
        """
        text = 'The, first sentence - nice. The second sentence: bad!'
        expected = (('_', 't', 'h', 'e', '_'),
                    ('_', 'f', 'i', 'r', 's', 't', '_'),
                    ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_'),
                    ('_', 'n', 'i', 'c', 'e', '_'),
                    ('_', 't', 'h', 'e', '_'),
                    ('_', 's', 'e', 'c', 'o', 'n', 'd', '_'),
                    ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_'),
                    ('_', 'b', 'a', 'd', '_'))
        actual = tokenize_by_letters(text)
        self.assertEqual(expected, actual)

    def test_dirty_text(self):
        """
        Tests that tokenize_by_letters function
            can handle text filled with inappropriate characters
        """
        text = 'The first% sentence><. The sec&*ond sent@ence #.'
        expected = (('_', 't', 'h', 'e', '_'),
                    ('_', 'f', 'i', 'r', 's', 't', '_'),
                    ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_'),
                    ('_', 't', 'h', 'e', '_'),
                    ('_', 's', 'e', 'c', 'o', 'n', 'd', '_'),
                    ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_'))
        actual = tokenize_by_letters(text)
        self.assertEqual(expected, actual)

    def test_incorrect_input(self):
        """
        Tests that tokenize_by_letters function
            can handle incorrect input cases
        """
        bad_inputs = [[], {}, (), None, 9, 9.34, True]
        expected = -1
        for bad_input in bad_inputs:
            actual = tokenize_by_letters(bad_input)
            self.assertEqual(expected, actual)

    def test_complex(self):
        """
        Tests that tokenize_by_letters function
            can handle complex split case
        """
        text = 'Mar#y wa$nted, to swim. However, she was afraid of sharks.'
        expected = (('_', 'm', 'a', 'r', 'y', '_'),
                    ('_', 'w', 'a', 'n', 't', 'e', 'd', '_'),
                    ('_', 't', 'o', '_'),
                    ('_', 's', 'w', 'i', 'm', '_'),
                    ('_', 'h', 'o', 'w', 'e', 'v', 'e', 'r', '_'),
                    ('_', 's', 'h', 'e', '_'),
                    ('_', 'w', 'a', 's', '_'),
                    ('_', 'a', 'f', 'r', 'a', 'i', 'd', '_'),
                    ('_', 'o', 'f', '_'),
                    ('_', 's', 'h', 'a', 'r', 'k', 's', '_'))
        actual = tokenize_by_letters(text)
        self.assertEqual(expected, actual)

    def test_empty_sentence(self):
        """
        Tests that tokenize_by_sentence function
            can handle empty sentence input
        """
        text = ''

        expected = ()
        actual = tokenize_by_letters(text)
        self.assertEqual(expected, actual)

    def test_inappropriate_sentence(self):
        """
        Tests that tokenize_by_letters function
            can handle inappropriate sentence input
        """
        text = '$#&*@#$*#@)'

        expected = ()
        actual = tokenize_by_letters(text)
        self.assertEqual(expected, actual)
