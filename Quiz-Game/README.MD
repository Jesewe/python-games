# Python quiz game

This is a simple quiz game written in Python. In the game, the user answers several questions, and then gets his final result.

## How to launch the game

1. Make sure Python is installed on your computer.
2. Download the `quiz_game.py` and save it on your computer.
3. Open a command prompt (in Windows) or a terminal (in macOS and Linux).
4. Navigate to the directory where the file is located `quiz_game.py` .
5. Start the game by entering the command: `python quiz_game.py `

## How to play the game

1. The quiz game will show the question to be answered.
2. Enter your answer and press Enter.
3. If your answer is correct, you will see the message "Correct!" and your score will increase by 1.
4. If your answer is incorrect, you will see the message "Incorrect!" and the correct answer.
5. The game will continue until you answer all the questions.
6. At the end of the game you will see your final result - the number of correct answers from the total number of questions.

## How to change questions

1. Open the file `quiz_game.py` in any text editor.
2. Change the list of questions in the questions variable. Each question is a list of two elements: the first element is the question, and the second element is the correct answer to the question.

```python
questions = [
    ["What is the capital of France?", "Paris"],
    ["What is the tallest mountain in the world?", "Mount Everest"],
    ["What is the largest country in the world by land area?", "Russia"],
    ["What is the smallest country in the world by land area?", "Vatican City"],
    ["What is the largest planet in the solar system?", "Jupiter"]
]
