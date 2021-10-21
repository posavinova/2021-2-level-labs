"""
Language detection starter
"""
import os
from lab_1.main import tokenize, remove_stop_words
from lab_2.main import get_language_profiles, get_sparse_vector, predict_language_knn_sparse

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

    RESULT = []
    stop_words = []
    corpus = []
    labels = []
    k = 3

    for text in DE_SAMPLES:
        corpus.append(remove_stop_words(tokenize(text), stop_words))
        labels.append('de')
    for text in EN_SAMPLES:
        corpus.append(remove_stop_words(tokenize(text), stop_words))
        labels.append('eng')
    for text in LAT_SAMPLES:
        corpus.append(remove_stop_words(tokenize(text), stop_words))
        labels.append('lat')

    profiles = get_language_profiles(corpus, labels)
    known_text_vectors = [get_sparse_vector(text, profiles) for text in corpus]
    for text in UNKNOWN_SAMPLES:
        unknown_text = remove_stop_words(tokenize(text), stop_words)
        unknown_text_vector = get_sparse_vector(unknown_text, profiles)
        prediction_knn_sparse = predict_language_knn_sparse(unknown_text_vector,
                                                            known_text_vectors,
                                                            labels, k)
        RESULT.append(prediction_knn_sparse[0])
    EXPECTED = ['de', 'eng', 'lat']
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert EXPECTED == RESULT, 'Detection not working'
