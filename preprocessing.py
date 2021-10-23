from nltk.corpus import words
import string
import json
from functools import wraps
from time import time


# Returns all words that start with the particular subword
def search(dictionary, subword):
    return list(filter(lambda x: x.startswith(subword), dictionary))


# Returns all words, minus the subword, that starts with the particular subword
def search_remaining_letters(dictionary, subword):
    return list(map(lambda x: x[len(subword):], search(dictionary, subword)))


# Recursively remove words that contain another word as prefix
def remove_prefix(dictionary, prefix):
    if len(dictionary) == 0:
        return []
    if dictionary[0] == "":
        return [prefix]

    new_dictionary = []
    for i in string.ascii_lowercase:
        new_dictionary += remove_prefix(search_remaining_letters(dictionary, i), prefix+i)
    return new_dictionary


def preprocess(dictionary):
    # Remove words greater than 4 letters
    dictionary = list(filter(lambda x: len(x) >= 4, dictionary))

    # Remove words starting with capital letters because they are likely to be names
    dictionary = list(filter(lambda x: x[0] not in string.ascii_uppercase, dictionary))

    # Remove words that contain another word as a prefix
    dictionary = remove_prefix(dictionary, "")

    with open("article2/dictionary.txt", "w") as d:
        json.dump(dictionary, d)

    return dictionary


# @timing
# Load dictionary file if it exists else create a new one
def get_dictionary(dictionary=words.words()):
    try:
        with open("article2/dictionary.txt", "r") as d:
            dictionary = json.load(d)
        return dictionary
    except FileNotFoundError:
        return preprocess(dictionary)
