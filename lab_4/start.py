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

    # score 6
    profile = LanguageProfile(storage, "idk")
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

    # score 8
    generator = LikelihoodBasedTextGenerator(profile)
    for length in range(5, 11):
        print(generator.generate_decoded_sentence((1,), length))

    # score 10
    profile = PublicLanguageProfile(LetterStorage(), "ne")
    profile.open(os.path.join(PATH_TO_LAB_FOLDER, "ne"))

    generation = []
    for generator in [
        NGramTextGenerator(profile),
        LikelihoodBasedTextGenerator(profile),
        BackOffGenerator(profile),
    ]:
        generation.append(
            generator.generate_decoded_sentence(
                (profile.storage.get_special_token_id(),), 5
            )
        )
    print(" ".join(generation))

    RESULT = generation
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT == generation, "Detection not working"
