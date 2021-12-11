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
        if debugCounter < 500:
          print("Before: (" + str(x1) + ", " + str(i) + "): " + str(graph[x1][i]))
        graph[x1,i] += 1
        if debugCounter < 500:
          print("After: (" + str(x1) + ", " + str(i) + "): " + str(graph[x1][i]))
          debugCounter += 1
    else:
      for i in range(y2, y1+1):
        if debugCounter < 0:
          print("Before (" + str(x1) + ", " + str(i) + "): " + str(graph[x1][i]))
        graph[x1,i] += 1
        if debugCounter < 0:
          print("After (" + str(x1) + ", " + str(i) + "): " + str(graph[x1][i]))
          debugCounter += 1
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



for x in range(1000):
  for y in range(1000):
    if graph[x,y] > 1:
      answer += 1

print(answer)