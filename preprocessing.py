from nltk.corpus import words
import string
import json
from helper_functions import *


# Recursively remove words that contain another word as prefix
def remove_unnecessary_words(dictionary, prefix):
    if len(dictionary) == 0:
        return []
    if dictionary[0] == "":
        return [prefix]

    new_dictionary = []
    for i in string.ascii_lowercase:
        new_dictionary += remove_unnecessary_words(search_remaining_letters(dictionary, i), prefix+i)
    return new_dictionary


# @timing
# Load dictionary file if it exists else create a new one
def get_dictionary(dictionary=words.words()):
    try:
        with open("dictionary.txt", "r") as d:
            dictionary = json.load(d)
        return dictionary

    except FileNotFoundError:
        # Remove words greater than 4 letters
        dictionary = list(filter(lambda x: len(x) >= 4, dictionary))

        # Remove words starting with capital letters because they are likely to be names
        dictionary = list(filter(lambda x: x[0] not in string.ascii_uppercase, dictionary))

        # Remove words that contain another word as a prefix
        dictionary = remove_unnecessary_words(dictionary, "")

        with open("dictionary.txt", "w") as d:
            json.dump(dictionary, d)

        return dictionary


dictionary = get_dictionary()
print(len(dictionary))
# >>> 83111
