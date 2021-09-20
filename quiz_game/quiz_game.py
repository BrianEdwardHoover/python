print("Welcome to my computer quiz!")

questions_answers = {
    "What does CPU stand for? ": "central processing unit",
    "What type of computer do you have? ": "mac"
}
score = 0
for question, answer in questions_answers.items():
    if input(question) == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The right answer was: {answer}")

print(f"You're final score was: {score}")
