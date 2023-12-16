inFile = open("input.txt" , 'r')
grid = inFile.read().split("\n")
#numbers = [i.split(' ') for i in numbers]
answer = 0
touched = set()
touchedD = set()

def move(row, col, direction, grid, touched, touchedD):
  touched.add((row, col))
  touchedD.add((row, col, direction))
  newPoints = []
  if grid[row][col] == ".":
    if direction == "u" and row > 0:
      newPoints.append((row - 1, col, "u"))
    elif direction == "d" and row < len(grid) - 1:
      newPoints.append((row + 1, col, "d"))
    elif direction == "l" and col > 0:
      newPoints.append((row, col - 1, "l"))
    elif direction == "r" and col < len(grid[0]) - 1:
      newPoints.append((row, col + 1, "r"))
  elif grid[row][col] == "|":
    if direction == "u" and row > 0:
      newPoints.append((row - 1, col, "u"))
    elif direction == "d" and row < len(grid) - 1:
      newPoints.append((row + 1, col, "d"))
    elif direction == "l" or direction == "r":
      if row > 0:
        newPoints.append((row - 1, col, "u"))
      if row < len(grid) - 1:
        newPoints.append((row + 1, col, "d"))
  elif grid[row][col] == "-":
    if direction == "l" and col > 0:
      newPoints.append((row, col - 1, "l"))
    elif direction == "r" and col < len(grid[0]) - 1:
      newPoints.append((row, col + 1, "r"))
    elif direction == "u" or direction == "d":
      if col > 0:
        newPoints.append((row, col - 1, "l"))
      if col < len(grid[0]) - 1:
        newPoints.append((row, col + 1, "r"))
  elif grid[row][col] == "/":
    if direction == "u" and col < len(grid[0]) - 1:
      newPoints.append((row, col + 1, "r"))
    elif direction == "d" and col > 0:
      newPoints.append((row, col - 1, "l"))
    elif direction == "l" and row < len(grid) - 1:
      newPoints.append((row + 1, col, "d"))
    elif direction == "r" and row > 0:
      newPoints.append((row - 1, col, "u"))
  elif grid[row][col] == "\\":
    if direction == "u" and col > 0:
      newPoints.append((row, col - 1, "l"))
    elif direction == "d" and col < len(grid[0]) - 1:
      newPoints.append((row, col + 1, "r"))
    elif direction == "l" and row > 0:
      newPoints.append((row - 1, col, "u"))
    elif direction == "r" and row < len(grid) - 1:
      newPoints.append((row + 1, col, "d"))
  return newPoints
      
  
currentPoints = [(0, 0, "r")]

while len(currentPoints) > 0:
  newPoints = []
  for point in currentPoints:
    if point not in touchedD:
      newPoints += move(point[0], point[1], point[2], grid, touched, touchedD)
  currentPoints = newPoints

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if (i, j) not in touched:
      print(".", end = "")
    else:
      print("#", end = "")
  print()

print(len(touched))