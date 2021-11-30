# pylint: skip-file
"""
Tests LikelihoodBasedTextGenerator class
"""

import unittest

from lab_4.main import LikelihoodBasedTextGenerator, LetterStorage, tokenize_by_letters, encode_corpus, decode_sentence
from lab_4.language_profile import LanguageProfile


class LikelihoodBasedTextGeneratorTest(unittest.TestCase):
    """
    check LikelihoodBasedTextGenerator class functionality.
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
        profile.create_from_tokens(encoded, (2, 3))
        text_generator = LikelihoodBasedTextGenerator(profile)
        actual = text_generator.generate_sentence((4,), 4)
        expected = ((4, 5, 1), (1, 2, 1), (1, 2, 1), (1, 2, 1))
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
        text_generator = LikelihoodBasedTextGenerator(profile)
        bad_inputs = [[123], LanguageProfile, profile, None, 'none', ()]
        for bad_input in bad_inputs:
            actual = text_generator._generate_letter(bad_input)
            self.assertEqual(-1, actual)

            actual = text_generator._calculate_maximum_likelihood(bad_input, (1,))
            self.assertEqual(-1, actual)

            actual = text_generator._calculate_maximum_likelihood(1, bad_input)
            self.assertEqual(-1, actual)

    def test_not_existing_context(self):
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
        profile.create_from_tokens(encoded, (2, 3))
        text_generator = LikelihoodBasedTextGenerator(profile)
        actual = text_generator.generate_sentence((4, 20), 4)
        expected = ((4, 20, 1), (1,), (1,), (1,))
        self.assertEqual(actual, expected)
