import random
from words import words_1
from words import words_2
from words import words_3
from hangman_stages import hangman

def validate_lvl(data):
    """
    Validates the level the player choose.
    """
    try:
        if data.isalpha():
            raise ValueError(f"You need to enter a whole number. You entered: {data}")
        if int(data) < 1:
            raise ValueError(f"Minimum lvl is 1. You entered: {data}")
        if int(data) > 3:
            raise ValueError(f"Maximum lvl is 3. You entered: {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        return False
    return True


class Hangman:
    """
    Class that holds details to create and play the game.
    """
    def __init__(self, name, word):
        self.name = name
        self.word = word
        self.guesses = []  # Holds the guessed letters
        self.tries = 6 
        self.secret_word = len(self.word)*["_"] # Takes the lenght of the word & place an: _ for every letter.

    def start_game(self):
        print(f"Let's start the game {self.name}. Word to guess is\n{self.word}")
        print(self.secret_word)
        print(self.guesses)
    
    
    def validate_guess(self, data):
        """
        Checks the guess of letter so it's not anything else than a letter,
        also checks if it is more or less than one letter.
        """
        try:
            if not data.isalpha():
                raise ValueError(f"You can only guess letters. You guessed: {data}")
            if len(data) != 1:
                raise ValueError(f"You can only guess one letter at a time. You guessed: {data}")
        except ValueError as e:
            print("Invalid input: {e}. Please try again.")
            return False
        return True


    def guess_letter(self):
        """
        If validate_guess function comes back as false player get to guess the letter again, otherwise the loop breaks.
        """
        while True:
            guess = input("Guess a letter: ").upper()
            if self.validate_guess(guess):
                break
        self.guesses.append(guess) # Guessed letter goes into the list guesses
        self.check_letter(guess) # Calls the function check_letter with the input from the player

    def check_letter(self, data):
        """
        Checks if the guessed letter is in the word or not. 
        Returns the index of the first item that is equal to data.
        """
        if data in self.word:
            print("Correct")
            index = self.word.index(data)
            self.secret_word[index] = data
            print(self.secret_word)

        else:
            print("Incorrect")

    def word_complete(self):
        if "_" not in self.secret_word:
            return True


def main():
    print("Welcome to hangman!")
    name = input("Enter your name: ").capitalize()
    print(name)
    
    global lvl_input
    global word_input

    """
    Checks the validate_lvl function if True the while loop breaks. 
    If False player get to choose lvl again.
    """
    while True: 
        print("Choose a lvl between 1-3")
        lvl_input = input("Choose lvl: ")
        if validate_lvl(lvl_input): 
            break
    
    """ 
    Picks a list with random words choosed by player depending of lvl difficulty.
    """
    if lvl_input == "1":
        word_input = random.choice(words_1).upper()
    elif lvl_input == "2":
        word_input = random.choice(words_2).upper()
    elif lvl_input == "3":
        word_input = random.choice(words_3).upper()   

    player = Hangman(name, word_input) 
    while True:
        player.start_game()
        player.guess_letter()
        if player.word_complete():
            print("You win!")
            break


main()
