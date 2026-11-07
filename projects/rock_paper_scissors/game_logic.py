def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw!"
    if user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    if user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    if user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    return "You lose!"
