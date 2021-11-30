"""
Lab 3
Language classification using n-grams
"""
import json
import math
from typing import Dict, Tuple
import re


# 4
def tokenize_by_sentence(text: str) -> tuple:
    """
    Splits a text into sentences, sentences into tokens, tokens into letters
    Tokens are framed with '_'
    :param text: a text
    :return: a list of sentence with lists of tokens split into letters
    e.g.
    text = 'She is happy. He is happy.'
    -->  (
         (('_', 's', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_')),
         (('_', 'h', 'e', '_'), ('_', 'i', 's', '_'), ('_', 'h', 'a', 'p', 'p', 'y', '_'))
         )
    """
    if not isinstance(text, str):
        return ()
    # start level - 'sentences'
    sentences_raw = re.split(r"[!.?]\W(?=[\wöüäßÜÖÄẞ])", text)
    # delete empty strings
    sentences_raw = [sentence_raw.lower().strip() for sentence_raw in sentences_raw if sentence_raw]
    text_tuple = []
    for sentence_raw in sentences_raw:
        # start level - 'words'
        words_raw = sentence_raw.split()
        sentence_tuple = []
        for word_raw in words_raw:
            # start level - 'letters'
            word_tuple = [letter for letter in word_raw if letter.isalpha()]
            if word_tuple:
                word_tuple.append('_')
                word_tuple.insert(0, '_')
            word_tuple = tuple(word_tuple)
            # end level - 'letters'
            sentence_tuple.append(word_tuple)
        # end level - 'words'
        # delete empty tuples
        sentence_tuple = tuple(word_tuple for word_tuple in sentence_tuple if word_tuple)
        text_tuple.append(sentence_tuple)
    # end level - 'sentences'
    # delete empty tuples
    text_tuple = tuple(sentence_tuple for sentence_tuple in text_tuple if sentence_tuple)
    return text_tuple


# 4
class LetterStorage:
    """
    Stores and manages letters
    """

    def __init__(self):
        self.storage = {}
        self.counter = 1

    def _put_letter(self, letter: str) -> int:
        """
        Puts a letter into storage, assigns a unique id
        :param letter: a letter
        :return: 0 if succeeds, -1 if not
        """
        if not isinstance(letter, str):
            return -1
        if letter not in self.storage:
            self.storage[letter] = self.counter
            self.counter += 1
        return 0

    def get_id_by_letter(self, letter: str) -> int:
        """
        Gets a unique id by a letter
        :param letter: a letter
        :return: an id
        """
        if not isinstance(letter, str) or letter not in self.storage:
            return -1
        return self.storage[letter]

    def get_letter_by_id(self, letter_id: int) -> str or int:
        """
        Gets a letter by a unique id
        :param letter_id: a unique id
        :return: letter
        """
        storage_upside_down = dict(zip(self.storage.values(), self.storage.keys()))
        if not isinstance(letter_id, int) or letter_id not in storage_upside_down:
            return -1
        return storage_upside_down[letter_id]

    def update(self, corpus: tuple) -> int:
        """
        Fills a storage by letters from the corpus
        :param corpus: a tuple of sentences
        :return: 0 if succeeds, 1 if not
        """
        if not isinstance(corpus, tuple):
            return -1
        for sentence in corpus:
            for word in sentence:
                for letter in word:
                    if self._put_letter(letter) == -1:
                        return -1
        return 0

    def update_string(self, text: str) -> int:
        """
        Fills a storage by letters from the glued_letters
        :param text: a string with glued_letters
        :return: 0 if succeeds, 1 if not
        """
        if not isinstance(text, str):
            return -1
        for letter in text:
            if self._put_letter(letter) == -1:
                return -1
        return 0


