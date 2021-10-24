from pygtrie import CharTrie
import preprocessing

dictionary = CharTrie()
for i in preprocessing.dictionary:
    dictionary[i] = True


def get_possible(prefix):
    possible_words = dictionary.keys(prefix)
    if possible_words[0] == prefix:
        return [], [""]
    possible_letters = sorted(list(set([word[len(prefix)] for word in possible_words])))

    return possible_letters, possible_words
