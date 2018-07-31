import random

def addElement(letters, capitalLetters, numbers, specialCharacters):
    character = random.randint(0, 3)
    element = None
    if character == 0:
        element = random.choice(letters)
    if character == 1:
        element = random.choice(capitalLetters)
    if character == 2:
        element = random.choice(numbers)
    if character == 3:
        element = random.choice(specialCharacters)
    return element

def structurePassword(passwordList, passwordWords):
    positionOfWord = random.randint(0, 1)
    password = None
    if positionOfWord == 0:
        password = passwordWords[random.randint(0, len(passwordWords)-1)] + "".join(passwordList)
    if positionOfWord == 1:
        password = "".join(passwordList) + passwordWords[random.randint(0, len(passwordWords)-1)]
    return password

def generate(passwordStrength):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    capitalLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789"
    specialCharacters = "@#$%-."

    passwordList = []
    password = None

    # Weak Passwords
    if passwordStrength == "W" or passwordStrength == "w" or passwordStrength == "weak" or passwordStrength == "Weak":

        passwordWords = ["password", "lazy", "user", "loza"]
        for i in range(random.randint(1, 2)):
            passwordList.append(addElement(letters, capitalLetters, numbers, specialCharacters))

        password = structurePassword(passwordList, passwordWords)

    # Moderate Passwords
    if passwordStrength == "M" or passwordStrength == "m" or passwordStrength == "moderate" or passwordStrength == "Moderate":
        specialCharacters += "_!^*:&"
        passwordWords = ["player", "child", "power", "powerful", "unbreakable"]
        for i in range(random.randint(2, 4)):
            passwordList.append(addElement(letters, capitalLetters, numbers, specialCharacters))

        password = structurePassword(passwordList, passwordWords)


    # Strong Passwords
    if passwordStrength == "S" or passwordStrength == "s" or passwordStrength == "Strong" or passwordStrength == "strong":
        specialCharacters += "|{}][?/<>+=,"
        passwordWords = ["paSswOrd", "uNbreaKaBlE", "uSeRheRE", "pOWerFUL"]

        for i in range(random.randint(2, 5)):
            passwordList.append(addElement(letters, capitalLetters, numbers, specialCharacters))

        password = structurePassword(passwordList, passwordWords)

    return password

passwordStrength = input("Enter how strong u want ur password to be: (W: Weak || M: Moderate || S: Strong) ")
password = generate(passwordStrength)
print("The password is", password)