# 4
def encode_corpus(storage: LetterStorage, corpus: tuple) -> tuple:
    """
    Encodes sentences by replacing letters with their ids
    :param storage: an instance of the LetterStorage class
    :param corpus: a tuple of sentences
    :return: a tuple of the encoded sentences
    """
    if not (isinstance(storage, LetterStorage) and isinstance(corpus, tuple)):
        return ()
    storage.update(corpus)
    encoded_sentences = tuple(tuple(tuple(storage.get_id_by_letter(letter)
                                          for letter in word)
                                    for word in sentence)
                              for sentence in corpus)
    return encoded_sentences


# 4
def decode_corpus(storage: LetterStorage, corpus: tuple) -> tuple:
    """
    Decodes sentences by replacing letters with their ids
    :param storage: an instance of the LetterStorage class
    :param corpus: an encoded tuple of sentences
    :return: a tuple of the decoded sentences
    """
    if not (isinstance(storage, LetterStorage) and isinstance(corpus, tuple)):
        return ()
    storage.update(corpus)
    decoded_sentences = tuple(tuple(tuple(storage.get_letter_by_id(letter)
                                          for letter in word)
                                    for word in sentence)
                              for sentence in corpus)
    return decoded_sentences


# 6
class NGramTrie:
    """
    Stores and manages ngrams
    """

    def __init__(self, n: int, letter_storage: LetterStorage):
        self.size = n
        self.storage = letter_storage
        self.n_grams = []
        self.n_gram_frequencies = {}
        self.n_gram_log_probabilities = {}

    # 6 - biGrams
    # 8 - threeGrams
    # 10 - nGrams
    def extract_n_grams(self, encoded_corpus: tuple) -> int:
        """
        Extracts n-grams from the given sentence, fills the field n_grams
        :return: 0 if succeeds, 1 if not
        e.g.
        encoded_corpus = (
            ((1, 2, 3, 4, 1), (1, 5, 2, 1)),
            ((1, 3, 4, 1), (1, 5, 2, 1))
        )
        self.size = 2
        --> (
            (
                ((1, 2), (2, 3), (3, 4), (4, 1)), ((1, 5), (5, 2), (2, 1))),
                (((1, 3), (3, 4), (4, 1)), ((1, 5), (5, 2), (2, 1))
            )
        )
        """
        if not isinstance(encoded_corpus, tuple):
            return 1
        n_grams = tuple(tuple(tuple(word[i:i + self.size]
                                    for i in range(len(word) - self.size + 1))
                              for word in sent)
                        for sent in encoded_corpus)
        n_grams = tuple(tuple(word for word in sent if word) for sent in n_grams if sent)
        self.n_grams = tuple(n_grams)
        return 0

    def get_n_grams_frequencies(self) -> int:
        """
        Fills in the n-gram storage from a sentence, fills the field n_gram_frequencies
        :return: 0 if succeeds, 1 if not
        e.g.
        self.n_grams = (
            (
                ((1, 2), (2, 3), (3, 4), (4, 1)), ((1, 5), (5, 2), (2, 1))),
                (((1, 3), (3, 4), (4, 1)), ((1, 5), (5, 2), (2, 1))
            )
        )
        --> {
            (1, 2): 1, (2, 3): 1, (3, 4): 2, (4, 1): 2,
            (1, 5): 2, (5, 2): 2, (2, 1): 2, (1, 3): 1
        }
        """
        if not self.n_grams:
            return 1
        for sentence in self.n_grams:
            for word in sentence:
                for n_gram in word:
                    self.n_gram_frequencies[n_gram] = self.n_gram_frequencies.get(n_gram, 0) + 1
        return 0

    # 8
    def extract_n_grams_frequencies(self, n_grams_dictionary: dict) -> int:
        """
        Extracts n_grams frequencies from given dictionary.
        Fills self.n_gram_frequency field.
        """
        if not isinstance(n_grams_dictionary, dict):
            return 1
        for key, value in n_grams_dictionary.items():
            if isinstance(key, tuple) and isinstance(value, int):
                self.n_gram_frequencies[key] = value
        return 0

    # 10
    def extract_n_grams_log_probabilities(self, n_grams_dictionary: dict) -> int:
        """
        Extracts n_grams log-probabilities from given dictionary.
        Fills self.n_gram_log_probabilities field.
        """
        if not isinstance(n_grams_dictionary, dict):
            return 1
        for n_gram, log_probability in n_grams_dictionary.items():
            if isinstance(n_gram, tuple) and isinstance(log_probability, float):
                self.n_gram_log_probabilities[n_gram] = log_probability
        return 0

    # 10
    def calculate_log_probabilities(self) -> int:
        """
        Gets log-probabilities of n-grams, fills the field n_gram_log_probabilities
        :return: 0 if succeeds, 1 if not
        """
        if not self.n_gram_frequencies:
            return 1
        for n_gram, frequency in self.n_gram_frequencies.items():
            amount = 0
            for n_gram_neighbour, frequency_neighbour in self.n_gram_frequencies.items():
                if n_gram[:-1] == n_gram_neighbour[:-1]:
                    amount += frequency_neighbour
            self.n_gram_log_probabilities[n_gram] = math.log(frequency / amount, math.e)
        return 0


