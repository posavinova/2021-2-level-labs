"""
Lab 1
Language detection
"""


import re
# import json
# from typing import Optional


def tokenize(text: str) -> list or None:
    """
    Splits a text into tokens, converts the tokens into lowercase,
    removes punctuation and other symbols from words
    :param text: a text
    :return: a list of lower-cased tokens without punctuation
    """
    if isinstance(text, str):
        return re.sub(r"[-\d,.!?'_@#№$:;\"\\]+", "", text).strip().lower().split()
    else:
        return None


def remove_stop_words(tokens: list, stop_words: list) -> list or None:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    """
    if isinstance(tokens, list):
        if isinstance(stop_words, list):
            return [tokens.remove(word) for word in tokens if word in stop_words]
        else:
            return tokens
    else:
        return None


def calculate_frequencies(tokens: list) -> dict or None:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """
    if isinstance(tokens, list):
        freq_dict = {}
        for word in tokens:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        return freq_dict
    else:
        return None


def get_top_n_words(freq_dict: dict, top_n: int) -> list or None:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words
    :return: a list of the most common words
    """
    if isinstance(freq_dict, dict) and isinstance(top_n, int):
        sorted_by_key = dict(sorted(freq_dict.items()))
        sorted_by_value = dict(sorted(sorted_by_key.items(), key=lambda kv: kv[1], reverse=True))
        tokens = list(sorted_by_value.keys())
        if top_n <= len(tokens):
            return tokens[:top_n]
        else:
            return tokens
    else:
        return None


def create_language_profile(language: str, text: str, stop_words: list) -> dict or None:
    """
    Creates a language profile
    :param language: a language
    :param text: a text
    :param stop_words: a list of stop words
    :return: a dictionary with three keys – name, freq, n_words
    """
    if isinstance(language, str) and isinstance(text, str) and isinstance(stop_words, list):
        tokenized = tokenize(text)
        cleared = remove_stop_words(tokenized, stop_words)
        freq_dict = calculate_frequencies(cleared)
        lang_profile = {"name": language, "freq": freq_dict, "n_words": len(freq_dict)}
        return lang_profile
    else:
        return None


def compare_profiles(unknown_profile: dict, profile_to_compare: dict, top_n: int) -> float or None:
    """
    Compares profiles and calculates the distance using top n words
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: the distance
    """
    if isinstance(profile_1, dict) and isinstance(profile_2, dict) and isinstance(top_n, int):
        top_1 = get_top_n_words(profile_1, top_n)
        top_2 = get_top_n_words(profile_2, top_n)
        intersection = []
        [intersection.append(word) for word in profile_1 if word in profile_2]
        return len(intersection) / top_n
    else:
        return None


def detect_language(unknown_profile: dict, profile_1: dict, profile_2: dict, top_n: int) -> str or None:
    """
    Detects the language of an unknown profile
    :param unknown_profile: a dictionary
    :param profile_1: a dictionary
    :param profile_2: a dictionary
    :param top_n: a number of the most common words
    :return: a language
    """
    if isinstance(unknown_profile, dict) and isinstance(profile_1, dict) and isinstance(profile_2, dict):
        match_1 = calculate_distance(profile_1, unknown_profile, top_n)
        match_2 = calculate_distance(profile_2, unknown_profile, top_n)
        if match_1 > match_2:
            return profile_1["name"]
        else:
            return profile_2["name"]
    else:
        return None


def compare_profiles_advanced(unknown_profile: dict, profile_to_compare: dict, top_n: int) -> list or None:
    """
    Compares profiles and calculates some advanced parameters
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: a dictionary with 7 keys – name, score, common, sorted_common, max_length_word,
    min_length_word, average_token_length
    """
    pass


def detect_language_advanced(unknown_profile: dict, profiles: list, languages: list, top_n: int) -> str or None:
    """
    Detects the language of an unknown profile within the list of possible languages
    :param unknown_profile: a dictionary
    :param profiles: a list of dictionaries
    :param languages: a list of possible languages
    :param top_n: a number of the most common words
    :return: a language
    """
    pass


def load_profile(path_to_file: str) -> dict or None:
    """
    Loads a language profile
    :param path_to_file: a path
    :return: a dictionary with three keys – name, freq, n_words
    """
    pass


def save_profile(profile: dict) -> int:
    """
    Saves a language profile
    :param profile: a dictionary
    :return: 0 if everything is ok, 1 if not
    """
    pass
