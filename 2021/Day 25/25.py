import copy

def parse_data():
  with open('25input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = []
  for i in range(len(rawData)):
    row = rawData[i]
    data.append([])
    for char in row:
      data[i].append(char)
  return data
   
def move_south(grid):
  moved = False
  newGrid = copy.deepcopy(grid)
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == 'v':
        nextRow = (row + 1) if (row + 1) < len(grid) else 0
        if grid[nextRow][col] == '.':
          #print("Moving south from " + str((row, col)) + " to " + str((nextRow, col)))
          moved = True
          newGrid[row][col] = '.'
          newGrid[nextRow][col] = 'v'
  return newGrid, moved

def move_east(grid):
  moved = False
  newGrid = copy.deepcopy(grid)
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == '>':
        nextCol = (col + 1) if (col + 1) < len(grid[row]) else 0
        if grid[row][nextCol] == '.':
          #print("Moving east from " + str((row, col)) + " to " + str((row, nextCol)))
          moved = True
          newGrid[row][col] = '.'
          newGrid[row][nextCol] = '>'
  return newGrid, moved

def print_grid(grid):
  for row in grid:
    for col in row:
      print(col, end='')
    print()
  print()

def main():
  answer = 0
  moved = True
  step = 0
  grid = parse_data()
  print_grid(grid)

  while moved:
    step += 1

    grid, movedS = move_east(grid)
    grid, movedE = move_south(grid)

    #print_grid(grid)
    moved = (movedS or movedE)

  print_grid(grid)
  answer = step
  print(answer)
  
if __name__ == "__main__":
  main()