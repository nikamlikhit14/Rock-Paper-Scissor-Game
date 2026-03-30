import random

# Options for the game
options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

while True:
    # User input
    user_choice = input("Your choice: ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Computer randomly selects an option
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
    
    print()  # Blank line for readability
