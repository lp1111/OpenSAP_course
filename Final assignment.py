def word_list():
    with open("5_letter_words.txt", "r") as words:
        l_o_w = []
        for word in words:
            word = word.strip("\n")
            l_o_w.append(word)

    return l_o_w


def random_word(list_of_words):
    real_word = r.choice(list_of_words)
    return real_word


def is_real_word(gword, wlist):
    return bool(gword in wlist)


def check_guess(gword, rword):
    result = ""
    gletters = ""

    for gletter in list(range(5)):

        if gword[gletter] == rword[gletter]:
            result += "X"
            gletters += gword[gletter]
        elif gword[gletter] in rword and (gletters.count(gword[gletter]) < rword.count(gword[gletter])):
            result += "O"
            gletters += gword[gletter]
        else:
            result += "_"

    return result


def next_guess(list_of_words):
    loop = 0
    while loop < 1:
        guess_word = input("Please enter a guess: ")
        guess_word = guess_word.lower()

        if is_real_word(guess_word, list_of_words):
            return guess_word

        print("That's not a real word!")


def play():
    list_of_words = word_list()
    real_word = random_word(list_of_words)
    # real_word = "visor"
    result = ""
    counter = 0

    while counter < 6:

        guess_word = next_guess(list_of_words)

        result = check_guess(guess_word, real_word)

        if result == "XXXXX":
            return print(result + "\n" + "You won!")

        print(result)
        counter += 1

    return print("You lost!\n" + "The word was", real_word)


import random as r

play()
