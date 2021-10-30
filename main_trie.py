from helper_functions_simple import *
import trie
import trie2


def value(curr_word, player, players_turn):
    next_possible_letters, possible_words = trie.get_possible(curr_word)

    if not next_possible_letters: # or len(set(map(lambda x: len(x) % 2, possible_words))) == 1:  # Check if gamestate is terminal
        return get_score(player, curr_word)

    if players_turn:  # Max if it is player's turn
        v = -float("inf")
        for letter in next_possible_letters:
            v = max(v, value(curr_word+letter, player, 0))
    else:  # Min if it is opponent's turn
        v = float("inf")
        for letter in next_possible_letters:
            v = min(v, value(curr_word+letter, player, 1))

    return v


@timing
def main(curr_word):
    if not search(curr_word):  # Ensure that the letters typed in can be used to form a word
        print("No word can be formed\n")
        return

    player = (len(curr_word)+1) % 2  # Assume that the player who plays the next letter wants to win

    possible_letters, possible_words = get_possible(curr_word)

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
    while True:
        main(input("Starting letters: "))

# >>> Starting letters:
# >>> Best letters to pick are: a, e, h, l