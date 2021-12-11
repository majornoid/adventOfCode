def splitter(word):
    return [char for char in word]

inFile = open("4input.txt" , 'r')
data = inFile.read().split()
calls = data[0].split(',')
answer = -1
currCall = -1
currBoard = -1
bingo = 0
unmarkedSum = 0

for x in calls:
  currCall = int(x)
  for i in range(1, len(data)):
    if int(data[i]) == currCall:
      data[i] = -1
  
  for i in range(1, len(data), 25):
    currBoard = i
    for j in range(i, i+5):
      for k in range(j, j+25, 5):
        if data[k] == -1:
          bingo += 1
      if bingo == 5:
        break
      bingo = 0

    if bingo == 5:
      break

    for j in range(i, i+25, 5):
      for k in range(j, j+5):
        if data[k] == -1:
          bingo += 1
      if bingo == 5:
        break
      bingo = 0
      
    if bingo == 5:
      break

  if bingo == 5:
    break

for y in range(currBoard, currBoard+25):
  if data[y] != -1:
    unmarkedSum += int(data[y])

answer = currCall * unmarkedSum

print(answer)