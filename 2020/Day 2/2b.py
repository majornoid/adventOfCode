inFile = open("2input.txt", 'r')
data = inFile.read().replace('-', ' ').replace(': ', ' ').split()
solution = 0
pos1 = -1
pos2 = -1
testChar = ''
testPass = ""


for x in range(0, len(data)):
  if x % 4 == 0:
    pos1 = int(data[x])
  elif x % 4 == 1:
    pos2 = int(data[x])
  elif x % 4 == 2:
    testChar = data[x]
  else:
    testPass = data[x]
    charCounter = 0
    currPos = 0
    for y in testPass:
      currPos += 1
      if y == testChar and (currPos == pos1 or currPos == pos2):
        charCounter += 1
    if charCounter == 1:
      solution += 1
print(solution)