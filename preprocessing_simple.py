from nltk.corpus import words
import string
from pygtrie import CharTrie


# Returns list of words from the nltk corpus
def get_dictionary(corpus=words.words()):
    # Remove words greater than 4 letters
    corpus = list(filter(lambda x: len(x) >= 4, corpus))

    # Remove words starting with capital letters because they are likely to be names
    corpus = list(filter(lambda x: x[0] not in string.ascii_uppercase, corpus))

    output = CharTrie()
    for word in corpus:
        output[word] = True

    return output


dictionary = get_dictionary()

# print(len(dictionary))
# >>> 209410

# print(dictionary.keys()[:10])  # Display the first 10 words in the dictionary
# >>> ['aalii', 'aardvark', 'aardwolf', 'abac', 'abaca', 'abacate', 'abacay', 'abacinate', 'abacination', 'abaciscus']

# print(dictionary.keys("mediu"))  # Search the dictionary for words that start with the prefix "mediu"
# >>> ['medium', 'mediumism', 'mediumistic', 'mediumization', 'mediumize', 'mediumship', 'medius']
