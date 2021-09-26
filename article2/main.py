from preprocessing import *


# Return score of all words given the player, 0 if player has to play the last letter and 1 if otherwise
def get_scores(dictionary, player):
    scores = {}
    for word in dictionary:
        parity = len(word) % 2
        scores[word] = parity ^ (player % 2)
    return scores


def get_possible(dictionary, curr_word):
    possible_words = search_remaining_letters(dictionary, curr_word)
    if len(possible_words) == 0 or possible_words[0] == "":
        return [], [""]
    possible_letters = sorted(list(set([i[0] for i in possible_words])))

    return possible_letters, possible_words


def value(dictionary, scores, curr_word, player, players_turn):
    # Check if gamestate is terminal
    next_possible_letters, possible_words = get_possible(dictionary, curr_word)

    if len(possible_words) == 1 or len(set([scores[curr_word + word] for word in possible_words])) == 1:
        return scores[curr_word + possible_words[0]]

    if players_turn:
        v = -float("inf")
        for letter in next_possible_letters:
            v = max(v, value(dictionary, scores, curr_word+letter, player, 0))
            if v == 1:
                return v
    else:
        v = float("inf")
        for letter in next_possible_letters:
            v = min(v, value(dictionary, scores, curr_word+letter, player, 1))
            if v == 0:
                return v
    return v


# Tell you whether you win given a word
def show_winner(scores, word):
    print("You win!") if scores[word] == 1 else print("You lose:(")


@timing
def get_next_letter(dictionary, scores, player, curr_word):
    possible_letters, possible_words = get_possible(dictionary, curr_word)

    if not possible_letters:
        return show_winner(scores, curr_word)

    if len(possible_words) == 1:
        word = curr_word + possible_words[0]
        print("The only possible word is", word, '\n')
        return show_winner(scores, word)

    scores = [value(dictionary, scores, curr_word + letter, player, 0) for letter in possible_letters]
    best_indices = [i for i in range(len(scores)) if scores[i] == 1]
    best_letters = [possible_letters[i] for i in best_indices]

    if not best_letters:
        print("There are no winning letters")
        print("Possible letters: ", ", ".join(possible_letters))
        return possible_letters

    print("Best letters to pick are:", ", ".join(best_letters))

    return best_letters


def main():
    dictionary = get_dictionary()
    # player = int(input("Player 1 or 2: "))
    # scores = get_scores(dictionary, player)

    while True:
        curr_word = input("Starting letters: ")
        if not search(dictionary, curr_word):
            print("No word can be formed\n")
            continue

        player = (len(curr_word)+1) % 2
        scores = get_scores(dictionary, player)
        get_next_letter(dictionary, scores, player, curr_word)


if __name__ == '__main__':
    main()
