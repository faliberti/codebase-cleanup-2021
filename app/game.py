
from random import choice

#
# DETERMINATION OF WINNER
#


def determine_winner(u, c):

    win_options = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    win_choice = win_options[u]

    if (u == c):
        winner = "None"
        print("It's a tie!")
    elif (c == win_choice):
        winner = "User"
        print("The User Wins")
    else:
        winner = "Computer"
        print("The Computer Wins")

    return winner

#
# USER SELECTION
#


VALID_OPTIONS = ["rock", "paper", "scissors"]

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#


c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# FINAL RESULT
#


determine_winner(u, c)
