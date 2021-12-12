def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

def parse_data():
  with open('11input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = rawData
  return data

def flash(row, col, grid):
  flashes = 0
  val = grid[row][col]
  #print(val)
  if val != 0:
    #print("Not Zero")
    grid[row][col] += 1
    if grid[row][col] > 9:
      flashes += 1
      grid[row][col] = 0

      above = 0
      below = 0
      left  = 0
      right = 0
      if row - 1 >= 0:
        above = 1
        flashes += flash(row - 1, col, grid)
      if row + 1 < len(grid):
        below = 1
        flashes += flash(row + 1, col, grid)
      if col - 1 >= 0 and grid[row][col - 1] != '9' and grid[row][col - 1] != '*':
        left = 1
        flashes += flash(row, col - 1, grid)
      if col + 1 < len(grid[row]) and grid[row][col + 1] != '9' and grid[row][col + 1] != '*':
        right = 1
        flashes += flash(row, col + 1, grid)
      
      if above and left:
        flashes += flash(row - 1, col - 1, grid)
      if above and right: 
        flashes += flash(row - 1, col + 1, grid)
      if below and left:
        flashes += flash(row + 1, col - 1, grid)
      if below and right: 
        flashes += flash(row + 1, col + 1, grid)
  #print(flashes)
  return flashes
    

def main():
  answer = 0
  data = parse_data()
  grid = []
  flashes = 0
  steps = 100

  for row, nums in enumerate(data):
    grid.append([])
    for col, valChar in enumerate(nums):
      grid[row].append(int(valChar))

  #print(grid)

  for _ in range(steps):
    for row, nums in enumerate(grid):
      for col, val in enumerate(nums):
        grid[row][col] += 1

    for row, nums in enumerate(grid):
      for col, val in enumerate(nums):
        if grid[row][col] > 9:
          flashes += flash(row, col, grid)

  answer = flashes
  print(answer)

if __name__ == "__main__":
  main()