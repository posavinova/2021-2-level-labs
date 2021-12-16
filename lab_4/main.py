"""
Lab 4
Language generation algorithm based on language profiles
"""
import re
import json
from typing import Tuple
from lab_4.storage import Storage
from lab_4.language_profile import LanguageProfile
from lab_4.language_profile import NGramTrie


# 4
def tokenize_by_letters(text: str) -> Tuple or int:
    """
    Tokenizes given sequence by letters
    """
    if not isinstance(text, str):
        return -1
    text = "".join(char for char in text if char.isalpha() or char.isspace())
    tokenized = tuple(tuple("_" + word + "_") for word in text.lower().strip().split())
    return tokenized


# 4
class LetterStorage(Storage):
    """
    Stores letters and their ids
    """

    def update(self, elements: tuple) -> int:
        """
        Fills a storage by letters from the tuple
        :param elements: a tuple of tuples of letters
        :return: 0 if succeeds, -1 if not
        """
        if not isinstance(elements, tuple):
            return -1
        for token in elements:
            for letter in token:
                self._put(letter)
        return 0

    def get_letter_count(self) -> int:
        """
        Gets the number of letters in the storage
        """
        if not self.storage:
            return -1
        return len(self.storage)


# 4
def encode_corpus(storage: LetterStorage, corpus: tuple) -> tuple:
    """
    Encodes corpus by replacing letters with their ids
    :param storage: an instance of the LetterStorage class
    :param corpus: a tuple of tuples
    :return: a tuple of the encoded letters
    """
    if not (isinstance(storage, LetterStorage) and isinstance(corpus, tuple)):
        return ()
    storage.update(corpus)
    encoded = tuple(tuple(storage.get_id(letter) for letter in token) for token in corpus)
    return encoded


# 4
def decode_sentence(storage: LetterStorage, sentence: tuple) -> tuple:
    """
    Decodes sentence by replacing letters with their ids
    :param storage: an instance of the LetterStorage class
    :param sentence: a tuple of tuples-encoded words
    :return: a tuple of the decoded sentence
    """
    if not (isinstance(storage, LetterStorage) and isinstance(sentence, tuple)):
        return ()
    decoded = tuple(
        tuple(storage.get_element(letter) for letter in token) for token in sentence
    )
    return decoded


# 6
class NGramTextGenerator:
    """
    Language model for basic text generation
    """

    def __init__(self, language_profile: LanguageProfile):
        self.profile = language_profile
        self._used_n_grams = []

    def get_trie_by_level(self, trie_level: int):
        """
        Gets NGramTrie of the requested N-gram size
        :param trie_level: N-gram size
        :return: NGramTrie if succeeds, None if not
        """
        for trie in self.profile.tries:
            if trie.size == trie_level:
                return trie
        return None

    def _generate_letter(self, context: tuple) -> int:
        """
        Generates the next letter.
            Takes the letter from the most
            frequent ngram corresponding to the context given.
        """
        if not isinstance(context, tuple):
            return -1
        trie = self.get_trie_by_level(len(context) + 1)
        if not trie:
            return -1
        frequencies = {
            n_gram: freq
            for n_gram, freq in trie.n_gram_frequencies.items()
            if n_gram[:-1] == context and n_gram not in self._used_n_grams
        }
        if not frequencies:
            frequencies = {
                n_gram: freq
                for n_gram, freq in trie.n_gram_frequencies.items()
                if n_gram not in self._used_n_grams
            }
        if not frequencies:
            self._used_n_grams = []
            frequencies = {
                n_gram: freq
                for n_gram, freq in trie.n_gram_frequencies.items()
                if n_gram[:-1] == context
            }
        if not frequencies:
            return -1
        n_gram = max(frequencies, key=frequencies.get)
        self._used_n_grams.append(n_gram)
        return n_gram[-1]

    def _generate_word(self, context: tuple, word_max_length=15) -> tuple:
        """
        Generates full word for the context given.
        """
        if not isinstance(context, tuple) or not isinstance(word_max_length, int):
            return ()

        special_id = self.profile.storage.get_special_token_id()
        trie_level = len(context)
        if context[-1] == special_id:
            context = (special_id,)
        token = [*context]
        letter = None

        while not (letter == special_id or len(token) >= word_max_length):
            context = tuple(token[-trie_level:])
            letter = self._generate_letter(context)
            token.append(letter)

        if len(token) >= word_max_length and token[-1] != special_id:
            token.append(special_id)
        word = tuple(token)
        return word

    def generate_sentence(self, context: tuple, word_limit: int) -> tuple:
        """
        Generates full sentence with fixed number of words given.
        """
        if not isinstance(context, tuple) or not isinstance(word_limit, int):
            return ()
        sentence = []
        for _ in range(word_limit):
            word = self._generate_word(context)
            context = word[-len(context) :]
            sentence.append(word)
        sentence = tuple(sentence)
        return sentence

    def generate_decoded_sentence(self, context: tuple, word_limit: int) -> str:
        """
        Generates full sentence and decodes it
        """
        if not isinstance(context, tuple) or not isinstance(word_limit, int):
            return ()
        sentence = self.generate_sentence(context, word_limit)
        sentence = tuple(
            self.profile.storage.get_element(i) for token in sentence for i in token
        )
        generation = translate_sentence_to_plain_text(sentence)
        return generation


