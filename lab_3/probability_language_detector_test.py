# pylint: skip-file
"""
Tests for Probability Language Detector
"""

import unittest

from lab_3.main import LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    tokenize_by_sentence, \
    ProbabilityLanguageDetector


class ProbabilityLanguageDetectorTest(unittest.TestCase):
    """
    Tests for Probability Language Detector
    """

    def test_detect_language_ideal(self):
        """
        Detect language
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
        profile_en.create_from_tokens(encoded_en, (1, 2, 3))

        profile_de = LanguageProfile(storage, 'de')
        profile_de.create_from_tokens(encoded_de, (1, 2, 3))

        profile_unk = LanguageProfile(storage, 'unk')
        profile_unk.create_from_tokens(encoded_unk, (1, 2, 3))

        detector = ProbabilityLanguageDetector()
        self.assertEqual(detector.language_profiles, {})
        self.assertEqual(detector.register_language(profile_en), 0)
        detector.register_language(profile_de)

        actual_bi_grams = detector.detect(profile_unk, 5, (2,))
        self.assertEqual(len(actual_bi_grams), 2)
        self.assertAlmostEqual(actual_bi_grams[('en', 2)], -6.568706927023317, 5)
        self.assertAlmostEqual(actual_bi_grams[('de', 2)], -9.608814432895493, 5)

        actual_three_grams = detector.detect(profile_unk, 5, (3,))
        self.assertEqual(len(actual_three_grams), 2)
        self.assertAlmostEqual(actual_three_grams[('en', 3)], -1.0033021088637848, 5)
        self.assertAlmostEqual(actual_three_grams[('de', 3)], 0.0, 5)

        actual_three_grams_less_k = detector.detect(profile_unk, 3, (3,))
        self.assertEqual(len(actual_three_grams_less_k), 2)
        self.assertAlmostEqual(actual_three_grams_less_k[('en', 3)], -1.0033021088637848, 5)
        self.assertAlmostEqual(actual_three_grams_less_k[('de', 3)], 0.0, 5)

        actual_multi = detector.detect(profile_unk, 4, (1, 2, 3))
        self.assertEqual(len(actual_multi), 6)
        self.assertAlmostEqual(actual_multi[('en', 1)], -9.674308785927618, 5)
        self.assertAlmostEqual(actual_multi[('de', 1)], -9.392476840786713, 5)

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

        encoded_en = encode_corpus(storage, text)

        profile_en = LanguageProfile(storage, 'en')
        profile_en.create_from_tokens(encoded_en, (2, 3))

        detector = ProbabilityLanguageDetector()
        bad_inputs = [None, LetterStorage, 'abc', []]

        detector.register_language(profile_en)

        for bad_input in bad_inputs:
            self.assertEqual(detector.detect(bad_input, 5, (3,)), -1)

        for bad_input in bad_inputs:
            self.assertEqual(detector.detect(profile_en, bad_input, (3,)), -1)

        for bad_input in bad_inputs:
            self.assertEqual(detector.detect(profile_en, 5, bad_input), -1)
