import random
from words import words_1
from words import words_2
from words import words_3
from hangman_stages import hangman

def get_random_word():
    word = random.choice(list_of_words) #Get's a random word in uppercase
    return word.upper()

def main():
    print("Welcome player!")
    name = input("Enter your name: ").capitalize()
    print(name)

main()
