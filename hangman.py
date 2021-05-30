import random
import string

from images import IMAGES
from words import choose_word

'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    # print(letters_guessed)
    return all(ele in letters_guessed for ele in secret_word)
    # return True if len(secret_word) == len(letters_guessed) else False


# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for letter in letters_guessed:
        letters_left = letters_left.replace(letter, "")
    return letters_left


def hint(secret):
    print(f"One of the letter is:" + secret_word[random.randint(0, len(secret_word) - 1)])


hints = 1


def take_input():
    global hints
    guess = input("Please guess a letter: ")
    if guess == "hint":
        if hints > 0:
            hint(secret_word)
            hints -= 1
        else:
            print("Maximum number of hints are Used!")
        return take_input()
    elif not guess.isalpha() or len(guess) != 1:
        print("Please Enter a Valid Input!")
        return take_input()
    else:
        return guess


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!    ->" + secret_word)
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    print("you have 8 tries!")
    tries = 8
    letters_guessed = []
    while tries > 0:

        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        letter = take_input()

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed):
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print(IMAGES[8 - tries])
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            tries -= 1
            letters_guessed.append(letter)
        print("Tries Left : " + str(tries))
    if tries <= 0:
        print(f"Better Luck next time!\n The word Was: {secret_word}")


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
