import random
from words import *
import string

topic = input("What topic do you chose?\nfor CSS type 'c' \nfor HTML type 'h' \nfor JavaScript type 'j'\n")
words_list = []
match topic:
    case "j":
       words_list = javascript_words
    case "c":
        words_list = css_words
    case "h":
        words_list = html5_words
    case _:
       words_list = general_words


def get_valid_word(words_list):
    word = random.choice(words_list)
    while "-" in word or " " in word:
        word = random.choice(words_list)
    return word.upper()    

def hangman():
    word = get_valid_word(words_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print(words_list[0].upper()," list")
        print("You have used these letters: ", " ".join(sorted(used_letters)))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", "".join(word_list))

        user_letter = input ("Guess a letter:\n").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives = lives - 1
                print("\nYour letter,", user_letter, "is not in the word.")    
    
        elif user_letter in used_letters:
            print (f"\nYou have already used this letter {user_letter}!")
        else:
            print ("Invalid character. Please try again")   
    if lives == 0:
        print("You died, sorry. the word was", word)
    else:
        print("Great!! you guessed it correctly, it is", word, "!!")            

hangman()