# 6
def translate_sentence_to_plain_text(decoded_corpus: tuple) -> str:
    """
    Converts decoded sentence into the string sequence
    """
    if not isinstance(decoded_corpus, tuple):
        return ""
    sentence = [letter for token in decoded_corpus for letter in token]
    if len(sentence):
        if sentence[0] == "_":
            sentence.pop(0)
        if sentence[0].islower():
            sentence[0] = sentence[0].upper()
        if sentence[-1] == "_":
            sentence[-1] = "."
    sentence = re.sub("_+", " ", "".join(sentence))
    return sentence


# 8
class LikelihoodBasedTextGenerator(NGramTextGenerator):
    """
    Language model for likelihood based text generation
    """

    def _calculate_maximum_likelihood(self, letter: int, context: tuple) -> float:
        """
        Calculates maximum likelihood for a given letter
        :param letter: a letter given
        :param context: a context for the letter given
        :return: float number, that indicates maximum likelihood
        """
        if not (isinstance(letter, int) and isinstance(context, tuple) and context):
            return -1
        n_gram = (*context, letter)
        trie = self.get_trie_by_level(len(context) + 1)
        contexts = {
            n_gram: freq
            for n_gram, freq in trie.n_gram_frequencies.items()
            if n_gram[:-1] == context
        }
        if not (contexts and n_gram in contexts):
            return 0.0
        probability = contexts[n_gram] / sum(contexts.values())
        return probability

    def _generate_letter(self, context: tuple) -> int:
        """
        Generates the next letter.
            Takes the letter with highest
            maximum likelihood frequency.
        """
        if not (isinstance(context, tuple) and context):
            return -1
        trie = self.get_trie_by_level(len(context) + 1)
        probabilities = {}
        contexts = {
            n_gram: freq
            for n_gram, freq in trie.n_gram_frequencies.items()
            if n_gram[:-1] == context
        }
        if not contexts:
            trie = self.get_trie_by_level(1)
            contexts = trie.n_gram_frequencies
        for n_gram in contexts:
            probabilities[n_gram] = self._calculate_maximum_likelihood(
                n_gram[-1], n_gram[:-1]
            )
        letter = max(probabilities, key=probabilities.get)[-1]
        return letter


# 10
class BackOffGenerator(NGramTextGenerator):
    """
    Language model for back-off based text generation
    """

    def _generate_letter(self, context: tuple) -> int:
        """
        Generates the next letter.
            Takes the letter with highest
            available frequency for the corresponding context.
            if no context can be found, reduces the context size by 1.
        """
        if not isinstance(context, tuple):
            return -1
        trie = self.get_trie_by_level(len(context) + 1)
        contexts = {
            n_gram: freq
            for n_gram, freq in trie.n_gram_frequencies.items()
            if n_gram[:-1] == context and n_gram not in self._used_n_grams
        }
        if not contexts:
            return self._generate_letter(context[1:])
        n_gram = max(contexts, key=contexts.get)
        self._used_n_grams.append(n_gram)
        return n_gram[-1]


# 10
class PublicLanguageProfile(LanguageProfile):
    """
    Language Profile to work with public language profiles
    """

    def open(self, file_name: str) -> int:
        """
        Opens public profile and adapts it.
        :return: o if succeeds, 1 otherwise
        """
        if not isinstance(file_name, str):
            return 1
        with open(file_name, encoding="utf-8") as file:
            text = json.load(file)
        self.language = text["name"]
        self.n_words = text["n_words"]
        self.tries = [
            self._build_n_gram_trie(text["freq"], trie_level)
            for trie_level in set(map(len, text["freq"]))
        ]
        return 0

    def _build_n_gram_trie(
        self, n_gram_frequencies: dict, trie_level: int
    ) -> NGramTrie:
        """
        Helper function to build N-Gram tries from imported dictionaries.
        :param n_gram_frequencies: a dictionary of N-gram frequencies
        :param trie_level: trie level
        :return: NGramTrie
        """
        n_gram_trie = NGramTrie(trie_level, self.storage)
        for raw_n_gram, freq in n_gram_frequencies.items():
            if len(raw_n_gram) == trie_level:
                n_gram = raw_n_gram.replace(" ", "_").lower()
                self.storage.update(tuple(n_gram))
                n_gram = tuple(map(self.storage.get_id, n_gram))
                if n_gram not in n_gram_trie.n_gram_frequencies:
                    n_gram_trie.n_gram_frequencies[n_gram] = 0
                n_gram_trie.n_gram_frequencies[n_gram] += freq
        return n_gram_trie
