import random
import time

playerPoints = 0
computerPoints = 0

def playMove():
    move = random.randint(0, 2)
    return move

def judgeMove(playerMove, pcMove):
    #0: Rock
    #1: Paper
    #2: Scissor

    if pcMove == 0:
        print("Computer played ROCK")
    if pcMove == 1:
        print("Computer played PAPER")
    if pcMove == 2:
        print("Computer played SCISSOR")
    time.sleep(0.35)

    if playerMove == 0:
        print("You played ROCK")
    if playerMove == 1:
        print("You played PAPER")
    if playerMove == 2:
        print("You played SCISSOR")
    time.sleep(0.35)

    if pcMove == playerMove:
        print("Its a draw")
        return None

    if pcMove == 0 and playerMove == 1:
        print("Computer loses. Player gained point")
        return True

    if pcMove == 0 and playerMove == 2:
        print("Player losses. Computer gains point")
        return False

    if pcMove == 1 and playerMove == 0:
        print("Player losses. Computer gains point")
        return False

    if pcMove == 1 and playerMove == 2:
        print("Computer loses. Player gains point")
        return True

    if pcMove == 2 and playerMove == 0:
        print("Computer loses. Player gains point")
        return True

    if pcMove == 2 and playerMove == 1:
        print("Player loses. Computer gains point")
    time.sleep(0.5)

def updatePoints(win):
    global playerPoints
    global computerPoints

    if win == True:
        playerPoints += 1
    if win == False:
        computerPoints += 1

def checkIfValid(input):
    if input < 0 or input > 2:
        print("Please enter the values 0(ROCK), 1(PAPER) or 2(SCISSORS)!!")
        playRound()

def play():
    print("Welcome to ROCK-PAPER-SCISSORS!!!")
    time.sleep(1)
    noOfRounds = int(input("Please enter the number of rounds you want to play: "))

    time.sleep(1)
    print("Enter 0 for ROCK; 1: PAPER; 2: SCISSOR")
    for i in range(noOfRounds):
        playRound()

def playRound():
    try:
       time.sleep(0.5)
       pcMove = playMove()

       playerMove = int(input("Enter your move(IN NUMBER FORM): "))

       checkIfValid(playerMove)
       win = judgeMove(playerMove, pcMove)
       updatePoints(win)
    except ValueError:
        print("Please enter the values 0(ROCK), 1(PAPER) or 2(SCISSORS)!!")
        playRound()


play()

time.sleep(0.5)
if playerPoints > computerPoints:
    print("===========================================")
    print("Congratz u win!!!")
    print("Your score: " + str(playerPoints))
    print("Computer Score: " + str(computerPoints))
    print("===========================================")

if playerPoints < computerPoints:
    print("===========================================")
    print("Sorry the computer won. U can always try again :)")
    print("Your score: " + str(playerPoints))
    print("Computer Score: " + str(computerPoints))
    print("===========================================")
if playerPoints == computerPoints:
    print("===========================================")
    print("Its a DRAW!! Close fight ;)")
    print("Score: " + str(playerPoints))
    print("===========================================")

playAgain = input("Do you want to play again(Y/N)")
if playAgain == "Y" or playAgain == "y" or playAgain == "yes" or playAgain == "Yes":
    time.sleep(0.3)
    play()
else:
    time.sleep(0.3)
    print("Thx for playing have a good day :)")
 
