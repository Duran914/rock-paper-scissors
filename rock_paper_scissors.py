import random

# game messages
rockBeatScissors = "You win! Rock breaks scissors!"
paperBeatRock = "You win! Paper covers rock!"
ScissorsBeatPaper = "You win! Scissors cuts paper."

rockLossToPaper = "Sorry, Paper covers rock."
paperLossToScissors = "Sorry, Scissors cuts paper."
scissorsLossToRock = "Sorry, Rock breaks scissors"

tie = "It's a Tie!"
unvailed = "Unvaild choice"

# while loop to play again
playAgain = ""

while playAgain != "N":

    #user input
    print "---Lets play Rock, Paper, Scissors---\nType R for rock, P for paper, S for Scissors"

    userPick = raw_input("Enter your choice: ").upper()

    # Array
    choices = ["R", "P" , "S"]

    computerPick = random.choice(choices)

    print "You chose " + userPick + " The computer chose " + computerPick

    if userPick == computerPick:
        print tie
    elif userPick == "R" and computerPick == "P":
        print rockLossToPaper
    elif userPick == "R" and computerPick == "S":
        print rockBeatScissors
    elif userPick == "P" and computerPick == "R":
        print paperBeatRock
    elif userPick == "P" and computerPick == "S":
        print paperLossToScissors
    elif userPick == "S" and computerPick == "P":
        print ScissorsBeatPaper
    elif userPick == "S" and computerPick == "R":
        print scissorsLossToRock
    else:
        print "Unvaild choice"

    playAgain = raw_input("Play again(Y/N)?").upper()
    print "\n"

# Ended game
print "GoodBye!"
