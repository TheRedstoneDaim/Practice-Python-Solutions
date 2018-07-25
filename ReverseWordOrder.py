
def reverse(string):
    list = string.split()
    reversedList = []
    a = len(list) - 1
    for i in range(len(list)):
        reversedList.append(list[a])
        a -= 1
    reversedString = " ".join(reversedList)
    return reversedString

try:
    string = input("Please enter a string with multiple words: ")
    reversedString = reverse(string)
    print(reversedString)
except ValueError:
    print("Pls enter a string not number! Restart and try again!!")
    
