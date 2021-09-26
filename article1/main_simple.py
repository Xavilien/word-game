from preprocessing_simple import *


def value(curr_word, player, players_turn):
    # Check if gamestate is terminal
    possible_words = search(curr_word)

    if len(possible_words) == 1:
        parity = len(possible_words[0]) % 2
        v = parity & (player % 2)
        return v

    # Get next possible letters
    next_possible_letters, possible_words = get_possible(curr_word)

    if players_turn:
        v = -float("inf")
        for letter in next_possible_letters:
            v = max(v, value(curr_word+letter, player, 0))
    else:
        v = float("inf")
        for letter in next_possible_letters:
            v = min(v, value(curr_word+letter, player, 1))
    return v


def get_next_letter(scores, player, curr_word):
    possible_letters, possible_words = get_possible(curr_word)

    if not possible_letters:
        print("You win!") if scores[curr_word] == 1 else print("You lose:(")
        return

    if len(possible_words) == 1:
        word = curr_word + possible_words[0]
        print("The only possible word is", word, '\n')
        print("You win!") if scores[word] == 1 else print("You lose:(")
        return

    scores = [value(scores, curr_word + letter, player, 0) for letter in possible_letters]
    best_indices = [i for i in range(len(scores)) if scores[i] == 1]
    best_letters = [possible_letters[i] for i in best_indices]

    if not best_letters:
        print("There are no winning letters")
        print("Possible letters: ", ", ".join(possible_letters))
        return possible_letters

    print("Best letters to pick are:", ", ".join(best_letters))

    return best_letters


def main():
    while True:
        curr_word = input("Starting letters: ")
        player = (len(curr_word)+1) % 2
        scores = get_scores(player)
        get_next_letter(scores, player, curr_word)


if __name__ == '__main__':
    main()
