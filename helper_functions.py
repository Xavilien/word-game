from functools import wraps
from time import time


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


# Returns all words that start with the particular prefix
def search(dictionary, prefix):
    return list(filter(lambda x: x.startswith(prefix), dictionary))


# Returns all words, minus the prefix, that starts with the particular prefix
def search_remaining_letters(dictionary, prefix):
    return list(map(lambda x: x[len(prefix):], search(dictionary, prefix)))


# Returns list of next possible letters along with possible words
def get_possible(dictionary, prefix):
    possible_words = search_remaining_letters(dictionary, prefix)
    if len(possible_words) == 0 or possible_words[0] == "":
        return [], [""]
    possible_letters = sorted(list(set([i[0] for i in possible_words])))

    return possible_letters, possible_words


# Returns whether the player wins if the word is formed
def get_score(player, word):
    parity = len(word) % 2
    score = parity ^ (player % 2)
    return score
