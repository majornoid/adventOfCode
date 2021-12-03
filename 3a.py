def splitter(word):
    return [char for char in word]

inFile = open("3input.txt" , 'r')
binaries = inFile.read().split()
answer = -1
oneCounts  = [0] * len(binaries[0])
zeroCounts = [0] * len(binaries[0])
gammaString = ""
epsilonString = ""

for x in binaries:
    binary = splitter(x)
    for y in range(0, len(binary)):
        if binary[y] == "1":
            oneCounts[y] += 1
        else:
            zeroCounts[y] += 1

for z in range(0, len(oneCounts)):
    if oneCounts[z] > zeroCounts[z]:
        gammaString += "1"
        epsilonString += "0"
    else:
        gammaString += "0"
        epsilonString += "1"

gamma = int(gammaString, 2)
epsilon = int(epsilonString, 2)

answer = gamma * epsilon

print(answer)