from preprocessing_simple import *


# Returns all words that start with the particular subword
def search(subword):
    return list(filter(lambda x: x.startswith(subword), dictionary))


# Returns all words, minus the subword, that starts with the particular subword
def search_remaining_letters(subword):
    return list(map(lambda x: x[len(subword):], search(subword)))


def get_possible(curr_word):
    possible_words = search_remaining_letters(curr_word)
    if len(possible_words) == 0 or possible_words[0] == "":
        return [], [""]
    possible_letters = list(set([i[0] for i in possible_words]))

    return sorted(list(set(possible_letters))), possible_words

# print(search(dictionary, "epidemi"))
# print(search_remaining_letters(dictionary, "epidemi"))
