import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        print(f"You did not pick a valid choice, you typed: {user_input}")
        continue

    random_number = random.randint(0,2)
    # 0 = rock
    # 1 = paper
    # 2 = scissors
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print(f"You won! The computer picked {computer_pick}")
        user_wins += 1
        continue
    elif user_input == 'paper' and computer_pick == 'rock':
        print(f"You won! The computer picked {computer_pick}")
        user_wins += 1
        continue
    elif user_input == 'scissors' and computer_pick == 'paper':
        print(f"You won! The computer picked {computer_pick}")
        user_wins += 1
        continue
    else:
        print(f"You lost! The computer picked {computer_pick}")
        computer_wins += 1
        continue

print(f"The final score was user: {user_wins} vs computer: {computer_wins}.")
print("Goodbye!")

