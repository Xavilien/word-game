from nltk.corpus import words
import string


# Returns list of words from the nltk corpus
def get_dictionary(corpus=words.words()):
    # Remove words greater than 4 letters
    corpus = list(filter(lambda x: len(x) >= 4, corpus))

    # Remove words starting with capital letters because they are likely to be names
    corpus = list(filter(lambda x: x[0] not in string.ascii_uppercase, corpus))

    return corpus


dictionary = get_dictionary()
# print(len(dictionary))
# print(dictionary[:10])
