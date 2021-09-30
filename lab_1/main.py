"""
Lab 1
Language detection
"""

import json

from os.path import exists
from typing import Optional


def tokenize(text: str) -> Optional[list]:
    """
    Splits a text into tokens, converts the tokens into lowercase,
    removes punctuation and other symbols from words
    :param text: a text
    :return: a list of lower-cased tokens without punctuation
    """
    if not isinstance(text, str):
        return None
    tokenized = (
        "".join([char for char in text if char.isalpha() or char.isspace()])
        .lower()
        .split()
    )
    return tokenized


def remove_stop_words(tokens: list, stop_words: list) -> Optional[list]:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    """
    if (not isinstance(tokens, list)
            or not isinstance(stop_words, list)
            or not all(isinstance(i, str) for i in tokens)):
        return None
    cleaned = [word for word in tokens if word not in stop_words]
    return cleaned


def calculate_frequencies(tokens: list) -> Optional[dict]:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """
    if not isinstance(tokens, list):
        return None
    freq_dict = {}
    for token in tokens:
        if not isinstance(token, str):
            return None
        if token not in freq_dict:
            freq_dict[token] = 1
        else:
            freq_dict[token] += 1
    return freq_dict


def get_top_n_words(freq_dict: dict, top_n: int) -> Optional[list]:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words
    :return: a list of the most common words
    """
    if not isinstance(freq_dict, dict) or not isinstance(top_n, int):
        return None
    sorted_dict = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    tokens = [word for word, count in sorted_dict][:top_n]
    return tokens


def create_language_profile(
        language: str, text: str, stop_words: list
) -> Optional[dict]:
    """
    Creates a language profile
    :param language: a language
    :param text: a text
    :param stop_words: a list of stop words
    :return: a dictionary with three keys – name, freq, n_words
    """
    if (not isinstance(language, str)
            or not isinstance(text, str)
            or not isinstance(stop_words, list)):
        return None
    tokenized = tokenize(text)
    cleared = remove_stop_words(tokenized, stop_words)
    freq_dict = calculate_frequencies(cleared)
    lang_profile = {"name": language, "freq": freq_dict, "n_words": len(freq_dict)}
    return lang_profile


def compare_profiles(
        unknown_profile: dict, profile_to_compare: dict, top_n: int
) -> Optional[float]:
    """
    Compares profiles and calculates the distance using top n words
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: the distance
    """
    if (not isinstance(unknown_profile, dict)
            or not isinstance(profile_to_compare, dict)
            or not isinstance(top_n, int)):
        return None
    unk_top = get_top_n_words(unknown_profile["freq"], top_n)
    check_top = get_top_n_words(profile_to_compare["freq"], top_n)
    common = set(unk_top).intersection(set(check_top))
    score = round(len(common) / len(check_top), 2)
    return score


def detect_language(
        unknown_profile: dict, profile_1: dict, profile_2: dict, top_n: int
) -> Optional[str]:
    """
    Detects the language of an unknown profile
    :param unknown_profile: a dictionary
    :param profile_1: a dictionary
    :param profile_2: a dictionary
    :param top_n: a number of the most common words
    :return: a language
    """
    if (not isinstance(unknown_profile, dict)
            or not isinstance(profile_1, dict)
            or not isinstance(profile_2, dict)):
        return None
    match_one = compare_profiles(profile_1, unknown_profile, top_n)
    match_two = compare_profiles(profile_2, unknown_profile, top_n)
    if match_one > match_two:
        match = profile_1["name"]
        return match
    match = profile_2["name"]
    return match


def compare_profiles_advanced(
        unknown_profile: dict, profile_to_compare: dict, top_n: int
) -> Optional[dict]:
    """
    Compares profiles and calculates some advanced parameters
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: a dictionary with 7 keys – name, score, common, sorted_common, max_length_word,
    min_length_word, average_token_length
    """
    if (not isinstance(unknown_profile, dict)
            or not isinstance(profile_to_compare, dict)
            or not isinstance(top_n, int)):
        return None
    unk_top = get_top_n_words(unknown_profile["freq"], top_n)
    check_top = get_top_n_words(profile_to_compare["freq"], top_n)
    common = [token for token in check_top if token in unk_top]
    sorted_common = sorted(common)
    score = len(common) / len(check_top)
    tokens = [token for token, freq in profile_to_compare["freq"].items()]
    max_length_word = max(tokens, key=len)
    min_length_word = min(tokens, key=len)
    average_token_length = sum(map(len, tokens)) / len(tokens)
    comparison = {
        "name": profile_to_compare["name"],
        "common": common,
        "score": score,
        "max_length_word": max_length_word,
        "min_length_word": min_length_word,
        "average_token_length": average_token_length,
        "sorted_common": sorted_common,
    }
    return comparison


def detect_language_advanced(
        unknown_profile: dict, profiles: list, languages: list, top_n: int
) -> Optional[str]:
    """
    Detects the language of an unknown profile within the list of possible languages
    :param unknown_profile: a dictionary
    :param profiles: a list of dictionaries
    :param languages: a list of possible languages
    :param top_n: a number of the most common words
    :return: a language
    """
    if (not isinstance(unknown_profile, dict)
            or not isinstance(profiles, list)
            or not isinstance(languages, list)
            or not isinstance(top_n, int)):
        return None
    lang_match = [
        compare_profiles_advanced(unknown_profile, profile, top_n)
        for profile in profiles
        if profile["name"] in languages or not languages
    ]
    match = sorted(
        sorted(lang_match, key=lambda profile: profile["name"]),
        key=lambda profile: profile["score"],
        reverse=True,
    )
    if match:
        result = match[0]["name"]
        return result
    return None


def load_profile(path_to_file: str) -> Optional[dict]:
    """
    Loads a language profile
    :param path_to_file: a path
    :return: a dictionary with three keys – name, freq, n_words
    """
    if not isinstance(path_to_file, str):
        return None
    if not exists(path_to_file):
        return None
    with open(path_to_file, encoding="utf-8") as profile:
        file = json.load(profile)
        if file:
            return file
        return None


def save_profile(profile: dict) -> int:
    """
    Saves a language profile
    :param profile: a dictionary
    :return: 0 if everything is ok, 1 if not
    """
    if not isinstance(profile, dict):
        return 1
    if ("name" not in profile.keys()
            or "freq" not in profile.keys()
            or "n_words" not in profile.keys()):
        return 1
    if (not isinstance(profile["name"], str)
            or not isinstance(profile["freq"], dict)
            or not isinstance(profile["n_words"], int)):
        return 1
    path_to_file = f'{profile["name"]}.json'
    with open(path_to_file, mode="w", encoding="utf-8") as file:
        json.dump(profile, file)
        return 0
