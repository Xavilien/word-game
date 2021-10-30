from functools import wraps
from time import time
from preprocessing_simple import dictionary


# Decorator to determine how long a function takes to run
def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f'{f.__name__} took {(end-start):.3f}s to run\n')
        return result
    return wrap


# Returns list of words that start with a particular prefix as well as the next possible letters
def search(dictionary, prefix):
    try:
        possible_words = dictionary.keys(prefix)
    except KeyError:  # No word starting with the prefix exists
        return [], []

    try:
        possible_letters = sorted(list(set([word[len(prefix)] for word in possible_words])))
    except IndexError:  # Prefix is already a word
        return possible_words, []

    return possible_words, possible_letters


# Returns whether the player wins if the word is formed
def get_score(player, word):
    parity = len(word) % 2
    score = parity ^ (player % 2)
    return score


# print(search(dictionary, "mediu"))
# >>> (['medium', 'mediumism', 'mediumistic', 'mediumization', 'mediumize', 'mediumship', 'medius'], ['m', 's'])

# print(get_score(1, "medium"))
# >>> 1

# print(get_score(2, "medium"))
# >>> 0
