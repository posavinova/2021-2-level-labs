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


class CalculateDistanceTest(unittest.TestCase):
    """
    Tests for distance calculation
    """

    def test_calculate_distance_ideal(self):
        """
        Calculate distance ideal test
        """
        eng = "Helium is the byproduct of millennia of radioactive decay from the elements thorium and uranium"
        de = "Zwei Begriffe die nicht unbedingt zueinander passen am Arbeitsplatz schon mal gar nicht"
        unk = "Helium is material"

        tokenized_eng = tokenize_by_sentence(eng)
        tokenized_de = tokenize_by_sentence(de)
        tokenized_unk = tokenize_by_sentence(unk)

        storage = LetterStorage()
        storage.update(tokenized_eng)
        storage.update(tokenized_de)
        storage.update(tokenized_unk)

        encoded_eng = encode_corpus(storage, tokenized_eng)
        encoded_de = encode_corpus(storage, tokenized_de)
        encoded_unk = encode_corpus(storage, tokenized_unk)

        profile_eng = LanguageProfile(letter_storage=storage, language_name='en')
        profile_de = LanguageProfile(letter_storage=storage, language_name='en')
        profile_unk = LanguageProfile(letter_storage=storage, language_name='en')

        profile_eng.create_from_tokens(encoded_eng, (2,))
        profile_de.create_from_tokens(encoded_de, (2,))
        profile_unk.create_from_tokens(encoded_unk, (2,))

        distance_eng_unk = calculate_distance(profile_unk, profile_eng, 5, 2)
        distance_de_unk = calculate_distance(profile_unk, profile_de, 5, 2)

        self.assertEqual(distance_eng_unk, 17)
        self.assertEqual(distance_de_unk, 25)

    def test_calculate_distance_bad_inputs(self):
        """
        Tests with bad inputs
        """

        eng = "Helium is the byproduct of millennia of radioactive decay from the elements thorium and uranium."
        de = "Zwei Begriffe, die nicht unbedingt zueinander passen, am Arbeitsplatz schon mal gar nicht."
        unk = "Helium is material."

        tokenized_eng = tokenize_by_sentence(eng)
        tokenized_de = tokenize_by_sentence(de)
        tokenized_unk = tokenize_by_sentence(unk)

        storage_eng = LetterStorage()
        storage_eng.update(tokenized_eng)

        storage_de = LetterStorage()
        storage_de.update(tokenized_de)

        storage_unk = LetterStorage()
        storage_unk.update(tokenized_unk)

        profile_eng = LanguageProfile(letter_storage=storage_eng, language_name='en')
        profile_unk = LanguageProfile(letter_storage=storage_unk, language_name='en')

        bad_inputs = [{}, None, LetterStorage, 'abc']
        for bad_input in bad_inputs:
            actual = calculate_distance(bad_input, profile_eng, 5, 2)
            self.assertEqual(actual, -1)

        for bad_input in bad_inputs:
            actual = calculate_distance(profile_unk, bad_input, 5, 2)
            self.assertEqual(actual, -1)

        for bad_input in bad_inputs:
            actual = calculate_distance(profile_unk, profile_eng, bad_input, 2)
            self.assertEqual(actual, -1)

        for bad_input in bad_inputs:
            actual = calculate_distance(profile_unk, profile_eng, 5, bad_input)
            self.assertEqual(actual, -1)
