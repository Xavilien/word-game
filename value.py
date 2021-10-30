from helper_functions import *
from preprocessing import dictionary


def value(prefix, player, players_turn):
    possible_words, possible_letters = search(dictionary, prefix)

    # Check if gamestate is terminal, making use of the parity of the remaining words
    if len(possible_words) == 1 or len(set(map(lambda x: len(x) % 2, possible_words))) == 1:
        return get_score(player, possible_words[0])

    if players_turn:
        v = -float("inf")
        for letter in possible_letters:
            v = max(v, value(prefix+letter, player, 0))
            if v == 1:  # Alpha-beta pruning!
                return v
    else:
        v = float("inf")
        for letter in possible_letters:
            v = min(v, value(prefix+letter, player, 1))
            if v == 0:  # Alpha-beta pruning!
                return v

    return v
