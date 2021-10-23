from preprocessing import *
from helper_functions_simple import timing


def value(curr_word, player, players_turn):
    next_possible_letters, possible_words = get_possible(dictionary, curr_word)

    # Check if gamestate is terminal, making use of the precalculated scores
    if len(possible_words) == 1 or len(set(map(len, possible_words))) == 1:
        return get_score(player, curr_word + possible_words[0])

    if players_turn:
        v = -float("inf")
        for letter in next_possible_letters:
            v = max(v, value(curr_word+letter, player, 0))
            if v == 1:  # Alpha-beta pruning
                return v
    else:
        v = float("inf")
        for letter in next_possible_letters:
            v = min(v, value(curr_word+letter, player, 1))
            if v == 0:  # Alpha-beta pruning
                return v

    return v


@timing
def main(curr_word):
    if not search(dictionary, curr_word):  # Ensure that the letters typed in can be used to form a word
        print("No word can be formed\n")
        return

    player = (len(curr_word)+1) % 2  # Assume that the player who plays the next letter wants to win

    possible_letters, possible_words = get_possible(dictionary, curr_word)

    if not possible_letters:  # If curr_word is already an actual word
        print(curr_word, "is already a word!\n")
        return

    if len(possible_words) == 1:  # If only one possible word can be formed with curr_word
        word = curr_word + possible_words[0]
        print("The only possible word is", word)
        print("You win!\n") if get_score(player, word) == 1 else print("You lose:(\n")
        return

    scores = [value(curr_word + letter, player, 0) for letter in possible_letters]
    best_letters = [possible_letters[i] for i in range(len(scores)) if scores[i] == 1]

    if not best_letters:  # If there is no possible way to win, just show all possible letters
        print("There are no winning letters")
        print("Possible letters: ", ", ".join(possible_letters), "\n")
        return

    print("Best letters to pick are:", ", ".join(best_letters), "\n")


if __name__ == '__main__':
    dictionary = get_dictionary()
    while True:
        main(input("Starting letters: "))
