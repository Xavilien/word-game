from helper_functions import *
from preprocessing_simple import dictionary


def value(prefix, player, players_turn):
    possible_words, possible_letters = search(dictionary, prefix)

    if len(possible_letters) == 0:  # Check if gamestate is terminal
        return get_score(player, possible_words[0])

    if players_turn:  # Max if it is player's turn
        v = -float("inf")
        for letter in possible_letters:
            v = max(v, value(prefix+letter, player, 0))
    else:  # Min if it is opponent's turn
        v = float("inf")
        for letter in possible_letters:
            v = min(v, value(prefix+letter, player, 1))

    return v
