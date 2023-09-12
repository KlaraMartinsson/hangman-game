import random
from words import words_1
from words import words_2
from words import words_3
from hangman_stages import hangman

class Hangman:
    """
    Class that holds details to create and play game.
    """
    def __init__(self, name, word):
        self.name = name
        self.word = word
        self.guesses = []
        self.tries = 6

"""
def get_random_word():
    word = random.choice(list_of_words) #Get's a random word in uppercase
    return word.upper()
"""

def main():
    print("Welcome player!")
    name = input("Enter your name: ").capitalize()
    print(name)

main()
