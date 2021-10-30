from value import *
# from value_simple import *


@timing
def main(prefix):
    possible_words, possible_letters = search(dictionary, prefix)

    if len(possible_words) == 0:   # Ensure that the letters typed in can be used to form a word
        print("No word can be formed!\n")
        return

    if len(possible_letters) == 0:  # If prefix is already an actual word
        print(prefix, "is already a word!\n")
        return

    player = (len(prefix)+1) % 2  # Assume that the player who plays the next letter wants to win

    if len(possible_words) == 1:  # If only one possible word can be formed with prefix
        word = possible_words[0]
        print("The only possible word is", word)
        print("You win!\n") if get_score(player, word) == 1 else print("You lose:(\n")
        return

    scores = [value(prefix + letter, player, 0) for letter in possible_letters]
    best_letters = [possible_letters[i] for i in range(len(scores)) if scores[i] == 1]

    if not best_letters:  # If there is no possible way to win, just show all possible letters
        print("There are no winning letters")
        print("Possible letters: ", ", ".join(possible_letters), "\n")
        return

    print("Best letters to pick are:", ", ".join(best_letters), "\n")


if __name__ == '__main__':
    while True:
        main(input("Starting letters: "))

# >>> Starting letters:
# >>> Best letters to pick are: a, e, h, l
