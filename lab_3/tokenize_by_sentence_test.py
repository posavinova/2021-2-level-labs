# pylint: skip-file
"""
Tests for tokenize_by_sentence_function
"""

import unittest

from lab_3.main import tokenize_by_sentence


class TokenizeBySentenceTest(unittest.TestCase):
    """
    checks for tokenize_by_sentence function.
    """

    def test_tokenize_by_sentence_ideal(self):
        """
        Tests that tokenize_by_sentence function
            can handle ideal two sentence input
        """
        text = 'She is happy. He is happy.'
        expected = (
            (('_', 's', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_')),
            (('_', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_'))
        )
        actual = tokenize_by_sentence(text)
        self.assertEqual(expected, actual)

    def test_tokenize_by_sentence_multiline_text(self):
        """
            Tests that tokenize_by_sentence function
                can handle ideal multi-line text
            """
        text = '''I wish I loved the Human Race.
I wish I loved its silly face.
I wish I liked the way it walks.
I wish I liked the way it talks.
And when I am introduced to one.
I wish I thought What Jolly Fun.'''.lower()
        expected = ((('_', 'i', '_'),
                     ('_', 'w', 'i', 's', 'h', '_'),
                     ('_', 'i', '_'),
                     ('_', 'l', 'o', 'v', 'e', 'd', '_'),
                     ('_', 't', 'h', 'e', '_'),
                     ('_', 'h', 'u', 'm', 'a', 'n', '_'),
                     ('_', 'r', 'a', 'c', 'e', '_')),
                    (('_', 'i', '_'),
                     ('_', 'w', 'i', 's', 'h', '_'),
                     ('_', 'i', '_'),
                     ('_', 'l', 'o', 'v', 'e', 'd', '_'),
                     ('_', 'i', 't', 's', '_'),
                     ('_', 's', 'i', 'l', 'l', 'y', '_'),
                     ('_', 'f', 'a', 'c', 'e', '_')),
                    (('_', 'i', '_'),
                     ('_', 'w', 'i', 's', 'h', '_'),
                     ('_', 'i', '_'),
                     ('_', 'l', 'i', 'k', 'e', 'd', '_'),
                     ('_', 't', 'h', 'e', '_'),
                     ('_', 'w', 'a', 'y', '_'),
                     ('_', 'i', 't', '_'),
                     ('_', 'w', 'a', 'l', 'k', 's', '_')),
                    (('_', 'i', '_'),
                     ('_', 'w', 'i', 's', 'h', '_'),
                     ('_', 'i', '_'),
                     ('_', 'l', 'i', 'k', 'e', 'd', '_'),
                     ('_', 't', 'h', 'e', '_'),
                     ('_', 'w', 'a', 'y', '_'),
                     ('_', 'i', 't', '_'),
                     ('_', 't', 'a', 'l', 'k', 's', '_')),
                    (('_', 'a', 'n', 'd', '_'),
                     ('_', 'w', 'h', 'e', 'n', '_'),
                     ('_', 'i', '_'),
                     ('_', 'a', 'm', '_'),
                     ('_', 'i', 'n', 't', 'r', 'o', 'd', 'u', 'c', 'e', 'd', '_'),
                     ('_', 't', 'o', '_'),
                     ('_', 'o', 'n', 'e', '_')),
                    (('_', 'i', '_'),
                     ('_', 'w', 'i', 's', 'h', '_'),
                     ('_', 'i', '_'),
                     ('_', 't', 'h', 'o', 'u', 'g', 'h', 't', '_'),
                     ('_', 'w', 'h', 'a', 't', '_'),
                     ('_', 'j', 'o', 'l', 'l', 'y', '_'),
                     ('_', 'f', 'u', 'n', '_')))
        actual = tokenize_by_sentence(text)
        self.assertEqual(expected, actual)

    def test_tokenize_by_sentence_punctuation_marks(self):
        """
        Tests that tokenize_by_sentence function
            can process and ignore different punctuation marks
        """
        text = 'The, first sentence - nice. The second sentence: bad!'
        expected = (
            (('_', 't', 'h', 'e', '_'), ('_', 'f', 'i', 'r', 's', 't', '_'),
             ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_'), ('_', 'n', 'i', 'c', 'e', '_')),
            (('_', 't', 'h', 'e', '_'), ('_', 's', 'e', 'c', 'o', 'n', 'd', '_'),
             ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_'), ('_', 'b', 'a', 'd', '_'))
        )
        actual = tokenize_by_sentence(text)
        self.assertEqual(expected, actual)

    def test_tokenize_by_sentence_dirty_text(self):
        """
        Tests that tokenize_by_sentence function
            can handle text filled with inappropriate characters
        """
        text = 'The first% sentence><. The sec&*ond sent@ence #.'
        expected = (
            (('_', 't', 'h', 'e', '_'), ('_', 'f', 'i', 'r', 's', 't', '_'),
             ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_')),
            (('_', 't', 'h', 'e', '_'), ('_', 's', 'e', 'c', 'o', 'n', 'd', '_'),
             ('_', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', '_'))
        )
        actual = tokenize_by_sentence(text)
        self.assertEqual(expected, actual)

    def test_tokenize_by_sentence_incorrect_input(self):
        """
        Tests that tokenize_by_sentence function
            can handle incorrect input cases
        """
        bad_inputs = [[], {}, (), None, 9, 9.34, True]
        expected = ()
        for bad_input in bad_inputs:
            actual = tokenize_by_sentence(bad_input)
            self.assertEqual(expected, actual)

    def test_tokenize_by_sentence_complex(self):
        """
        Tests that tokenize_by_sentence function
            can handle complex split case
        """
        text = 'Mar#y wa$nted, to swim. However, she was afraid of sharks.'
        expected = (
            (('_', 'm', 'a', 'r', 'y', '_'), ('_', 'w', 'a', 'n', 't', 'e', 'd', '_'),
             ('_', 't', 'o', '_'), ('_', 's', 'w', 'i', 'm', '_')),
            (('_', 'h', 'o', 'w', 'e', 'v', 'e', 'r', '_'), ('_', 's', 'h', 'e', '_'),
             ('_', 'w', 'a', 's', '_'), ('_', 'a', 'f', 'r', 'a', 'i', 'd', '_'),
             ('_', 'o', 'f', '_'), ('_', 's', 'h', 'a', 'r', 'k', 's', '_'))
        )
        actual = tokenize_by_sentence(text)
        self.assertEqual(expected, actual)

    def test_tokenize_by_sentence_empty_sentence(self):
        """
        Tests that tokenize_by_sentence function
            can handle empty sentence input
        """
        text = ''

        expected = ()
        actual = tokenize_by_sentence(text)
        self.assertEqual(expected, actual)

    def test_tokenize_by_sentence_inappropriate_sentence(self):
        """
        Tests that tokenize_by_sentence function
            can handle inappropriate sentence input
        """
        text = '$#&*@#$*#@)'

        expected = ()
        actual = tokenize_by_sentence(text)
        self.assertEqual(expected, actual)
