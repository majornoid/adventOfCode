def splitter(word):
    return [char for char in word]

inFile = open("4input.txt" , 'r')
data = inFile.read().split('\n\n')
boards = []
calls = data[0].split(',')
answer = -1
currCall = -1
currBoard = []
finalBoard = []
bingo = 0
unmarkedSum = 0

for z in range(1, len(data)):
  boards.append(data[z].split())

for x in calls:
  currCall = int(x)

  i = 0
  while True:
    if i >= len(boards):
      break
    currBoard = boards[i]

    for l in range(0, len(currBoard)):
      if int(currBoard[l]) == currCall:
        currBoard[l] = -1

    for j in range(0, 5):
      for k in range(j, j+25, 5):
        if currBoard[k] == -1:
          bingo += 1
      if bingo == 5:
        break
      bingo = 0

    if bingo == 5:
      bingo = 0
      #print("Bingo on Board:" + str(i))
      finalBoard = boards[0]
      boards.pop(i)
      continue

    for j in range(0, 25, 5):
      for k in range(j, j+5):
        if currBoard[k] == -1:
          bingo += 1
      if bingo == 5:
        break
      bingo = 0
      
    if bingo == 5:
      bingo = 0
      #print("Bingo on Board:" + str(i))
      finalBoard = boards[0]
      boards.pop(i)
      continue
    i += 1

  if len(boards) <= 0:
    break



#print(finalBoard)
#print(currCall)
for y in range(0, len(finalBoard)):
  if finalBoard[y] != -1:
    unmarkedSum += int(finalBoard[y])

answer = currCall * unmarkedSum

print(answer)