# 6
class LanguageProfile:
    """
    Stores and manages language profile information
    """

    def __init__(self, letter_storage: LetterStorage, language_name: str):
        self.storage = letter_storage
        self.language = language_name
        self.tries = []
        self.n_words = []

    def create_from_tokens(self, encoded_corpus: tuple, ngram_sizes: tuple) -> int:
        """
        Creates a language profile
        :param encoded_corpus: a tuple of encoded letters
        :param ngram_sizes: a tuple of ngram sizes,
            e.g. (1, 2, 3) will indicate the function to create 1,2,3-grams
        :return: 0 if succeeds, 1 if not
        e.g.
        encoded_corpus = (((1, 2, 3, 1), (1, 4, 5, 1), (1, 2, 6, 7, 7, 8, 1)),)
        ngram_sizes = (2, 3)

        self.tries --> [<__main__.NGramTrie object at 0x09DB9BB0>,
        <__main__.NGramTrie object at 0x09DB9A48>]
        self.n_words --> [11, 9]
        self.tries[0].n_grams --> (
            (((1, 2), (2, 3), (3, 1)), ((1, 4), (4, 5), (5, 1)), ((1, 2), (2, 6), (6, 7), (7, 7),
            (7, 8), (8, 1))),
        )
        """
        if not (isinstance(encoded_corpus, tuple) and isinstance(ngram_sizes, tuple)):
            return 1
        for ngram_size in ngram_sizes:
            n_gram_trie = NGramTrie(ngram_size, self.storage)
            extraction_failure = n_gram_trie.extract_n_grams(encoded_corpus)
            frequencies_failure = n_gram_trie.get_n_grams_frequencies()
            if extraction_failure or frequencies_failure:
                return 1
            self.tries.append(n_gram_trie)
            self.n_words.append(len(n_gram_trie.n_gram_frequencies))
        return 0

    def get_top_k_n_grams(self, k: int, trie_level: int) -> tuple:
        """
        Returns the most common n-grams
        :param k: a number of the most common n-grams
        :param trie_level: N-gram size
        :return: a tuple of the most common n-grams
        e.g.
        language_profile = {
            'name': 'en',
            'freq': {
                (1,): 8, (2,): 3, (3,): 2, (4,): 2, (5,): 2,
                (1, 2): 1, (2, 3): 1, (3, 4): 2, (4, 1): 2,
                (1, 5): 2, (5, 2): 2, (2, 1): 2, (1, 3): 1,
                (1, 2, 3): 1, (2, 3, 4): 1, (3, 4, 1): 2,
                (1, 5, 2): 2, (5, 2, 1): 2, (1, 3, 4): 1
            },
            'n_words': [5, 8, 6]
        }
        k = 5
        --> (
            (1,), (2,), (3,), (4,), (5,),
            (3, 4), (4, 1), (1, 5), (5, 2), (2, 1)
        )
        """
        if not (isinstance(k, int) and isinstance(trie_level, int)):
            return ()
        if k <= 0:
            return ()
        for n_gram_trie in self.tries:
            if n_gram_trie.size == trie_level:
                # object NGramTrie with n_gram_frequencies
                frequency = n_gram_trie.n_gram_frequencies
                # .get for returning value from key in dictionary
                top_k_n_grams = tuple(sorted(frequency, key=frequency.get, reverse=True)[:k])
                return top_k_n_grams
        return ()

    # 8
    def save(self, name: str) -> int:
        """
        Saves language profile into json file
        :param name: name of the json file with .json format
        :return: 0 if profile saves, 1 if any errors occurred
        """
        if not isinstance(name, str):
            return 1
        freq = {}
        profile_as_dict = {}
        for n_gram_trie in self.tries:
            freq.update(((''.join(map(self.storage.get_letter_by_id, k)), v)
                         for k, v in n_gram_trie.n_gram_frequencies.items()))
        profile_as_dict["freq"] = freq
        profile_as_dict["n_words"] = self.n_words
        profile_as_dict["name"] = self.language
        # changes for name 'file'
        with open(name, "w", encoding="utf-8") as lang_profile_file:
            json.dump(profile_as_dict, lang_profile_file)
        return 0

    # 8
    def open(self, file_name: str) -> int:
        """
        Opens language profile from json file and writes output to
            self.language,
            self.tries,
            self.n_words fields.
        :param file_name: name of the json file with .json format
        :return: 0 if profile is opened, 1 if any errors occurred
        """
        if not isinstance(file_name, str):
            return 1
        with open(file_name, encoding="utf-8") as lang_profile_file:
            profile_dict = json.load(lang_profile_file)
        # task 1: name and n_words
        self.language = profile_dict["name"]
        self.n_words = profile_dict["n_words"]

        self.tries = []

        # task 3: fill the storage
        for glued_letter in "".join(profile_dict["freq"]):
            self.storage.update_string(glued_letter)

        # task 2, 4, 5: get {2: {"ab": 1, "bd": 2}, 3: {"abc": 5, "cde": 6}}
        tries_dict = {}
        for n_gram, frequency in profile_dict["freq"].items():
            if len(n_gram) not in tries_dict:
                tries_dict[len(n_gram)] = {}
            tries_dict[len(n_gram)][tuple(map(self.storage.get_id_by_letter, n_gram))] = frequency
            # fill self.tries
        for size, freq_dict in tries_dict.items():
            trie = NGramTrie(size, self.storage)
            trie.extract_n_grams_frequencies(freq_dict)
            self.tries.append(trie)
        return 0


