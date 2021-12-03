def splitter(word):
    return [char for char in word]

inFile = open("3input.txt" , 'r')
binaries = inFile.read().split()
binaries2 = binaries.copy()
answer = -1
oneCount  = 0
zeroCount = 0
gammaString = ""
epsilonString = ""

for y in range(0, len(binaries[0])):
    oneCount  = 0
    zeroCount = 0
    for x in binaries:
        binary = splitter(x)
        if binary[y] == "1":
            oneCount += 1
        else:
            zeroCount += 1

    print(str(zeroCount) + " at " + str(y))
    print(str(oneCount) + " at " + str(y) + "\n")

    for z in range(0, len(binaries)):
        binary = splitter(binaries[z])
        if(len(binaries) == 1):
            break
        if oneCount < zeroCount and binary[y] == "1":
            binaries.remove(z)
        elif oneCount >= zeroCount and binary[y] == "0":
            binaries.remove(z)

    print(binaries)


print(len(binaries2))

for y in range(0, len(binaries2[0])):
    oneCount  = 0
    zeroCount = 0
    for x in binaries2:
        binary = splitter(x)
        if binary[y] == "1":
            oneCount += 1
        else:
            zeroCount += 1

    for z in binaries2:
        binary = splitter(z)
        if(len(binaries2) == 1):
            break
        if oneCount < zeroCount and binary[y] == "0":
            binaries2.remove(z)
        elif oneCount >= zeroCount and binary[y] == "1":
            binaries2.remove(z)

print(len(binaries))
print(len(binaries2))

gammaString = binaries[0]
epsilonString = binaries2[0]

print(gammaString)
print(epsilonString)

gamma = int(gammaString, 2)
epsilon = int(epsilonString, 2)

print(gamma)
print(epsilon)

answer = gamma * epsilon

print(answer)