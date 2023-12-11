inFile = open("input.txt" , 'r')
grid = inFile.read().split("\n")

print(len(grid))
i = 0
while i < len(grid):
  if "#" not in grid[i]:
    grid.insert(i, "." * len(grid[0]))
    i += 1
  i += 1
  
print(len(grid))
print(len(grid[0]))
i = 0
while i < len(grid[0]):
  empty = True
  for row in grid:
    if row[i] == "#":
      empty = False
      break
  if empty:
    for j in range(len(grid)):
      grid[j] = grid[j][:i] + "." + grid[j][i:]
    i += 1
  i += 1
print(len(grid[0]))

galaxies = []
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == "#":
      galaxies.append((i, j))

answer = 0
for i in range(len(galaxies)):
  for j in range(i + 1, len(galaxies)):
    answer += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    
print(answer)


      
  
  
  
  
