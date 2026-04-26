import logic

while True:
    print("""
 GAME MENU
1. Stone-Paper-Scissors
2. Dice Roll Game
3. Exit

""")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_input = input("Enter stone/paper/scissors: ").lower()

        if user_input in ["stone", "paper", "scissors"]:
            logic.play_sps(user_input)
        else:
            print("Invalid input!")

    elif choice == "2":
        logic.roll_dice()

    elif choice == "3":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice! Try again.")
