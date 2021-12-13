# pylint: skip-file
"""
Tests BackOffGenerator class
"""

import unittest

from lab_4.main import BackOffGenerator, LetterStorage, tokenize_by_letters, encode_corpus
from lab_4.language_profile import LanguageProfile


class BackOffGeneratorTest(unittest.TestCase):
    """
    check BackOffGenerator class functionality.
    """

    def test_ideal(self):
        """
        ideal case
        """
        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)

        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (1, 2, 3))
        text_generator = BackOffGenerator(profile)
        actual = text_generator.generate_sentence((4,), 4)
        expected = ((4, 5, 1), (1, 2, 1), (1, 3, 2, 4, 1), (1, 11, 5, 9, 1))
        self.assertEqual(actual, expected)

    def test_ideal_bigger_context(self):
        """
        ideal case
        """
        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)

        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (1, 2, 3))
        text_generator = BackOffGenerator(profile)
        actual = text_generator.generate_sentence((2, 3), 4)
        expected = ((2, 3, 2, 4, 5, 1), (1, 2, 1), (1, 3, 2, 10, 1), (1, 11, 5, 9, 1))
        self.assertEqual(actual, expected)

    def test_incorrect_input(self):
        """
        incorrect input
        """
        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)

        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (2,))
        text_generator = BackOffGenerator(profile)
        bad_inputs = [[123], LanguageProfile, profile, None, 'none']
        for bad_input in bad_inputs:
            actual = text_generator._generate_letter(bad_input)
            self.assertEqual(-1, actual)

    def test_ideal_second(self):
        """
        ideal case
        """
        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)

        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (1, 2))
        text_generator = BackOffGenerator(profile)
        actual = text_generator.generate_sentence((100,), 2)
        expected = ((100, 1), (1, 2, 1))
        self.assertEqual(actual, expected)
