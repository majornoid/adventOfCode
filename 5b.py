def splitter(word):
    return [char for char in word]

answer = 0
debugCounter = 500

inFile = open("5input.txt" , 'r')
lines = []
graph = {}
lineStrings = inFile.read().replace(','," ").replace(' -> '," ").split("\n")
lineStrings.remove('')
for x in range(0, len(lineStrings)):
  lines.append(lineStrings[x].split())

for x in range(1000):
  for y in range(1000):
    graph[x,y] = 0

for l in lines:
  x1 = int(l[0])
  y1 = int(l[1])
  x2 = int(l[2])
  y2 = int(l[3])
  if x1 == x2:
    print("Vertical! from (" + str(x1) + ", " + str(y1) + ") to (" + str(x2) + ", " + str(y2) + ")")
    if y1 < y2:
      for i in range(y1, y2+1):
        graph[x1,i] += 1
    else:
      for i in range(y2, y1+1):
        graph[x1,i] += 1

  elif y1 == y2:
    #print("Horizontal! from (" + str(x1) + ", " + str(y1) + ") to (" + str(x2) + ", " + str(y2) + ")")
    if x1 < x2:
      for i in range(x1, x2+1):
        print('', end='')
        graph[i,y1] += 1
    else:
      for i in range(x2, x1+1):
        print('', end='')
        graph[i,y1] += 1

  elif abs(y2 - y1) == abs(x2 - x1):
    stepX = 0
    stepY = 0
    currX = x1
    currY = y1

    if x1 < x2:
      stepX = 1
    else:
      stepX = -1

    if y1 < y2:
      stepY = 1
    else:
      stepY = -1

    for i in range(abs(y2 - y1)+1):
      graph[currX,currY] += 1
      currX += stepX
      currY += stepY





for x in range(1000):
  for y in range(1000):
    if graph[x,y] > 1:
      answer += 1

print(answer)