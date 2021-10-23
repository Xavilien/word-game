from preprocessing import *


# Return score of all words given the player, 0 if player has to play the last letter and 1 if otherwise
def get_scores(player):
    scores = {}
    for word in dictionary:
        parity = len(word) % 2
        scores[word] = parity ^ (player % 2)
    return scores


def get_possible(curr_word):
    possible_words = search_remaining_letters(dictionary, curr_word)
    if len(possible_words) == 0 or possible_words[0] == "":
        return [], [""]
    possible_letters = sorted(list(set([i[0] for i in possible_words])))

    return possible_letters, possible_words


def value(scores, curr_word, player, players_turn):
    # Check if gamestate is terminal
    next_possible_letters, possible_words = get_possible(curr_word)

    if len(possible_words) == 1 or len(set([scores[curr_word + word] for word in possible_words])) == 1:
        return scores[curr_word + possible_words[0]]

    if players_turn:
        v = -float("inf")
        for letter in next_possible_letters:
            v = max(v, value(scores, curr_word+letter, player, 0))
            if v == 1:
                return v
    else:
        v = float("inf")
        for letter in next_possible_letters:
            v = min(v, value(scores, curr_word+letter, player, 1))
            if v == 0:
                return v

    return v


@timing
def main(curr_word):
    if not search(dictionary, curr_word):  # Ensure that the letters typed in can be used to form a word
        print("No word can be formed\n")
        return

    player = (len(curr_word)+1) % 2  # Assume that the player who plays the next letter wants to win
    scores = get_scores(player)

    possible_letters, possible_words = get_possible(curr_word)

    if not possible_letters:  # If curr_word is already an actual word
        print(curr_word, "is already a word!\n")
        return

    if len(possible_words) == 1:  # If only one possible word can be formed with curr_word
        word = curr_word + possible_words[0]
        print("The only possible word is", word, '\n')
        print("You win!") if scores[word] == 1 else print("You lose:(")
        return

    scores = [value(dictionary, scores, curr_word + letter, player, 0) for letter in possible_letters]
    best_letters = [possible_letters[i] for i in range(len(scores)) if scores[i] == 1]

    if not best_letters:  # If there is no possible way to win, just show all possible letters
        print("There are no winning letters")
        print("Possible letters: ", ", ".join(possible_letters))
        return

    print("Best letters to pick are:", ", ".join(best_letters))


if __name__ == '__main__':
    dictionary = get_dictionary()
    while True:
        main(input("Starting letters: "))
