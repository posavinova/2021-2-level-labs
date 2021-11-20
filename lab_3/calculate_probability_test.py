# pylint: skip-file
"""
Tests for calculate_probability func
"""

import unittest

from lab_3.main import LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    tokenize_by_sentence, \
    LanguageDetector, \
    calculate_probability


class CalculateProbabilityTest(unittest.TestCase):
    """
    Tests for calculate_probability func
    """

    def test_calculate_probability_ideal(self):
        """
        Calculate probability
        """

        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()
        text = tokenize_by_sentence(text)
        storage = LetterStorage()
        storage.update(text)

        text_de = 'Familie Müller plant ihren Urlaub ' \
                  'Sie geht in ein Reisebüro und lässt sich von einem ' \
                  'Angestellten beraten ' \
                  'Als Reiseziel wählt sie Mallorca aus ' \
                  'Familie Müller bucht einen Flug auf die Mittelmeerinsel'.lower()
        text_de = tokenize_by_sentence(text_de)
        storage.update(text_de)

        text_unk = 'I loved its silly face ' \
                   'I wish walks' \
                   'I wish I liked' \
                   'And one'.lower()
        text_unk = tokenize_by_sentence(text_unk)
        storage.update(text_unk)

        encoded_en = encode_corpus(storage, text)
        encoded_de = encode_corpus(storage, text_de)
        encoded_unk = encode_corpus(storage, text_unk)

        profile_en = LanguageProfile(storage, 'en')
        profile_en.create_from_tokens(encoded_en, (2, 3))

        profile_de = LanguageProfile(storage, 'de')
        profile_de.create_from_tokens(encoded_de, (2, 3))

        profile_unk = LanguageProfile(storage, 'unk')
        profile_unk.create_from_tokens(encoded_unk, (2, 3))

        self.assertAlmostEqual(calculate_probability(profile_unk, profile_en, 3, 2), -3.295342916871046, 5)
        self.assertAlmostEqual(calculate_probability(profile_unk, profile_de, 3, 2), -6.174827228410347, 5)
        self.assertAlmostEqual(calculate_probability(profile_unk, profile_en, 5, 2), -6.568706927023317, 5)
        self.assertAlmostEqual(calculate_probability(profile_unk, profile_de, 5, 2), -9.608814432895493, 5)

    def test_bad_input(self):
        """
        Tests with bad inputs
        """

        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()
        text = tokenize_by_sentence(text)
        storage = LetterStorage()
        storage.update(text)

        text_de = 'Familie Müller plant ihren Urlaub ' \
                  'Sie geht in ein Reisebüro und lässt sich von einem ' \
                  'Angestellten beraten ' \
                  'Als Reiseziel wählt sie Mallorca aus ' \
                  'Familie Müller bucht einen Flug auf die Mittelmeerinsel'.lower()
        text_de = tokenize_by_sentence(text_de)
        storage.update(text_de)

        text_unk = 'I loved its silly face ' \
                   'I wish walks' \
                   'I wish I liked' \
                   'And one'.lower()
        text_unk = tokenize_by_sentence(text_unk)
        storage.update(text_unk)

        encoded_en = encode_corpus(storage, text)
        encoded_de = encode_corpus(storage, text_de)
        encoded_unk = encode_corpus(storage, text_unk)

        profile_en = LanguageProfile(storage, 'en')
        profile_en.create_from_tokens(encoded_en, (2, 3))

        profile_de = LanguageProfile(storage, 'de')
        profile_de.create_from_tokens(encoded_de, (2, 3))

        profile_unk = LanguageProfile(storage, 'unk')
        profile_unk.create_from_tokens(encoded_unk, (2, 3))

        bad_inputs = [None, LanguageDetector, 'abc', []]
        for bad_input in bad_inputs:
            self.assertEqual(calculate_probability(bad_input, profile_en, 5, 2), -1)

        for bad_input in bad_inputs:
            self.assertEqual(calculate_probability(profile_unk, bad_input, 5, 2), -1)

        for bad_input in bad_inputs:
            self.assertEqual(calculate_probability(profile_unk, profile_en, bad_input, 2), -1)

        for bad_input in bad_inputs:
            self.assertEqual(calculate_probability(profile_unk, profile_en, 5, bad_input), -1)
