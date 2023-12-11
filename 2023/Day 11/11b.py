import copy

def solve(x):
  inFile = open("input.txt" , 'r')
  grid: list = inFile.read().split("\n")

  galaxies = []
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "#":
        galaxies.append([i, j])

  originalGalaxies = copy.deepcopy(galaxies)

  blankRows = []
  for i in range(len(grid)):
    if "#" not in grid[i]:
      blankRows.append(i)

  for j in range(len(galaxies)):
    for i in blankRows:
      if originalGalaxies[j][0] > i:
        galaxies[j][0] += x

  blankCols = []
  for i in range(len(grid[0])):
    empty = True
    for row in grid:
      if row[i] == "#":
        empty = False
        break
    if empty:
      blankCols.append(i)

  for j in range(len(galaxies)):    
    for i in blankCols:
      if originalGalaxies[j][1] > i:
        galaxies[j][1] += x

  answer = 0
  for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
      answer += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
  return answer

print(f"Part 1: {solve(1)}")
print(f"Part 2: {solve(999999)}")


      
  
  
  
  
