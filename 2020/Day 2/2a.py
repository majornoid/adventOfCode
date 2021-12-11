inFile = open("2input.txt", 'r')
data = inFile.read().replace('-', ' ').replace(': ', ' ').split()
solution = 0
minRange = -1
maxRange = 1
testChar = ''
testPass = ""


for x in range(0, len(data)):
  if x % 4 == 0:
    minRange = int(data[x])
  elif x % 4 == 1:
    maxRange = int(data[x])
  elif x % 4 == 2:
    testChar = data[x]
  else:
    testPass = data[x]
    charCounter = 0
    for y in testPass:
      if y == testChar:
        charCounter += 1
    if charCounter >= minRange and charCounter <= maxRange:
      solution += 1
print(solution)