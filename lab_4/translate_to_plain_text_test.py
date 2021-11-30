# pylint: skip-file
"""
Tests translate_to_plain_test function
"""

import unittest

from lab_4.language_profile import LanguageProfile
from lab_4.main import NGramTextGenerator, LetterStorage, tokenize_by_letters, decode_sentence, encode_corpus, translate_sentence_to_plain_text


class TranslateToPlainTextTest(unittest.TestCase):
    """
    check translate_to_plain_test function
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
        profile.create_from_tokens(encoded, (2,))
        text_generator = NGramTextGenerator(profile)
        generated_sentence = text_generator.generate_sentence((1,), 8)
        decoded = decode_sentence(storage, generated_sentence)
        actual = translate_sentence_to_plain_text(decoded)
        expected = 'I wish the loved fan acendumay hucs rallywam.'
        self.assertEqual(expected, actual)

    def test_incorrect_input(self):
        """
        incorrect input
        """
        bad_inputs = [[123], LanguageProfile, None, 'none', ()]
        for bad_input in bad_inputs:
            expected = ''

            actual = translate_sentence_to_plain_text(bad_input)
            self.assertEqual(expected, actual)

    def test_ideal_second(self):
        """
        ideal case
        """
        decoded = (('i', '_'),
                   ('_', 'w', 'i', 's', 'h', '_'),
                   ('_', 't', 'h', 'e', '_'),
                   ('_', 'l', 'o', 'v', 'e', 'd', '_'),
                   ('_', 'f', 'a', 'n', '_'),
                   ('_', 'a', 'c', 'e', 'n', 'd', 'u', 'm', 'a', 'y', '_'),
                   ('_', 'h', 'u', 'c', 'r', 'a', 'l', 'l', 'y', 't', '_'),
                   ('_', 's', '_'))
        actual = translate_sentence_to_plain_text(decoded)
        expected = 'I wish the loved fan acendumay hucrallyt s.'
        self.assertEqual(expected, actual)
