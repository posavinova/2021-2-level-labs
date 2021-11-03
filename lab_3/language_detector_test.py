# pylint: skip-file
"""
Tests for Language Detector
"""

import unittest

from lab_3.main import LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    tokenize_by_sentence, \
    LanguageDetector


class LanguageDetectorTest(unittest.TestCase):
    """
    Tests for Language Detector
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
        profile_en.create_from_tokens(encoded_en, (2, 3))

        profile_de = LanguageProfile(storage, 'de')
        profile_de.create_from_tokens(encoded_de, (2, 3))

        profile_unk = LanguageProfile(storage, 'unk')
        profile_unk.create_from_tokens(encoded_unk, (2, 3))

        detector = LanguageDetector()
        self.assertEqual(detector.language_profiles, {})
        self.assertEqual(detector.register_language(profile_en), 0)
        self.assertEqual(detector.register_language(profile_en), 0)
        self.assertEqual(len(detector.language_profiles), 1)
        detector.register_language(profile_de)

        actual_bi_grams = detector.detect(profile_unk, 5, (2,))
        self.assertEqual(len(actual_bi_grams), 2)
        self.assertEqual(actual_bi_grams['en'], 10)
        self.assertEqual(actual_bi_grams['de'], 25)

        actual_three_grams = detector.detect(profile_unk, 5, (3,))
        self.assertEqual(len(actual_three_grams), 2)
        self.assertEqual(actual_three_grams['en'], 0)
        self.assertEqual(actual_three_grams['de'], 25)

        actual_three_grams_less_k = detector.detect(profile_unk, 3, (3,))
        self.assertEqual(len(actual_three_grams_less_k), 2)
        self.assertEqual(actual_three_grams_less_k['en'], 0)
        self.assertEqual(actual_three_grams_less_k['de'], 9)

    def test_language_detector_bad_input(self):
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

        detector = LanguageDetector()
        bad_inputs = [None, LanguageDetector, 'abc', []]
        for bad_input in bad_inputs:
            self.assertEqual(detector.register_language(bad_input), 1)
            self.assertEqual(detector.language_profiles, {})

        detector.register_language(profile_en)
        self.assertEqual(detector.language_profiles, {'en': profile_en})

        for bad_input in bad_inputs:
            self.assertEqual(detector.detect(bad_input, 5, (3,)), -1)

        for bad_input in bad_inputs:
            self.assertEqual(detector.detect(profile_en, bad_input, (3,)), -1)

        for bad_input in bad_inputs:
            self.assertEqual(detector.detect(profile_en, 5, bad_input), -1)
