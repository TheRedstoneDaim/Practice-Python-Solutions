import random

def generate(passwordStrength):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    capitalLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789"
    specialCharacters = "@#$%-."

    passwordList = []
    password = None

    # Weak Passwords
    if passwordStrength == "W" or passwordStrength == "w" or passwordStrength == "weak" or passwordStrength == "Weak":

        passwordWords = ["password", "unbreakable", "user", "powerful"]
        for i in range(random.randint(1, 2)):
            character = random.randint(0, 3)
            if character == 0:
                passwordList.append(random.choice(letters))
            if character == 1:
                passwordList.append(random.choice(capitalLetters))
            if character == 2:
                passwordList.append(random.choice(numbers))
            if character == 3:
                passwordList.append(random.choice(specialCharacters))

        positionOfWord = random.randint(0, 1)
        if positionOfWord == 0:
            password = passwordWords[random.randint(0, 3)] + "".join(passwordList)
        if positionOfWord == 1:
            password = "".join(passwordList) + passwordWords[random.randint(0, 3)]

    # Moderate Passwords
    if passwordStrength == "M" or passwordStrength == "m" or passwordStrength == "moderate" or passwordStrength == "Moderate":
        specialCharacters += "_!^*:&"
        passwordWords = ["player", "child", "power", "loza", "lazy"]
        for i in range(random.randint(2, 4)):
            character = random.randint(0, 3)
            if character == 0:
                passwordList.append(random.choice(letters))
            if character == 1:
                passwordList.append(random.choice(capitalLetters))
            if character == 2:
                passwordList.append(random.choice(numbers))
            if character == 3:
                passwordList.append(random.choice(specialCharacters))

        positionOfWord = random.randint(0, 1)
        if positionOfWord == 0:
            password = passwordWords[random.randint(0, 4)] + "".join(passwordList)
        if positionOfWord == 1:
            password = "".join(passwordList) + passwordWords[random.randint(0, 4)]


    # Strong Passwords
    if passwordStrength == "S" or passwordStrength == "s" or passwordStrength == "Strong" or passwordStrength == "strong":
        specialCharacters += "|{}][?/<>+=,"
        passwordWords = ["paSswOrd", "uNbreaKaBlE", "uSeRheRE", "pOWerFUL"]

        for i in range(random.randint(2, 5)):
            character = random.randint(0, 3)
            if character == 0:
                passwordList.append(random.choice(letters))
            if character == 1:
                passwordList.append(random.choice(capitalLetters))
            if character == 2:
                passwordList.append(random.choice(numbers))
            if character == 3:
                passwordList.append(random.choice(specialCharacters))

        positionOfWord = random.randint(0, 1)
        if positionOfWord == 0:
            password = passwordWords[random.randint(0, 3)] + "".join(passwordList)
        if positionOfWord == 1:
            password = "".join(passwordList) + passwordWords[random.randint(0, 3)]

    return password

passwordStrength = input("Enter how strong u want ur password to be: (W: Weak || M: Moderate || S: Strong) ")
password = generate(passwordStrength)
print("The password is", password)
