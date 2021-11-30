"""
Lab 2
Language classification
"""
from math import sqrt, fabs
from lab_1.main import tokenize, remove_stop_words


# 4
def get_freq_dict(tokens: list) -> dict or None:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """
    if not (
            isinstance(tokens, list)
            and all(isinstance(t, str) for t in tokens)
    ):
        return None

    freq_dict = {}
    for token in tokens:
        if token not in freq_dict:
            freq_dict[token] = 1
        else:
            freq_dict[token] += 1
    for token in freq_dict:
        freq_dict[token] = round(freq_dict[token] / len(tokens), 5)
    return freq_dict


def get_language_profiles(texts_corpus: list, language_labels: list) -> dict or None:
    """
    Computes language profiles for a collection of texts
        and adds appropriate language label for each text
    :param texts_corpus: a list of given texts
    :param language_labels: a list of given language labels
    :return: a dictionary of dictionaries - language profiles
    """
    if not (
            isinstance(texts_corpus, list)
            and all(isinstance(i, list) for i in texts_corpus)
            and isinstance(language_labels, list)
            and all(isinstance(s, str) for s in language_labels)
    ):
        return None

    language_profiles = dict.fromkeys(language_labels)
    for i, lang in enumerate(language_profiles):
        language_profiles[lang] = get_freq_dict(texts_corpus[i])
    return language_profiles


def get_language_features(language_profiles: dict) -> list or None:
    """
    Gets all unique words from language profiles
        and sorts them in alphabetical order
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if not (
            isinstance(language_profiles, dict)
            and language_profiles
    ):
        return None

    unique_tokens = []
    for profile in language_profiles.values():
        for i in profile.keys():
            unique_tokens.append(i)
    features = list(set(unique_tokens))
    return sorted(features)


def get_text_vector(original_text: list, language_profiles: dict) -> list or None:
    """
    Builds a vector representation of a given text
        using dictionary with language profiles
    :param original_text: any tokenized text
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if not (
            isinstance(original_text, list)
            and all(isinstance(i, str) for i in original_text)
            and isinstance(language_profiles, dict)
            and language_profiles
    ):
        return None

    features = get_language_features(language_profiles)
    text_vector = []
    for i in features:
        if i not in original_text:
            text_vector.append(0)
        else:
            for profile in language_profiles.values():
                if i in profile.keys():
                    text_vector.append(profile[i])
    return text_vector


# 6
def calculate_distance(unknown_text_vector: list, known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using euclid metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vector: vector for known text
    """
    if not (
            isinstance(unknown_text_vector, list)
            and isinstance(known_text_vector, list)
            and all(isinstance(i, (int, float)) for i in unknown_text_vector)
            and all(isinstance(i, (int, float)) for i in known_text_vector)
    ):
        return None

    euclidean_distance = 0
    for index, vector in enumerate(unknown_text_vector):
        euclidean_distance += ((vector - known_text_vector[index]) ** 2)
    return round(sqrt(euclidean_distance), 5)


def predict_language_score(unknown_text_vector: list, known_text_vectors: list,
                           language_labels: list) -> [str, int] or None:
    """
    Predicts unknown text label and its distance to the closest known text
    :param unknown_text_vector: vector for unknown text
    :param known_text_vectors: a list of vectors for known texts
    :param language_labels: language labels for each known text
    """
    if not (
            isinstance(unknown_text_vector, list)
            and isinstance(known_text_vectors, list)
            and all(isinstance(i, (int, float)) for i in unknown_text_vector)
            and all(isinstance(i, list) for i in known_text_vectors)
            and isinstance(language_labels, list)
            and all(isinstance(i, str) for i in language_labels)
            and len(known_text_vectors) == len(language_labels)
    ):
        return None

    distances = []
    for i in known_text_vectors:
        distances.append(calculate_distance(unknown_text_vector, i))
    closest_distance = distances.index(min(distances))
    closest_label = language_labels[closest_distance]
    prediction = [closest_label, min(distances)]
    return prediction


