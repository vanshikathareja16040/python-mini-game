import random


def play_sps(user_choice):
    choices = ["stone", "paper", "scissors"]
    computer = random.choice(choices)

    print(f"\nComputer chose: {computer}")

    if user_choice == computer:
        print("Draw!")

    elif (user_choice == "stone" and computer == "scissors") or \
         (user_choice == "paper" and computer == "stone") or \
         (user_choice == "scissors" and computer == "paper"):
        print("You Win!")

    else:
        print("Computer Wins!")



def roll_dice():
    user = random.randint(1, 6)
    computer = random.randint(1, 6)

    print(f"\nYou rolled: {user}")
    print(f"Computer rolled: {computer}")

    if user > computer:
        print("You Win!")
    elif user < computer:
        print("Computer Wins!")
    else:
        print("Draw!")