import sys
sys.setrecursionlimit(2000)

def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

def parse_data():
  with open('9input.txt', 'r') as inFile:
    rawData = inFile.read().strip().split()
  data = rawData
  return data

def fill_in(row, col, grid):
  basinSize = 0
  val = grid[row][col]
  if val != '9' and val != '*':
    grid[row][col] = '*'
    basinSize += 1
    if row - 1 >= 0 and grid[row-1][col] != '9' and grid[row-1][col] != '*':
      #print("Going up from: [" + str(row) + ',' + str(col) + ']')
      basinSize += fill_in(row - 1, col, grid)
    if row + 1 < len(grid) and grid[row+1][col] != '9' and grid[row+1][col] != '*':
      #print("Going down from: [" + str(row) + ',' + str(col) + ']')
      basinSize += fill_in(row + 1, col, grid)
    if col - 1 >= 0 and grid[row][col - 1] != '9' and grid[row][col - 1] != '*':
      #print("Going left from: [" + str(row) + ',' + str(col) + ']')
      basinSize += fill_in(row, col - 1, grid)
    if col + 1 < len(grid[row]) and grid[row][col + 1] != '9' and grid[row][col + 1] != '*':
      #print("Going right from: [" + str(row) + ',' + str(col) + ']')
      basinSize += fill_in(row, col + 1, grid)  
  return basinSize

def main():
  answer = 0
  data = parse_data()
  basinSizes = []
  grid = []

  for row, nums in enumerate(data):
    grid.append([])
    #print(grid)
    #print(grid[0])
    for col, valChar in enumerate(nums):
      grid[row].append(valChar)

  for row, nums in enumerate(grid):
    for col, val in enumerate(nums):
      basinSize = fill_in(row, col, grid)
      if basinSize > 0:
        basinSizes.append(basinSize)
        print("Basin Complete!")

  basinSizes.sort()
  print(basinSizes)
  largest = len(basinSizes)-1
  answer = basinSizes[largest] * basinSizes[largest-1] * basinSizes[largest-2]
  print(answer)

if __name__ == "__main__":
  main()