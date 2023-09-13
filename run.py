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
            raise ValueError(f"You need to enter a whole number. You entered {data}")
        if int(data) < 1:
            raise ValueError(f"Minimum lvl is 1. You entered {data}")
        if int(data) > 3:
            raise ValueError(f"Maximum lvl is 3. You entered {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        return False
    return True

class Hangman:
    """
    Class that holds details to create and play game.
    """
    def __init__(self, name, word):
        self.name = name
        self.word = word
        self.guesses = []
        self.tries = 6

    def start_game(self):
        print(f"Let's start the game {self.name}. Word to guess is\n{self.word}")
    
    
    def validate_guess(self, data):
        try:
            if not data.isalpha():
                raise ValueError(f"You can only enter letters. You entered {data}")
            if 



    def guess_letter(self):
        guess = input("Guess a letter: ")


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
    player.start_game()
    player.guess_letter()
main()
