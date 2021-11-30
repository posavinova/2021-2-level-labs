"""
Language detection starter
"""

import os
from lab_2.main import (tokenize, remove_stop_words,
                        get_language_profiles, get_sparse_vector,
                        predict_language_knn_sparse)

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH_TO_PROFILES_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, 'profiles')
PATH_TO_DATASET_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, 'dataset')

if __name__ == '__main__':
    with open(os.path.join(PATH_TO_PROFILES_FOLDER, 'eng.txt'),
              'r', encoding='utf-8') as file_to_read:
        EN_TEXT = file_to_read.read()

    with open(os.path.join(PATH_TO_PROFILES_FOLDER, 'de.txt'),
              'r', encoding='utf-8') as file_to_read:
        DE_TEXT = file_to_read.read()

    with open(os.path.join(PATH_TO_PROFILES_FOLDER, 'lat.txt'),
              'r', encoding='utf-8') as file_to_read:
        LAT_TEXT = file_to_read.read()

    with open(os.path.join(PATH_TO_DATASET_FOLDER, 'known_samples_de.txt'),
              'r', encoding='utf-8') as file_to_read:
        DE_SAMPLES = file_to_read.read().split('[TEXT]')[1:]

    with open(os.path.join(PATH_TO_DATASET_FOLDER, 'known_samples_eng.txt'),
              'r', encoding='utf-8') as file_to_read:
        EN_SAMPLES = file_to_read.read().split('[TEXT]')[1:]

    with open(os.path.join(PATH_TO_DATASET_FOLDER, 'known_samples_lat.txt'),
              'r', encoding='utf-8') as file_to_read:
        LAT_SAMPLES = file_to_read.read().split('[TEXT]')[1:]

    with open(os.path.join(PATH_TO_DATASET_FOLDER, 'unknown_samples.txt'),
              'r', encoding='utf-8') as file_to_read:
        UNKNOWN_SAMPLES = file_to_read.read().split('[TEXT]')[1:]

    EXPECTED = ['de', 'eng', 'lat']
    stop_words = []
    corpus = []
    language_labels = []
    for text in DE_SAMPLES:
        corpus.append(remove_stop_words(tokenize(text), stop_words))
        language_labels.append('de')
    for text in EN_SAMPLES:
        corpus.append(remove_stop_words(tokenize(text), stop_words))
        language_labels.append('eng')
    for text in LAT_SAMPLES:
        corpus.append(remove_stop_words(tokenize(text), stop_words))
        language_labels.append('lat')
    language_profiles = get_language_profiles(corpus, language_labels)
    known_text_vectors = []
    for text in corpus:
        known_text_vectors.append(get_sparse_vector(text, language_profiles))
    k = 3
    RESULT = []
    for text in UNKNOWN_SAMPLES:
        unknown_text = remove_stop_words(tokenize(text), stop_words)
        unknown_text_vector = get_sparse_vector(unknown_text, language_profiles)
        predicted_lang = predict_language_knn_sparse(unknown_text_vector, known_text_vectors,
                                                     language_labels, k)
        RESULT.append(predicted_lang[0])
    print(f"{RESULT} are possible languages")
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT == EXPECTED, 'Detection not working'
