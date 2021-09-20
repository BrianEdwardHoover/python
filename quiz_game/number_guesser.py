import random

upper_limit = input("Type a number greater than zero for the upper limit: ")
num_of_guesses = 0
if upper_limit.isdigit():
    upper_limit = int(upper_limit)
    if upper_limit < 0:
        print("We need a number greater than zero!")
        quit()
else:
    print("You did not provide us a number!")
    quit()

random_number = random.randint(0, upper_limit)

while True:
    guess = int(input("What is your guess? "))
    num_of_guesses += 1
    if guess == random_number:
        print(f"You guessed correctly, the number was: {random_number}")
        break
    elif guess < random_number:
        print("Your guess was too low.")
        continue
    else:
        print("Your guess was too high.")
        continue
    break

print(f"It took you {num_of_guesses} guesses.")