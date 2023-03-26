def play_quiz(questions):
    score = 0
    total = len(questions)
    for question in questions:
        print(question[0])
        answer = input().strip().lower()
        if answer == question[1].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect! The correct answer is:", question[1])
        print()
    print("You got", score, "out of", total, "correct!")

if __name__ == '__main__':
    questions = [
        ["What is the capital of France?", "Paris"],
        ["What is the tallest mountain in the world?", "Mount Everest"],
        ["What is the largest country in the world by land area?", "Russia"],
        ["What is the smallest country in the world by land area?", "Vatican City"],
        ["What is the largest planet in the solar system?", "Jupiter"]
    ]
    play_quiz(questions)
