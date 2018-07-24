
def checkIfPrime(number):
    for i in range(number):
        if i > 1 and number != i and number % i == 0:
           return False
        if number == 1 or number == 0:
            return False
    return True

numberToBeChecked = int(input("Enter the number, which u wanna check is prime: "))
isPrime = checkIfPrime(numberToBeChecked)

if isPrime == True:
    print("The number " + str(numberToBeChecked) + " is prime")
else:
    print("The number " + str(numberToBeChecked) + " isn't prime")
