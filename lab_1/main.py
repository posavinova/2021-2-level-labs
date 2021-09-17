"""
Lab 1
Language detection
"""


import json
import re

from os.path import exists
from typing import Optional


def tokenize(text: str) -> Optional[list]:
    """
    Splits a text into tokens, converts the tokens into lowercase,
    removes punctuation and other symbols from words
    :param text: a text
    :return: a list of lower-cased tokens without punctuation
    """
    if isinstance(text, str):
        tokenized = (
            "".join([char for char in text if char.isalpha() or char.isspace()])
            .strip()
            .lower()
            .split()
        )
        return tokenized
    else:
        return None


def remove_stop_words(tokens: list, stop_words: list) -> Optional[list]:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    """
    if (
        isinstance(tokens, list)
        and isinstance(stop_words, list)
        and all(isinstance(i, str) for i in tokens)
    ):
        cleaned = [word for word in tokens if word not in stop_words]
        return cleaned
    else:
        return None


def calculate_frequencies(tokens: list) -> Optional[dict]:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """
    if isinstance(tokens, list) and all(isinstance(i, str) for i in tokens):
        freq_dict = {}
        for word in tokens:
            freq_dict[word] = tokens.count(word)
        return freq_dict
    else:
        return None


def get_top_n_words(freq_dict: dict, top_n: int) -> Optional[list]:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words
    :return: a list of the most common words
    """
    if (
        isinstance(freq_dict, dict)
        and isinstance(top_n, int)
        and all(isinstance(value, int) for value in freq_dict.values())
    ):
        sorted_dict = [
            pair[0]
            for pair in sorted(
                freq_dict.items(), key=lambda item: item[1], reverse=True
            )
        ]
        if top_n <= len(sorted_dict):
            return sorted_dict[:top_n]
        else:
            return sorted_dict
    else:
        return None


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
    if (
        isinstance(language, str)
        and isinstance(text, str)
        and isinstance(stop_words, list)
    ):
        tokenized = tokenize(text)
        cleared = remove_stop_words(tokenized, stop_words)
        freq_dict = calculate_frequencies(cleared)
        lang_profile = {"name": language, "freq": freq_dict, "n_words": len(freq_dict)}
        return lang_profile
    else:
        return None


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
    if (
        isinstance(unknown_profile, dict)
        and isinstance(profile_to_compare, dict)
        and isinstance(top_n, int)
    ):
        top_1 = get_top_n_words(unknown_profile.get("freq"), top_n)
        top_2 = get_top_n_words(profile_to_compare.get("freq"), top_n)
        if (top_1 and top_2) is not None:
            common = set(top_1).intersection(set(top_2))
            return round(len(common) / len(top_2), 2)
    else:
        return None


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
    if (
        isinstance(unknown_profile, dict)
        and isinstance(profile_1, dict)
        and isinstance(profile_2, dict)
    ):
        match_1 = compare_profiles(profile_1, unknown_profile, top_n)
        match_2 = compare_profiles(profile_2, unknown_profile, top_n)
        match = max([(match_1, profile_1["name"]), (match_2, profile_2["name"])])[1]
        return match
    else:
        return None


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
    if (
        isinstance(unknown_profile, dict)
        and isinstance(profile_to_compare, dict)
        and isinstance(top_n, int)
    ):
        unk_top = get_top_n_words(unknown_profile.get("freq"), top_n)
        check_top = get_top_n_words(profile_to_compare.get("freq"), top_n)
        if (unk_top and check_top) is not None:
            common = [token for token in check_top if token in unk_top]
            score = len(common) / len(check_top)
            sorted_common = sorted(common)
            tokens = profile_to_compare["freq"].keys()
            max_length_word = max(tokens, key=len)
            min_length_word = min(tokens, key=len)
            average_token_length = sum(map(len, tokens)) / len(tokens)
            comparison = {
                "name": profile_to_compare.get("name"),
                "common": common,
                "score": score,
                "max_length_word": max_length_word,
                "min_length_word": min_length_word,
                "average_token_length": average_token_length,
                "sorted_common": sorted_common,
            }
            return comparison
    else:
        return None


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
    if (
        isinstance(unknown_profile, dict)
        and isinstance(profiles, list)
        and isinstance(languages, list)
        and isinstance(top_n, int)
    ):
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
            return match[0]["name"]
        else:
            return None
    else:
        return None


def load_profile(path_to_file: str) -> Optional[dict]:
    """
    Loads a language profile
    :param path_to_file: a path
    :return: a dictionary with three keys – name, freq, n_words
    """
    if isinstance(path_to_file, str):
        if exists(path_to_file):
            with open(path_to_file, encoding="utf-8") as profile:
                file = json.load(profile)
                if file:
                    return file
                else:
                    return None
        else:
            return None
    else:
        return None


def save_profile(profile: dict) -> int:
    """
    Saves a language profile
    :param profile: a dictionary
    :return: 0 if everything is ok, 1 if not
    """
    if isinstance(profile, dict):
        pass
    else:
        return 1
    if (
        "name" in profile.keys()
        and "freq" in profile.keys()
        and "n_words" in profile.keys()
        and isinstance(profile["name"], str)
        and isinstance(profile["freq"], dict)
        and isinstance(profile["n_words"], int)
    ):
        path_to_file = f'{profile["name"]}.json'
        with open(path_to_file, mode="w", encoding="utf-8") as file:
            json.dump(profile, file)
            return 0
    else:
        return 1
