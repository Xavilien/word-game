from helper_functions_simple import *


def value(curr_word, player, players_turn):
    next_possible_letters, possible_words = get_possible(curr_word)

    if len(possible_words) == 1:  # Check if gamestate is terminal
        return get_score(player, curr_word + possible_words[0])

    if players_turn:  # Max if it is player's turn
        v = -float("inf")
        for letter in next_possible_letters:
            v = max(v, value(curr_word+letter, player, 0))
    else:  # Min if it is opponent's turn
        v = float("inf")
        for letter in next_possible_letters:
            v = min(v, value(curr_word+letter, player, 1))
    return v


def main():
    while True:
        curr_word = input("Starting letters: ")
        player = (len(curr_word)+1) % 2

        possible_letters, possible_words = get_possible(curr_word)

        if not possible_letters:
            print("You win!\n") if get_score(player, curr_word) == 1 else print("You lose:(\n")
            continue

        if len(possible_words) == 1:
            word = curr_word + possible_words[0]
            print("The only possible word is", word)
            print("You win!\n") if get_score(player, word) == 1 else print("You lose:(\n")
            continue

        scores = [value(curr_word + letter, player, 0) for letter in possible_letters]
        best_letters = [possible_letters[i] for i in range(len(scores)) if scores[i] == 1]

        if not best_letters:
            print("There are no winning letters")
            print("Possible letters: ", ", ".join(possible_letters))
            continue

        print("Best letters to pick are:", ", ".join(best_letters), "\n")


if __name__ == '__main__':
    main()
