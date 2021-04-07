
# import some code
from app.game import determine_winner

# test the code
def test_determine_winner():

    # If user input is rock
    assert determine_winner("rock" , "rock") == "None"
    assert determine_winner("rock", "paper") == "Computer"
    assert determine_winner("rock", "scissors") == "User"

    # If user input is paper
    assert determine_winner("paper" ,"rock") == "User"
    assert determine_winner("paper", "paper") == "None"
    assert determine_winner("paper", "scissors") == "Computer"

    # If user input is scissors
    assert determine_winner("scissors" ,"rock") == "Computer"
    assert determine_winner("scissors", "paper") == "User"
    assert determine_winner("scissors", "scissors") == "None"