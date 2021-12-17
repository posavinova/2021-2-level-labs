"""
Language generation starter
"""

import os
from lab_4.main import (
    tokenize_by_letters,
    LetterStorage,
    encode_corpus,
    LanguageProfile,
    NGramTextGenerator,
    LikelihoodBasedTextGenerator,
    BackOffGenerator,
    PublicLanguageProfile,
)

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    with open(
        os.path.join(PATH_TO_LAB_FOLDER, "reference_text.txt"), encoding="utf-8"
    ) as f:
        corpus = tokenize_by_letters(f.read())
    # score 4
    storage = LetterStorage()
    storage.update(corpus)
    print(len(storage.storage))
    print(list(storage.storage.items())[:5])
    print(list(storage.storage.items())[-5:])

    print("***")

    # score 6
    profile = LanguageProfile(storage, "ref")
    profile.create_from_tokens(
        encode_corpus(storage, corpus),
        (
            1,
            2,
        ),
    )
    generator = NGramTextGenerator(profile)
    for length in range(5, 11):
        print(generator.generate_decoded_sentence((1,), length))

    print("***")

    # score 8
    generator = LikelihoodBasedTextGenerator(profile)
    for length in range(5, 11):
        print(generator.generate_decoded_sentence((1,), length))

    print("***")

    # score 10
    # First public language
    profile_1 = PublicLanguageProfile(LetterStorage(), "fi")
    profile_1.open(os.path.join(PATH_TO_LAB_FOLDER, "fi"))

    generation_1 = []
    for generator in [
        NGramTextGenerator(profile_1),
        LikelihoodBasedTextGenerator(profile_1),
        BackOffGenerator(profile_1),
    ]:
        generation_1.append(
            generator.generate_decoded_sentence(
                (profile_1.storage.get_special_token_id(),), 5
            )
        )
    # print("\n".join(generation_1))

    # print("***")

    # Second public language
    profile_2 = PublicLanguageProfile(LetterStorage(), "ne")
    profile_2.open(os.path.join(PATH_TO_LAB_FOLDER, "ne"))

    generation_2 = []
    for generator in [
        NGramTextGenerator(profile_2),
        LikelihoodBasedTextGenerator(profile_2),
        BackOffGenerator(profile_2),
    ]:
        generation_2.append(
            generator.generate_decoded_sentence(
                (profile_2.storage.get_special_token_id(),), 5
            )
        )
    # print("\n".join(generation_2))
