import random

def randomize():
    list = []
    lengthOfList = random.randint(1, 10)
    for i in range(lengthOfList):
        randomNumber = random.randint(0, 1000)
        list.append(randomNumber)
    return list


def findLastElement(list):
    lastElement = None
    for i in range(len(list)):
        if i == len(list)-1:
            lastElement = list[i]
    return lastElement

a = randomize()
print("Original list: " + str(a))
print("First Element: " + str(a[0]))
print("Last Element: " + str(findLastElement(a)))
