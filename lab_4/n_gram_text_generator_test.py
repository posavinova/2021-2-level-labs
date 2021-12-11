# pylint: skip-file
"""
Tests NGramTextGenerator class
"""

import unittest

from lab_4.main import NGramTextGenerator, LetterStorage, tokenize_by_letters, encode_corpus, decode_sentence
from lab_4.language_profile import LanguageProfile


class NGramTextGeneratorTest(unittest.TestCase):
    """
    check NGramTextGenerator class functionality.
    """

    def test_ideal(self):
        """
        ideal case
        """
        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)

        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (2,))
        text_generator = NGramTextGenerator(profile)
        actual = text_generator.generate_sentence((1,), 3)
        expected = ((1, 12, 1), (1, 2, 3, 1), (1, 8, 9, 17, 1))
        self.assertEqual(expected, actual)

        decoded = text_generator.generate_decoded_sentence((1,), 3)
        expected_decoded = 'Yosth casatrite meetwiu.'
        self.assertEqual(decoded, expected_decoded)

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
        text_generator = NGramTextGenerator(profile)
        bad_inputs = [[123], LanguageProfile, profile, None, 'none']
        for bad_input in bad_inputs:
            expected = ()

            actual = text_generator.generate_sentence(bad_input, 3)
            self.assertEqual(expected, actual)

            actual = text_generator.generate_sentence((1,), bad_input)
            self.assertEqual(expected, actual)

            actual = text_generator._generate_letter(bad_input)
            self.assertEqual(-1, actual)

            actual = text_generator._generate_word(bad_input, 10)
            self.assertEqual(expected, actual)

            actual = text_generator._generate_word((1,), bad_input)
            self.assertEqual(expected, actual)

    def test_ideal_second(self):
        """
        ideal case
        """
        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)
        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (2,))
        text_generator = NGramTextGenerator(profile)
        actual = text_generator._generate_word((2,), 4)
        expected = (2, 3, 1)
        self.assertEqual(actual, expected)

    def test_generate_one_word(self):
        """
        ideal case
        """
        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)
        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (2,))
        text_generator = NGramTextGenerator(profile)
        actual = text_generator._generate_word((2,), 1)
        expected = (2, 1)
        self.assertEqual(actual, expected)

    def test_one_letter(self):
        """
        no left context
        """
        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)
        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (2,))
        text_generator = NGramTextGenerator(profile)
        actual = text_generator._generate_letter((2,))
        expected = 3
        self.assertEqual(actual, expected)

    def test_no_left_context(self):
        """
        no left context
        """
        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)
        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (2,))
        text_generator = NGramTextGenerator(profile)
        actual = text_generator._generate_letter((100,))
        expected = 12
        self.assertEqual(actual, expected)

    def test_used_ngrams(self):
        """
        used ngrams
        """
        text = 'If you can'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)
        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (2,))
        text_generator = NGramTextGenerator(profile)
        text_generator._used_n_grams = [(1, 2), (2, 3), (3, 1), (1, 4), (4, 5), (5, 6), (6, 1), (1, 7), (7, 8), (8, 9),
                                        (9, 1)]
        actual = text_generator._generate_letter((2,))
        expected = 3
        self.assertEqual(actual, expected)

    def test_no_trie(self):
        """
        No trie
        """
        text = 'If you can meet with Triumph and Disaster And treat those two impostors just the same'.lower()
        tokenized = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized)
        encoded = encode_corpus(storage, tokenized)

        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded, (4,))
        text_generator = NGramTextGenerator(profile)
        actual = text_generator._generate_letter((100,))
        self.assertEqual(actual, -1)
