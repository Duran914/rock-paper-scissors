import random

# while loop to play again
playAgain = ""

# message content
message = ""
while playAgain != "N":

    #user input
    print("---Lets play Rock, Paper, Scissors---\nType R for rock, P for paper, S for Scissors")

    userPick = input("Enter your choice: ").upper()

    # Choices Array
    choices = ["R", "P" , "S"]

    computerPick = random.choice(choices)

    if userPick == computerPick:
        print("It's a Tie!")
    elif userPick == "R" and computerPick == "P":
        message = "You lose!, paper covers rock."
    elif userPick == "R" and computerPick == "S":
        message = "You win! Rock breaks scissors!"
    elif userPick == "P" and computerPick == "R":
        message = "You win! Paper covers rock!"
    elif userPick == "P" and computerPick == "S":
        message = "You lose!, Scissors cuts paper."
    elif userPick == "S" and computerPick == "P":
        message = "You win! Scissors cuts paper."
    elif userPick == "S" and computerPick == "R":
        message = "You lose!, Rock breaks scissors"
    else:
        message = "Unvaild choice"
    print (f"You chose {userPick} The computer chose {computerPick} \n{message}")

    playAgain = input("Play again(Y/N)?").upper()

# Ended game
print ("GoodBye!")