# 8
def calculate_distance_manhattan(unknown_text_vector: list,
                                 known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using manhattan metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vector: vector for known text
    """
    if not (
            isinstance(unknown_text_vector, list)
            and isinstance(known_text_vector, list)
            and all(isinstance(i, (int, float)) for i in unknown_text_vector)
            and all(isinstance(i, (int, float)) for i in known_text_vector)
    ):
        return None

    manhattan_distance = 0
    for index, vector in enumerate(unknown_text_vector):
        manhattan_distance += fabs(vector - known_text_vector[index])
    return round(manhattan_distance, 5)


def predict_language_knn(unknown_text_vector: list, known_text_vectors: list,
                         language_labels: list, k=1, metric='manhattan') -> [str, int] or None:
    """
    Predicts unknown text label and its distance to the closest known text
        using knn based algorithm and specific metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vectors: a list of vectors for known texts
    :param language_labels: language labels for each known text
    :param k: the number of neighbors to choose label from
    :param metric: specific metric to use while calculating distance
    """
    if not (
            isinstance(unknown_text_vector, list)
            and isinstance(known_text_vectors, list)
            and all(isinstance(i, (int, float)) for i in unknown_text_vector)
            and all(isinstance(i, list) for i in known_text_vectors)
            and isinstance(language_labels, list)
            and all(isinstance(i, str) for i in language_labels)
            and len(known_text_vectors) == len(language_labels)
            and isinstance(k, int)
    ):
        return None

    distances = []
    if metric == 'euclid':
        for i in known_text_vectors:
            distances.append(calculate_distance(unknown_text_vector, i))
    else:
        for i in known_text_vectors:
            distances.append(calculate_distance_manhattan(unknown_text_vector, i))

    knn_distances = sorted(distances)[:k]
    closest_languages = []
    for i in knn_distances:
        ind = distances.index(i)
        label = language_labels[ind]
        closest_languages.append(label)

    predict_label = {}
    for language in closest_languages:
        if language not in predict_label:
            predict_label[language] = 1
        else:
            predict_label[language] += 1
    predict_language = max(predict_label, key=predict_label.get)
    prediction = [predict_language, min(distances)]
    return prediction


# 10 implementation
def get_sparse_vector(original_text: list, language_profiles: dict) -> list or None:
    """
    Builds a sparse vector representation of a given text
        using dictionary with language profiles
    :param original_text: any tokenized text
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if not (
            isinstance(original_text, list)
            and all(isinstance(i, str) for i in original_text)
            and isinstance(language_profiles, dict)
            and language_profiles
    ):
        return None

    features = get_language_features(language_profiles)
    sparse_vector = []

    vector = dict.fromkeys(features, 0)
    for language_profile in language_profiles.values():
        for word, freq in language_profile.items():
            vector[word] = freq
    for index, feature in enumerate(features):
        if feature in original_text:
            sparse_vector.append([index, vector[feature]])
    return sparse_vector


def calculate_distance_sparse(unknown_text_vector: list,
                              known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using euclid metric
    :param unknown_text_vector: sparse vector for unknown text
    :param known_text_vector: sparse vector for known text
    """
    if not (
            isinstance(unknown_text_vector, list)
            and isinstance(known_text_vector, list)
            and all(isinstance(i, list) for i in unknown_text_vector)
            and all(isinstance(i, list) for i in known_text_vector)
    ):
        return None

    unknown_text_dict = dict(unknown_text_vector)
    known_text_dict = dict(known_text_vector)
    mixed_dict = {**unknown_text_dict, **known_text_dict}

    for key, value in unknown_text_dict.items():
        if key in known_text_dict:
            mixed_dict[key] = value - known_text_dict[key]
    euclidean_distance = 0
    for value in mixed_dict.values():
        euclidean_distance += value ** 2
    return round(sqrt(euclidean_distance), 5)


def predict_language_knn_sparse(unknown_text_vector: list, known_text_vectors: list,
                                language_labels: list, k=1) -> [str, int] or None:
    """
    Predicts unknown text label and its distance to the closest known text
        using knn based algorithm
    :param unknown_text_vector: sparse vector for unknown text
    :param known_text_vectors: a list of sparse vectors for known texts
    :param language_labels: language labels for each known text
    :param k: the number of neighbors to choose label from
    """
    if not (
            isinstance(unknown_text_vector, list)
            and isinstance(known_text_vectors, list)
            and all(isinstance(i, list) for i in unknown_text_vector)
            and all(isinstance(i, list) for i in known_text_vectors)
            and isinstance(language_labels, list)
            and all(isinstance(i, str) for i in language_labels)
            and len(known_text_vectors) == len(language_labels)
            and isinstance(k, int)
    ):
        return None

    distances = []
    for i in known_text_vectors:
        distances.append(calculate_distance_sparse(unknown_text_vector, i))

    knn_distances_sparse = sorted(distances)[:k]
    closest_languages = []
    for i in knn_distances_sparse:
        ind = distances.index(i)
        label = language_labels[ind]
        closest_languages.append(label)

    predict_label = {}
    for language in closest_languages:
        if language not in predict_label:
            predict_label[language] = 1
        else:
            predict_label[language] += 1
    predict_language = max(predict_label, key=predict_label.get)
    prediction = [predict_language, min(distances)]
    return prediction
