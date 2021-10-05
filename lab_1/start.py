"""
Language detection starter
"""

import os
import main

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH_TO_TEXTS_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, 'texts')
PATH_TO_PROFILES_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, 'profiles')

if __name__ == '__main__':

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'en.txt'), 'r', encoding='utf-8') as file_to_read:
        en_text = file_to_read.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'de.txt'), 'r', encoding='utf-8') as file_to_read:
        de_text = file_to_read.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'la.txt'), 'r', encoding='utf-8') as file_to_read:
        la_text = file_to_read.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'unknown.txt'), 'r', encoding='utf-8') as \
            file_to_read:
        unknown_text = file_to_read.read()

    EXPECTED = 'en'
    RESULT = ''
    TOP_N = 7
    unknown_profile = main.create_language_profile('unknown_text', unknown_text, [])

    # compare language detective results
    profile_en_10 = main.load_profile(os.path.join(PATH_TO_PROFILES_FOLDER, 'en.json'))
    profile_de_10 = main.load_profile(os.path.join(PATH_TO_PROFILES_FOLDER, 'de.json'))
    profile_la_10 = main.load_profile(os.path.join(PATH_TO_PROFILES_FOLDER, 'la.json'))
    profiles_10 = [profile_en_10, profile_de_10, profile_la_10]
    # we may save profiles in json file
    main.save_profile(unknown_profile)

    RESULT = main.detect_language_advanced(unknown_profile, profiles_10, [], TOP_N)

    # profile_en_8 = main.create_language_profile("en", en_text, [])
    # profile_de_8 = main.create_language_profile("de", de_text, [])
    # profile_la_8 = main.create_language_profile("la", la_text, [])
    # profiles_8 = [profile_en_8, profile_de_8, profile_la_8]
    # RESULT_8 = main.detect_language_advanced(unknown_profile, profiles_8, [], TOP_N)

    # if RESULT_10 == RESULT_8:
    # print("Great!", RESULT_10, "==", RESULT_8)
    # else:
    # print("Something is wrong!")

    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    # assert RESULT, 'Detection not working'
    assert EXPECTED == RESULT, 'Detection not working'
