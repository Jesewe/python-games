import random

words = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'watermelon', 'grape']

def choose_word(words):
    return random.choice(words)

def hangman(word):
    lives = 6
    correct_guesses = []
    incorrect_guesses = []
    hidden_word = "_" * len(word)
    while lives > 0:
        print("Lives left:", lives)
        print("Word:", hidden_word)
        print("Correct guesses:", correct_guesses)
        print("Incorrect guesses:", incorrect_guesses)
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only one letter!")
            continue
        if not guess.isalpha():
            print("Please enter a letter!")
            continue
        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter!")
            continue
        if guess in word:
            print("Correct!")
            correct_guesses.append(guess)
            hidden_word = ""
            for letter in word:
                if letter in correct_guesses:
                    hidden_word += letter
                else:
                    hidden_word += "_"
            if hidden_word == word:
                print("Congratulations! You guessed the word:", word)
                return
        else:
            print("Incorrect!")
            incorrect_guesses.append(guess)
            lives -= 1
    print("You lost! The word was:", word)

word = choose_word(words)
hangman(word)
