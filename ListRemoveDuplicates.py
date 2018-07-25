
def constructList():
    lenOfList = int(input("How long do u want the list to be?: "))
    list = []
    for i in range(lenOfList):
        element = int(input("Enter element " + str(i+1) + ": "))
        list.append(element)
    return list

list = constructList()
print("List without Duplicates: " + str(set(list)))
