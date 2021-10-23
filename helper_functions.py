# Returns all words that start with the particular subword
def search(dictionary, subword):
    return list(filter(lambda x: x.startswith(subword), dictionary))


# Returns all words, minus the subword, that starts with the particular subword
def search_remaining_letters(dictionary, subword):
    return list(map(lambda x: x[len(subword):], search(dictionary, subword)))


# Returns list of next possible letters along with possible words
def get_possible(dictionary, curr_word):
    possible_words = search_remaining_letters(dictionary, curr_word)
    if len(possible_words) == 0 or possible_words[0] == "":
        return [], [""]
    possible_letters = sorted(list(set([i[0] for i in possible_words])))

    return possible_letters, possible_words


# Returns whether the player wins if the word is formed
def get_score(player, word):
    parity = len(word) % 2
    score = parity ^ (player % 2)
    return score
