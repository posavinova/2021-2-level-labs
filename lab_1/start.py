"""
Language detection starter
"""


if __name__ == '__main__':

    with open('texts/en.txt', 'r', encoding='utf-8') as file_to_read:
        en_text = file_to_read.read()

    with open('texts/de.txt', 'r', encoding='utf-8') as file_to_read:
        de_text = file_to_read.read()

    with open('texts/unknown.txt', 'r', encoding='utf-8') as file_to_read:
        unknown_text = file_to_read.read()

    EXPECTED = 'en'
    RESULT = ''
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Detection not working'
