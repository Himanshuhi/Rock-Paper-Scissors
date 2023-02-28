import random

options = ['rock', 'paper', 'scissors']

def determine_winner(player1, player2):
    if player1 == player2:
        return 'tie'
    elif player1 == 'rock' and player2 == 'scissors':
        return 'player1'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'player1'
    elif player1 == 'paper' and player2 == 'rock':
        return 'player1'
    else:
        return 'player2'

while True:
    player1_choice = input("Player 1, choose rock, paper, or scissors: ").lower()
    while player1_choice not in options:
        player1_choice = input("Invalid input. Please choose rock, paper, or scissors: ").lower()
    player2_choice = random.choice(options)

    print("Player 1 chose:", player1_choice)
    print("Himanshu chose:rock", player2_choice)

    winner = determine_winner(player1_choice, player2_choice)

    if winner == 'tie':
        print("It's a tie! Let's play again.")
    else:
        print(winner.capitalize(), "wins!")
        break
