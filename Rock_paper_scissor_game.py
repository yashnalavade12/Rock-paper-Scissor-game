import random

def get_user_choice():
    print("Let's play Rock, Paper, Scissors!")
    user_input = input("Your move (rock/paper/scissors): ").strip().lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Oops! That's not a valid choice.")
        user_input = input("Try again (rock/paper/scissors): ").strip().lower()
    return user_input

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def determine_winner(player, computer):
    if player == computer:
        return "It's a draw!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You got it! You win! 🎉"
    else:
        return "Ahh, the computer wins this time."

def play():
    player_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {player_choice}")
    print(f"The computer picked: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play()
