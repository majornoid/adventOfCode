inFile = open("input.txt" , 'r')
numbers = inFile.read().split("\n")
numbers = [i.split(' ') for i in numbers]
#numbers = [i.replace('-',',').split(',') for i in numbers]
answer = 0

grid = [ ['']*400 for i in range(400)]
knots = [ [200, 200] for i in range(10) ]


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
    knots[0][axis] += mod

    for i in range(1, len(knots)):
      xDiff = knots[i-1][0] - knots[i][0]
      yDiff = knots[i-1][1] - knots[i][1]

      #print(xDiff, yDiff, currT, currH)

      if xDiff > 1 or (xDiff > 0 and (yDiff > 1 or yDiff < -1)):
        knots[i][0] += 1
      elif xDiff < -1 or (xDiff < 0 and (yDiff > 1 or yDiff < -1)):
        knots[i][0] -= 1
      if yDiff > 1 or (yDiff > 0 and (xDiff > 1 or xDiff < -1)):
        knots[i][1] += 1
      elif yDiff < -1 or (yDiff < 0 and (xDiff > 1 or xDiff < -1)):
        knots[i][1] -= 1

    grid[knots[9][0]][knots[9][1]] = '#'
  

for row in grid:
  #if '#' in row:
    #print(row)
  for space in row:
    if space == '#':
      answer += 1

print(answer)