# 6
def calculate_distance(unknown_profile: LanguageProfile, known_profile: LanguageProfile,
                       k: int, trie_level: int) -> int:
    """
    Calculates distance between top_k n-grams of unknown profile and known profile
    :param unknown_profile: LanguageProfile class instance
    :param known_profile: LanguageProfile class instance
    :param k: number of frequent N-grams to take into consideration
    :param trie_level: N-gram sizes to use in comparison
    :return: a distance
    Например, первый набор N-грамм для неизвестного профиля - first_n_grams = ((1, 2), (4, 5),
    (2, 3)),
    второй набор N-грамм для известного профиля – second_n_grams = ((1, 2), (2, 3), (4, 5)).
    Расстояние для (1, 2) равно 0, так как индекс в первом наборе – 0, во втором – 0, |0 – 0| = 0.
    Расстояние для (4, 5) равно 1, расстояние для (2, 3) равно 1.
    Соответственно расстояние между наборами равно 2.
    """
    if not (isinstance(unknown_profile, LanguageProfile)
            and isinstance(known_profile, LanguageProfile)
            and isinstance(k, int)
            and isinstance(trie_level, int)):
        return -1
    distance = 0
    frequency_unk = unknown_profile.get_top_k_n_grams(k, trie_level)
    frequency_kn = known_profile.get_top_k_n_grams(k, trie_level)
    for index_unk, element_unk in enumerate(frequency_unk):
        if element_unk not in frequency_kn:
            distance += len(frequency_kn)
        for index_kn, element_kn in enumerate(frequency_kn):
            if element_unk == element_kn:
                distance += abs(index_unk - index_kn)
    return distance


