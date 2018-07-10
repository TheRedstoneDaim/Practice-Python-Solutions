palindrome = input("Enter the word, which you want to check is a palindrome: ")
palindromeList = []
reversedWord = []

for c in palindrome:
    palindromeList.append(c)

i = len(palindromeList) - 1
while i != 0:
    reversedWord.append(palindromeList[i])
    i -= 1
reversedWord.append(palindromeList[0])

if reversedWord == palindromeList:
    print("This word is a palindrome")
else:
    print("This word isn't a palindrome")

# Question from: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
