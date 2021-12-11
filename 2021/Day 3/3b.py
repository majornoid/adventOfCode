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

    z = 0
    while z < len(binaries):
        if z < 0:
            z = 0
        if z >= len(binaries):
            break
        binary = splitter(binaries[z])
        if(len(binaries) == 1):
            break
        if oneCount < zeroCount and binary[y] == "1":
            binaries.remove(binaries[z])
        elif oneCount >= zeroCount and binary[y] == "0":
            binaries.remove(binaries[z])
        else:
            z += 1

for y in range(0, len(binaries2[0])):
    oneCount  = 0
    zeroCount = 0
    for x in binaries2:
        binary = splitter(x)
        if binary[y] == "1":
            oneCount += 1
        else:
            zeroCount += 1

    z = 0
    while z < len(binaries2):
        if z < 0:
            z = 0
        if z >= len(binaries2):
            break
        binary = splitter(binaries2[z])
        if(len(binaries2) == 1):
            break
        if oneCount < zeroCount and binary[y] == "0":
            binaries2.remove(binaries2[z])
        elif oneCount >= zeroCount and binary[y] == "1":
            binaries2.remove(binaries2[z])
        else:
            z += 1


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