# 8
class LanguageDetector:
    """
    Detects profile language using distance
    """

    def __init__(self):
        self.language_profiles = {}

    def register_language(self, language_profile: LanguageProfile) -> int:
        """
        Adds a new language profile to the storage,
        where the storage is a dictionary like {language: language_profile}
        :param language_profile: a language profile
        :return: 0 if succeeds, 1 if not
        """
        if not isinstance(language_profile, LanguageProfile):
            return 1
        if language_profile not in self.language_profiles:
            self.language_profiles[language_profile.language] = language_profile
        return 0

    def detect(self, unknown_profile: LanguageProfile, k: int, trie_levels: Tuple[int]) -> \
            Dict[str, int] or int:
        """
        Detects the language of an unknown profile and its score
        :param unknown_profile: a dictionary
        :param k: a number of the most common n-grams
        :param trie_levels: N-gram size - tuple with one int for score 8
        :return: a dictionary with language labels and their scores if input is correct, otherwise
        -1
        """
        if not (isinstance(unknown_profile, LanguageProfile)
                and isinstance(k, int)
                and isinstance(trie_levels, tuple)):
            return -1
        dict_label_score = {}
        for language, language_profile in self.language_profiles.items():
            for trie_level in trie_levels:
                dict_label_score[language] = calculate_distance(unknown_profile,
                                                                language_profile,
                                                                k,
                                                                trie_level)
        return dict_label_score


def calculate_probability(unknown_profile: LanguageProfile, known_profile: LanguageProfile,
                          k: int, trie_level: int) -> float or int:
    """
    Calculates probability of unknown_profile top_k ngrams in relation to known_profile
    :param unknown_profile: an instance of unknown profile
    :param known_profile: an instance of known profile
    :param k: number of most frequent ngrams
    :param trie_level: the size of ngrams
    :return: a probability of unknown top k ngrams
    """
    if not (isinstance(unknown_profile, LanguageProfile)
            and isinstance(known_profile, LanguageProfile)
            and isinstance(k, int)
            and isinstance(trie_level, int)):
        return -1

    probability = 0

    for n_gram_trie in known_profile.tries:
        if n_gram_trie.size == trie_level:
            n_gram_trie.calculate_log_probabilities()

            for n_gram in unknown_profile.get_top_k_n_grams(k, trie_level):
                if n_gram in n_gram_trie.n_gram_log_probabilities:
                    probability += n_gram_trie.n_gram_log_probabilities[n_gram]

    return probability


# 10
class ProbabilityLanguageDetector(LanguageDetector):
    """
    Detects profile language using probabilities
    """

    def detect(self, unknown_profile: LanguageProfile, k: int, trie_levels: tuple) -> \
            Dict[Tuple[str, int], int or float] or int:
        """
        Detects the language of an unknown profile and its probability score
        :param unknown_profile: an instance of LanguageDetector
        :param k: a number of the most common n-grams
        :param trie_levels: N-gram size
        :return: sorted language labels with corresponding ngram size and their prob scores
        if input is correct, otherwise -1
        """
        if not (isinstance(unknown_profile, LanguageProfile)
                and isinstance(k, int)
                and isinstance(trie_levels, tuple)):
            return -1
        lang_probabilities = {}
        for language, language_profile in self.language_profiles.items():
            for trie_level in trie_levels:
                lang_probabilities[language, trie_level] = calculate_probability(unknown_profile,
                                                                                 language_profile,
                                                                                 k,
                                                                                 trie_level)
        return lang_probabilities
