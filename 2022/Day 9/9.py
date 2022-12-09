inFile = open("input.txt" , 'r')
numbers = inFile.read().split("\n")
numbers = [i.split(' ') for i in numbers]
#numbers = [i.replace('-',',').split(',') for i in numbers]
answer = 0
#print(numbers)

grid = [ ['']*400 for i in range(400)]

currH = [200, 200]
currT = [200, 200]

grid[200][200] = '#'

for command in numbers:
  axis = -1
  mod = 0
  if command[0] == 'U':
    axis = 0
    mod = -1
  elif command[0] == 'D':
    axis = 0
    mod = 1
  elif command[0] == 'L':
    axis = 1
    mod = -1
  elif command[0] == 'R':
    axis = 1
    mod = 1

  for i in range(int(command[1])):
    currH[axis] += mod

    xDiff = currH[0] - currT[0]
    yDiff = currH[1] - currT[1]

    #print(xDiff, yDiff, currT, currH)

    if xDiff > 1 or (xDiff > 0 and (yDiff > 1 or yDiff < -1)):
      currT[0] += 1
    elif xDiff < -1 or (xDiff < 0 and (yDiff > 1 or yDiff < -1)):
      currT[0] -= 1
    if yDiff > 1 or (yDiff > 0 and (xDiff > 1 or xDiff < -1)):
      currT[1] += 1
    elif yDiff < -1 or (yDiff < 0 and (xDiff > 1 or xDiff < -1)):
      currT[1] -= 1

    grid[currT[0]][currT[1]] = '#'
  

for row in grid:
  #if '#' in row:
  #  print(row)
  for space in row:
    if space == '#':
      answer += 1

print(answer)