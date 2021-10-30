from nltk.corpus import words
import string
from pygtrie import CharTrie
import json


# Recursively remove words that contain another word as prefix
def remove_unnecessary_words(corpus, prefix):
    if len(corpus) == 0:
        return []
    if corpus[0] == "":
        return [prefix]

    new_dictionary = []
    for i in string.ascii_lowercase:
        possible_words = filter(lambda x: x.startswith(prefix), dictionary)
        possible_letters = list(map(lambda x: x[len(prefix):], possible_words))
        new_dictionary += remove_unnecessary_words(possible_letters, prefix + i)
    return new_dictionary


# @timing
# Load dictionary file if it exists else create a new one
def get_dictionary(corpus=words.words()):
    try:
        with open("dictionary.txt", "r") as d:
            corpus = json.load(d)

    except FileNotFoundError:
        # Remove words greater than 4 letters
        corpus = list(filter(lambda x: len(x) >= 4, corpus))

        # Remove words starting with capital letters because they are likely to be names
        corpus = list(filter(lambda x: x[0] not in string.ascii_uppercase, corpus))

        # Remove words that contain another word as a prefix
        corpus = remove_unnecessary_words(corpus, "")

        with open("dictionary.txt", "w") as d:
            json.dump(corpus, d)

    output = CharTrie()
    for word in corpus:
        output[word] = True
    return output


dictionary = get_dictionary()
# print(len(dictionary))
# >>> 83111
