import random


def play_game():
    print("Let's play a game of Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]

    # Ensure valid input for the number of rounds
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? "))
            if rounds > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for round_num in range(1, rounds + 1):
        # Ensure valid input for rock, paper, or scissors
        while True:
            user_choice = input(f"Round {round_num}: Enter rock, paper, or scissors: ").lower()
            if user_choice in choices:
                break
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

        bot_choice = random.choice(choices)
        if user_choice == bot_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and bot_choice == "scissors") or (
                user_choice == "scissors" and bot_choice == "paper") or (
                user_choice == "paper" and bot_choice == "rock"):
            result = "You win!"
        else:
            result = "You lose!"

        print(f"Bot chose {bot_choice}. {result}")


# Call the function to play the game
play_game()
