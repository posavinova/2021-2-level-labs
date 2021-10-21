"""
Lab 2
Language classification
"""
from math import sqrt


# 4
def get_freq_dict(tokens: list) -> dict or None:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """
    if not isinstance(tokens, list) or not all(isinstance(i, str) for i in tokens):
        return None
    freq_dict = {}
    for token in tokens:
        if token not in freq_dict:
            freq_dict[token] = round(tokens.count(token) / len(tokens), 5)
    return freq_dict


def get_language_profiles(texts_corpus: list, language_labels: list) -> dict or None:
    """
    Computes language profiles for a collection of texts
        and adds appropriate language label for each text
    :param texts_corpus: a list of given texts
    :param language_labels: a list of given language labels
    :return: a dictionary of dictionaries - language profiles
    """
    if (not isinstance(texts_corpus, list)
            or not isinstance(language_labels, list)
            or not all(isinstance(i, list) for i in texts_corpus)
            or not all(isinstance(i, str) for i in language_labels)):
        return None
    lang_profiles = {}
    for label in language_labels:
        if label not in lang_profiles:
            lang_profiles[label] = get_freq_dict(texts_corpus[language_labels.index(label)])
    return lang_profiles


def get_language_features(language_profiles: dict) -> list or None:
    """
    Gets all unique words from language profiles
        and sorts them in alphabetical order
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if (not isinstance(language_profiles, dict)
            or not language_profiles
            or not all(isinstance(i, str) for i in language_profiles.keys())
            or not all(isinstance(i, dict) for i in language_profiles.values())):
        return None
    features = []
    for profile in language_profiles.values():
        for word in profile:
            features.append(word)
    features = sorted(features)
    return features


def get_text_vector(original_text: list, language_profiles: dict) -> list or None:
    """
    Builds a vector representation of a given text
        using dictionary with language profiles
    :param original_text: any tokenized text
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if (not isinstance(original_text, list)
            or not isinstance(language_profiles, dict)
            or not language_profiles
            or not all(isinstance(i, str) for i in language_profiles)
            or not all(isinstance(i, dict) for i in language_profiles.values())):
        return None
    text_features = get_language_features(language_profiles)
    text_vector = []
    for token in text_features:
        if token in original_text:
            frequencies = [freq_dict[token]
                           for freq_dict in language_profiles.values()
                           if token in freq_dict.keys()]
            text_vector.append(max(frequencies))
        else:
            text_vector.append(0)
    return text_vector


# 6
def calculate_distance(unknown_text_vector: list, known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using euclid metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vector: vector for known text
    """
    if (not isinstance(unknown_text_vector, list)
            or not isinstance(known_text_vector, list)
            or not all(isinstance(i, (int, float)) for i in unknown_text_vector)
            or not all(isinstance(i, (int, float)) for i in known_text_vector)):
        return None
    distance = round(float(sqrt(sum(pow(a - b, 2) for a, b
                                    in zip(unknown_text_vector, known_text_vector)))), 5)
    return distance


def predict_language_score(unknown_text_vector: list, known_text_vectors: list,
                           language_labels: list) -> [str, int] or None:
    """
    Predicts unknown text label and its distance to the closest known text
    :param unknown_text_vector: vector for unknown text
    :param known_text_vectors: a list of vectors for known texts
    :param language_labels: language labels for each known text
    """
    if (not isinstance(unknown_text_vector, list)
            or not isinstance(known_text_vectors, list)
            or not isinstance(language_labels, list)
            or len(known_text_vectors) != len(language_labels)):
        return None
    if (not all(isinstance(i, str) for i in language_labels)
            or not all(isinstance(i, list) for i in known_text_vectors)
            or not all(isinstance(i, (int, float)) for i in unknown_text_vector)):
        return None
    distances = [calculate_distance(unknown_text_vector, vector) for vector in known_text_vectors]
    prediction = list(min(zip(language_labels, distances), key=lambda x: x[1]))
    return prediction


