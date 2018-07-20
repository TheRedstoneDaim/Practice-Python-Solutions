import random

def randomize():
    list = []
    randomLength = random.randint(1, 10)
    for i in range(randomLength):
        randomNo = random.randint(0, 500)
        list.append(randomNo)
    return list

def checkForDuplicates(element):
    for i in range(len(commonElements)):
        if element == commonElements[i]:
            return True
    return False

a = randomize()
b = randomize()
commonElements = []

for i in range(len(a)):
    for i2 in range(len(b)):
        if a[i] == b[i2]:
            duplicates == checkForDuplicates(b[i2])
            if duplicates == False:
               commonElements.append(a[i])

if commonElements == []:
    print("No common elements were found")
else:
    print("The common element(s) are " + ", ".join(map(str, commonElements)))

print(str(a))
print(str(b))
