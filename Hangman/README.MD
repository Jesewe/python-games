# Hangman Game

This is a simple implementation of the classic Hangman game in Python. The game selects a random word from a list of words, and the player has to guess the word one letter at a time. The player has a limited number of lives, and each incorrect guess reduces the number of lives. The game continues until the player either guesses the word correctly or runs out of lives.

## How to Run

1. Make sure you have Python 3.x installed on your system.
2. Save the provided code in a file named `hangman.py`.
3. Open a terminal or command prompt and navigate to the directory containing the `hangman.py` file.
4. Run the following command: `python hangman.py`
5. Follow the on-screen instructions to play the game.

## Game Instructions

1. The game will display the number of lives left, the current state of the hidden word, and the correct and incorrect guesses made so far.
2. You will be prompted to guess a letter.
3. Enter a single letter and press Enter.
   - If you enter more than one letter or a non-letter character, you will be asked to enter a valid letter.
   - If you enter a letter that you have already guessed, you will be informed that you have already guessed that letter.
4. If your guess is correct, the hidden word will be updated to reveal the guessed letter(s).
5. If your guess is incorrect, you will lose a life.
6. The game continues until you either guess the word correctly or run out of lives.

## Example

```
Lives left: 6
Word: ______
Correct guesses: []
Incorrect guesses: []
Guess a letter: a

Correct!
Lives left: 6
Word: _a____
Correct guesses: ['a']
Incorrect guesses: []
Guess a letter: e

Incorrect!
Lives left: 5
Word: _a____
Correct guesses: ['a']
Incorrect guesses: ['e']
Guess a letter: i
```

Good luck and have fun playing Hangman!