# 8
def calculate_distance_manhattan(unknown_text_vector: list,
                                 known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using manhattan metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vector: vector for known text
    """
    if (not isinstance(unknown_text_vector, list)
            or not isinstance(known_text_vector, list)
            or not all(isinstance(i, (int, float)) for i in unknown_text_vector)
            or not all(isinstance(i, (int, float)) for i in known_text_vector)):
        return None
    distance = round(float(sum(abs(a - b) for a, b
                               in zip(unknown_text_vector, known_text_vector))), 5)
    return distance


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
    if (not isinstance(unknown_text_vector, list)
            or not isinstance(known_text_vectors, list)
            or not isinstance(language_labels, list)
            or not isinstance(k, int)
            or not all(isinstance(i, (int, float)) for i in unknown_text_vector)):
        return None
    if (metric not in ("manhattan", "euclid")
            or len(known_text_vectors) != len(language_labels)):
        return None
    distances = [calculate_distance_manhattan(unknown_text_vector, vector) if metric == "manhattan"
                 else calculate_distance(unknown_text_vector, vector)
                 for vector in known_text_vectors]
    knn = sorted(zip(language_labels, distances), key=lambda x: x[1])[:k]
    lang_freq = {}
    for lang in knn:
        if lang[0] not in lang_freq:
            lang_freq[lang[0]] = 0
        else:
            lang_freq[lang[0]] += 1
    prediction = [max(lang_freq, key=lang_freq.get), min(distances)]
    return prediction


# 10 implementation
def get_sparse_vector(original_text: list, language_profiles: dict) -> list or None:
    """
    Builds a sparse vector representation of a given text
        using dictionary with language profiles
    :param original_text: any tokenized text
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if (not isinstance(original_text, list)
            or not isinstance(language_profiles, dict)
            or not language_profiles
            or not all(isinstance(i, str) for i in language_profiles)
            or not all(isinstance(i, dict) for i in language_profiles.values())):
        return None
    text_features = get_language_features(language_profiles)
    text_vector = []
    for token in text_features:
        if token in original_text:
            frequencies = [freq_dict[token] for freq_dict
                           in language_profiles.values() if token in freq_dict.keys()]
            text_vector.append(max(frequencies))
        else:
            text_vector.append(0)
    sparse_vector = [[index, value] for index, value in enumerate(text_vector) if value != 0]
    return sparse_vector


def calculate_distance_sparse(unknown_text_vector: list,
                              known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using euclid metric
    :param unknown_text_vector: sparse vector for unknown text
    :param known_text_vector: sparse vector for known text
    """
    if (not isinstance(unknown_text_vector, list)
            or not isinstance(known_text_vector, list)
            or not all(isinstance(i, list) for i in unknown_text_vector)
            or not all(isinstance(i, list) for i in known_text_vector)):
        return None
    unk_dict = dict(unknown_text_vector)
    k_dict = dict(known_text_vector)
    merged = unk_dict
    for key, value in k_dict.items():
        if key not in merged:
            merged[key] = value
        else:
            merged[key] = merged[key] - k_dict[key]
    distance = 0
    for value in merged.values():
        distance += pow(value, 2)
    distance = round(sqrt(distance), 5)
    return distance


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
    if (not isinstance(unknown_text_vector, list)
            or not isinstance(known_text_vectors, list)
            or not isinstance(language_labels, list)
            or not isinstance(k, int)
            or not all(isinstance(i, list) for i in unknown_text_vector)):
        return None
    if len(known_text_vectors) != len(language_labels):
        return None
    distances = [calculate_distance_sparse(unknown_text_vector, vector)
                 for vector in known_text_vectors]
    knn = sorted(zip(language_labels, distances), key=lambda x: x[1])[:k]
    lang_freq = {}
    for lang in knn:
        if lang[0] not in lang_freq:
            lang_freq[lang[0]] = 0
        else:
            lang_freq[lang[0]] += 1
    prediction = [max(lang_freq, key=lang_freq.get), min(distances)]
    return prediction
