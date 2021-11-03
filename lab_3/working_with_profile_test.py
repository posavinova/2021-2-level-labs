# pylint: skip-file
"""
Work with real-life profile
"""

import os
import unittest

from lab_3.main import NGramTrie, \
    LetterStorage, \
    encode_corpus, \
    LanguageProfile, \
    tokenize_by_sentence, \
    calculate_distance, \
    LanguageDetector

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))


class WorkWithRealLifeProfileTest(unittest.TestCase):
    """
    Work with real-life profile
    """

    def test_ideal(self):
        """
        Work with real-life profile
        """

        text = '''I wish I loved the Human Race
I wish I loved its silly face
I wish I liked the way it walks
I wish I liked the way it talks
And when I am introduced to one
I wish I thought What Jolly Fun'''.lower()

        another_text = 'Кожна людина має право на ' \
                       'освіту Освіта повинна бути безплатною хоча ' \
                       'б початкова і загальна Початкова освіта ' \
                       'повинна бути обов язковою Технічна і ' \
                       'професійна освіта повинна бути загальнодоступною ' \
                       'а вища освіта повинна бути однаково доступною ' \
                       'для всіх на основі здібностей кожного Освіта ' \
                       'повинна бути спрямована на повний розвиток ' \
                       'людської особи і збільшення поваги до прав ' \
                       'людини і основних свобод Освіта повинна ' \
                       'сприяти взаєморозумінню терпимості і ' \
                       'дружбі між усіма народами расовими ' \
                       'або релігійними групами і повинна ' \
                       'сприяти діяльності Організації Обєднаних Націй ' \
                       'по підтриманню миру'.lower()

        text = tokenize_by_sentence(text)
        another_text = tokenize_by_sentence(another_text)
        storage = LetterStorage()
        storage.update(text)
        storage.update(another_text)
        encoded_text = encode_corpus(storage, text)
        encoded_another_text = encode_corpus(storage, another_text)

        profile_en = LanguageProfile(letter_storage=storage, language_name='en')
        profile_en.create_from_tokens(encoded_text, (2, 3, 4))

        profile_uk = LanguageProfile(letter_storage=storage, language_name='ukrainian')
        profile_uk.create_from_tokens(encoded_another_text, (2, 3, 4))

        loaded_profile = LanguageProfile(letter_storage=storage, language_name='unk')
        loaded_profile.open(os.path.join(PATH_TO_LAB_FOLDER, 'sample_profile.json'))

        dist_en_to_unk = calculate_distance(loaded_profile, profile_en, 3, 2)
        dist_uk_to_unk = calculate_distance(loaded_profile, profile_uk, 3, 2)

        self.assertGreater(dist_en_to_unk, dist_uk_to_unk)

        detector = LanguageDetector()
        detector.register_language(profile_en)
        detector.register_language(profile_uk)

        actual = detector.detect(loaded_profile, 3, (2,))
        self.assertGreater(actual['en'], actual['ukrainian'])
