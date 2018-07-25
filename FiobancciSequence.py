
def generateSequence(noOfSeqeunces):
    fiobancciSequence = []
    no = 1
    for i in range(noOfSeqeunces):
        if i <= 1:
            fiobancciSequence.append(1)
        else:
            previousNo1 = fiobancciSequence[i-1]
            previousNo2 = fiobancciSequence[i-2]
            no = previousNo1 + previousNo2
            fiobancciSequence.append(no)

    return fiobancciSequence

noOfSeqeunces = int(input("How many sequences do you want to generate: "))
fiobancciSequence = generateSequence(noOfSeqeunces)
print("Sequence: " + str(fiobancciSequence))
