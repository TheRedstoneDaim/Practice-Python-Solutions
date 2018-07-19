import random
import time

print("Welcome to the guessing game!!")
time.sleep(0.2)
print("The computer will guess a number between 1-9")
print("And its ur job to guess the number (NO SECOND CHANCES)")
time.sleep(0.4)
print("The game will continue until you type 'exit'")
time.sleep(0.3)

guessesRight = 0
totalGuesses = 0

def play():
    randomNo = random.randint(1, 9)
    time.sleep(0.5)

    try:
        userNo = int(input("The Computer has chose its number. Enter what u think it is: "))
        if userNo == randomNo:
           print("Congratz the number was: " + str(randomNo))
           global guessesRight
           guessesRight += 1

        if userNo > 9 or userNo < 1:
           print("The number, " + str(userNo) + " isn't between 1-9!!!")
           return False

        if userNo < randomNo:
           diff = randomNo - userNo
           print("The number was " + str(diff) + " higher than your guess")
           time.sleep(0.2)
           print("the number was: " + str(randomNo))

        if userNo > randomNo:
           diff = userNo - randomNo
           print("The number was " + str(diff) + " lower than your guess")
           time.sleep(0.2)
           print("the number was: " + str(randomNo))

        global totalGuesses
        totalGuesses += 1
        return False

    except ValueError:
        sureYouWantToExit = input("Are you sure u want to exit?(Y/N)")
        if sureYouWantToExit == "Y" or sureYouWantToExit == "y" or sureYouWantToExit == "yes" or sureYouWantToExit == "yes":
           return True
        else:
           return False

global stop
stop = False
while stop == False:
    stop = play()

time.sleep(1)
print("Thanks for Playing")
time.sleep(0.5)
print("You got " + str(guessesRight) + " guesse(s) right out of " + str(totalGuesses) + " guesse(s)")
