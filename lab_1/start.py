"""
Language detection starter
"""

import os
import main

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH_TO_TEXTS_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, "texts")

if __name__ == "__main__":

    with open(
        os.path.join(PATH_TO_TEXTS_FOLDER, "en.txt"), "r", encoding="utf-8"
    ) as file_to_read:
        en_text = file_to_read.read()

    with open(
        os.path.join(PATH_TO_TEXTS_FOLDER, "de.txt"), "r", encoding="utf-8"
    ) as file_to_read:
        de_text = file_to_read.read()

    with open(
        os.path.join(PATH_TO_TEXTS_FOLDER, "la.txt"), "r", encoding="utf-8"
    ) as file_to_read:
        la_text = file_to_read.read()

    with open(
        os.path.join(PATH_TO_TEXTS_FOLDER, "unknown.txt"), "r", encoding="utf-8"
    ) as file_to_read:
        unknown_text = file_to_read.read()

    unk_profile_test = main.create_language_profile("unk", unknown_text, [])
    main.save_profile(unk_profile_test)
    en_profile_test = main.create_language_profile("en", en_text, ["a", "an", "the"])
    de_profile_test = main.create_language_profile("de", de_text, [])
    la_profile_test = main.create_language_profile("la", la_text, [])

    detection_from_scratch = main.detect_language_advanced(
        unk_profile_test, [de_profile_test, la_profile_test], ["la", "de"], 10
    )

    de_profile = main.load_profile(
        "/home/polina/PycharmProjects/2021-2-level-labs/lab_1/profiles/de.json"
    )
    en_profile = main.load_profile(
        "/home/polina/PycharmProjects/2021-2-level-labs/lab_1/profiles/en.json"
    )
    la_profile = main.load_profile(
        "/home/polina/PycharmProjects/2021-2-level-labs/lab_1/profiles/la.json"
    )

    detection_from_profiles = main.detect_language_advanced(
        unk_profile_test, [de_profile, en_profile, la_profile], ["la", "de"], 10
    )

    print(
        f"1. Detecting language from scratch: it is most likely to be {detection_from_scratch}."
    )
    print(
        f"2. Detecting language from profiles: it is likely to be {detection_from_profiles}."
    )

    EXPECTED = "en"
    RESULT = detection_from_profiles
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, "Detection not working"
