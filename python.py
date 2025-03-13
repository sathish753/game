import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = None

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")

    while player_choice not in choices:
        player_choice = input("Your choice: ").lower()

    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors()
