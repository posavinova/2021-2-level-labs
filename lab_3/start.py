"""
Language detection starter
"""

import os
from lab_3.main import LetterStorage, LanguageProfile, LanguageDetector
from lab_3.main import encode_corpus, tokenize_by_sentence, calculate_distance


PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    ENG_SAMPLE = """Helium is the byproduct of millennia of radioactive
    decay from the elements thorium and uranium."""
    GERMAN_SAMPLE = """Zwei Begriffe, die nicht unbedingt zueinander passen,
    am Arbeitsplatz schon mal gar nicht."""
    UNKNOWN_SAMPLE = "Helium is material."
    SECRET_SAMPLE = """ Некој е болен и тој не е слободен.
    Dлетува гол во дупка од мраз. 
    И пее, а плаче од болка. Дали е ова контраст, можеби – живот?"""

    tokenized_en = tokenize_by_sentence(ENG_SAMPLE)
    tokenized_de = tokenize_by_sentence(GERMAN_SAMPLE)
    tokenized_unk = tokenize_by_sentence(UNKNOWN_SAMPLE)

    storage = LetterStorage()
    storage.update(tokenized_en)
    storage.update(tokenized_de)
    storage.update(tokenized_unk)

    encoded_en = encode_corpus(storage, tokenized_en)
    encoded_de = encode_corpus(storage, tokenized_de)
    encoded_unk = encode_corpus(storage, tokenized_unk)

    # score 6, params: k = 5, trie_level = 2
    # predict UNKNOWN_SAMPLE

    en_profile_6 = LanguageProfile(storage, 'en')
    de_profile_6 = LanguageProfile(storage, 'de')
    unknown_profile_6 = LanguageProfile(storage, 'unk')

    en_profile_6.create_from_tokens(encoded_en, (5, 2))
    de_profile_6.create_from_tokens(encoded_de, (5, 2))
    unknown_profile_6.create_from_tokens(encoded_unk, (5, 2))

    en_distance_6 = calculate_distance(unknown_profile_6, en_profile_6, 5, 2)
    de_distance_6 = calculate_distance(unknown_profile_6, de_profile_6, 5, 2)
    RESULT_6 = en_distance_6, de_distance_6
    print(RESULT_6)
    EXPECTED_DISTANCE_TO_EN_DE_PROFILES = 17, 25

    # score 8, k = 5, trie_level = 3
    # predict UNKNOWN_SAMPLE

    en_profile_8 = LanguageProfile(storage, 'en')
    de_profile_8 = LanguageProfile(storage, 'de')
    unknown_profile_8 = LanguageProfile(storage, 'unk')

    en_profile_8.create_from_tokens(encoded_en, (5, 3))
    de_profile_8.create_from_tokens(encoded_de, (5, 3))
    unknown_profile_8.create_from_tokens(encoded_unk, (5, 3))

    calculate_distance(unknown_profile_8, en_profile_8, 5, 3)
    calculate_distance(unknown_profile_8, de_profile_8, 5, 3)

    unknown_profile_8.save('unknown_profile.json')
    profile_unk = LanguageProfile(storage, 'unk')
    profile_unk.open('unknown_profile.json')

    detector = LanguageDetector()

    detector.register_language(en_profile_8)
    detector.register_language(de_profile_8)

    RESULT_8 = detector.detect(profile_unk, 5, (3,))
    print(RESULT_8)
    EXPECTED_SCORE = {'en': 24, 'de': 25}

    # score 10, k = 1000, trie_levels = (2,)
    # predict SECRET_SAMPLE
    # print(detector.detect(unknown_profile, 1000, (2,)))
    # EXPECTED_LANGUAGE = ?
    # EXPECTED_MIN_DISTANCE = ?

    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT_6 == EXPECTED_DISTANCE_TO_EN_DE_PROFILES, 'Detection not working'
    assert RESULT_8 == EXPECTED_SCORE, 'Detection not working'
