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
        if data < 1:
            raise ValueError(f"Minimum lvl is 1. You entered {data}")
        if data > 3:
            raise ValueError(f"Maximum lvl is 3. You entered {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

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


"""
def get_random_word():
    word = random.choice(list_of_words) #Get's a random word in uppercase
    return word.upper()
"""

def main():
    print("Welcome to hangman!")
    name = input("Enter your name: ").capitalize()
    print(name)

    while True:
        print("Choose a lvl between 1-3")
        lvl_input = input("Choose lvl: ")
        if validate_lvl(lvl_input):
            break

main()
