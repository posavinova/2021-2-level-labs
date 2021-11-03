# pylint: skip-file
"""
Tests for distance calculation
"""

import unittest

from lab_3.main import LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    calculate_distance, \
    tokenize_by_sentence


class CalculateDistanceNGramsTest(unittest.TestCase):
    """
    Tests for distance calculation
    """

    def test_calculate_distance_ideal(self):
        """
        Calculate distance ideal test
        """
        eng = "Helium is the byproduct of millennia of " \
              "radioactive decay from the elements thorium and uranium".lower()
        unk = "The helium is mostly trapped in subterranean " \
              "natural gas bunkers and commercially extracted " \
              "through a method known as fractional distillation " \
              "The loss of helium on Earth would affect society greatly".lower()

        tokenized_eng = tokenize_by_sentence(eng)
        tokenized_unk = tokenize_by_sentence(unk)

        storage_eng = LetterStorage()
        storage_eng.update(tokenized_eng)
        encoded_eng = encode_corpus(storage_eng, tokenized_eng)

        storage_unk = LetterStorage()
        storage_unk.update(tokenized_unk)
        encoded_unk = encode_corpus(storage_unk, tokenized_unk)

        profile_eng = LanguageProfile(letter_storage=storage_eng, language_name='en')
        profile_unk = LanguageProfile(letter_storage=storage_unk, language_name='en')

        profile_eng.create_from_tokens(encoded_eng, (3,))
        profile_unk.create_from_tokens(encoded_unk, (3,))

        distance_eng_unk = calculate_distance(profile_unk, profile_eng, 5, 3)

        self.assertEqual(distance_eng_unk, 25)
