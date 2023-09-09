import random
from words import list_of_words

def get_random_word():
    word = random.choice(list_of_words) #Get's a random word in uppercase
    return word.upper()