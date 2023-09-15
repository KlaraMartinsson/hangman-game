import random
import word_art
from words import words_1
from words import words_2
from words import words_3
from hangman_stages import hangman_stages


def game_rules(data):
    """
    Checks if player want's to read the rules. If not the game continues.
    """
    if data == "Y":
        print(word_art.rules_style)
        print("1. You can only guess one letter at a time.\n")
        print("You have 3 diffrent levels of difficulity:")
        print("\n'1' for easy, '2' for medium and '3' for hard.")
        print("\n2. If you guess correct the letter will appear in the word.")
        print("\n3. If you guess all the letters in the word, you win.\n")
        print("\n4. If you guess incorrect a body part goes on Hangman.")
        print("If you guess wrong 6 times you hang your Hangman and lose.\n")
        return True
    elif data == "N":
        return True
    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")


def validate_level(data):
    """
    Validates the level the player choose.
    """
    try:
        if data.isalpha():
            raise ValueError(
                f"You need to enter a whole number. You entered: {data}")
        if int(data) < 1:
            raise ValueError(f"Minimum level is 1. You entered: {data}")
        if int(data) > 3:
            raise ValueError(f"Maximum level is 3. You entered: {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.\n")
        return False
    return True


class Hangman:
    """
    Class that holds details to create and play the game.
    """
    def __init__(self, name, word):
        self.name = name
        self.word = [x for x in word]
        self.guesses = []  # Holds the guessed letters
        self.tries = 6
        self.secret_word = len(self.word)*["_"]
        # Takes the lenght of the word & place an: _ for every letter.

    def start_game(self):
        print(hangman_stages(self.tries))
        print(*self.secret_word)
        print(*self.guesses)

    def validate_guess(self, data):
        """
        Checks the guess of letter so it's not anything else than a letter,
        also checks if it is more or less than one letter.
        """
        try:
            if not data.isalpha():
                raise ValueError(
                    f"You can only guess letters. You guessed: {data}")
            if len(data) != 1:
                raise ValueError(
                    f"You can only guess one letter at a time."
                    f" You guessed: {data}")
            if data in self.guesses:
                raise ValueError(f"You already guessed: {data}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            return False
        return True

    def guess_letter(self):
        """
        If validate_guess function comes back as false player get to
        guess the letter again, otherwise the loop breaks.
        """
        while True:
            guess = input("Guess a letter: \n").upper()
            if self.validate_guess(guess):
                break
        self.guesses.append(guess)
        # Guessed letter goes into the list guesses
        self.check_letter(guess)
        # Calls the function check_letter with the input from the player

    def check_letter(self, data):
        """
        Checks if the guessed letter is in the word or not.
        Returns the index of the first item that is equal to data.
        """
        if data not in self.word:
            self.tries -= 1

        while data in self.word:
            i = self.word.index(data)
            self.secret_word[i] = data
            self.word[i] = "."
            print(*self.secret_word)

    def word_complete(self):
        """
        Checks if the word doesn't have any "_" in it.
        If so the word is completed, otherwise the player
        gets to keep on guessing.
        """
        if "_" not in self.secret_word:
            self.start_game()
            return True

    def check_tries(self):
        if self.tries <= 0:
            self.start_game()
            return True

    def play_again(self):
        while True:
            restart = input("Do you want to play again? (Y/N): \n").upper()
            if restart == "Y":
                return True
            if restart == "N":
                print("Thanks for playing!")
                return False
            else:
                print("Invalid choice. Please enter 'Y' or 'N'.")


def main():
    print(word_art.welcome)
    name = input("Enter your name: \n").capitalize()

    global rules_input
    global level_input
    global word_input

    """
    Gets input if player want's to read rules. Calls the function
    game_rules to either give rules or not.
    """
    while True:
        rules_input = input(
            f"Hello, {name}, do you want to read the rules? (Y/N): \n").upper()
        if game_rules(rules_input):
            break

    """
    Checks the validate_level function if True the while loop breaks.
    If False player get to choose level again.
    """
    while True:
        print("Choose a level between 1-3")
        level_input = input("Choose level: \n")
        if validate_level(level_input):
            break

    """
    Picks a list with random words choosed by
    player depending of level difficulty.
    """
    level_words = {
        "1": words_1,
        "2": words_2,
        "3": words_3
    }
    word_input = random.choice(level_words[level_input]).upper()

    player = Hangman(name, word_input)

    while True:  # Makes the game running until word is completed.
        player.start_game()
        player.guess_letter()
        if player.word_complete():
            print("You win!")
            break
        if player.check_tries():
            print("You lose!")
            break

    if player.play_again():
        main()


main()
