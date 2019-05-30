import random


def play():
    print_open_message()

    secret_word = load_secret_word()

    successful_words = success_words(secret_word)
    print(successful_words)

    Hanged = False
    success = False
    mistakes = 0

    while (not Hanged and not success):

        guess = guessing()

        if (guess in secret_word):
            pin_successful_guess(guess, successful_words, secret_word)
        else:
            mistakes += 1
            hangman_draw(mistakes)

        Hanged = mistakes == 7
        success = "_" not in successful_words
        print(successful_words)
    if (success):
        print_winner_message()
    else:
        print_loser_message(secret_word)


def print_open_message():
    print("**********************************")
    print("***Welcome to the HangMan Game!***")
    print("**********************************")


def load_secret_word():
    file = open('words.txt', 'r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def success_words(word):
    return ['_' for letter in word]


def guessing():
    guess = input("Guess a letter! ")
    guess = guess.strip().upper()
    return guess


def pin_successful_guess(guess, successful_words, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            successful_words[index] = letter
        index += 1


def print_winner_message():
    print("Congratulations, you won!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(secret_word):
    print("Your were hanged, better luck next time!")
    print("The word was{}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def hangman_draw(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if (mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    play()
