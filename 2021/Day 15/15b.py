import sys
sys.setrecursionlimit(1200)

def char_range(c1, c2):
  for c in range(ord(c1), ord(c2)+1):
      yield chr(c)

def parse_data():
  with open('15input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = []
  for line in rawData:
    temp = []
    for num in line:
      temp.append(int(num))
    data.append(temp)
  #print(data)
  return data



answer = 10000

def path_step(row, col, data, count, shortestPaths, depth):
  global answer
  count += data[row][col]
  depth += 1
  if count < shortestPaths[(row, col)] and depth < 1200:
    #print(row,col)
    shortestPaths[(row, col)] = count
    remaining = (499 - row) + (499 - col)
    if answer < count + remaining:
      return

    if row < 499:
      #print("Going Down")
      path_step(row+1, col, data, count, shortestPaths, depth)
    if col < 499:
      #print("Going Right")
      path_step(row, col+1, data, count, shortestPaths, depth)

    if row > 0:
      #print("Going Up")
      path_step(row-1, col, data, count, shortestPaths, depth)

    if col > 0:
      #print("Going Left")  
      path_step(row, col-1, data, count, shortestPaths, depth)

    if row >= 499 and col >= 499:
      print(count)
      if count < answer:
        answer = count
  else:
    #print("inelligible")
    if depth >= 1200:
      print("Depth Exceeded")


def main():
  global answer
  data = parse_data()
  gridFactor = 5
  newGrids = [] * ((gridFactor-1)*2)
  tempGrid = []
  tempRow = []
  shortestPaths = {}


  
  for x in range(1, ((gridFactor-1)*2)+1):
    tempGrid = []
    for row in data:
      tempRow = [i+x for i in row]
      tempGrid.append(tempRow)
    for row in range(100):
      for col in range(100):
        if tempGrid[row][col] > 9:
          tempGrid[row][col] %= 9
    #print(tempGrid)
    newGrids.append(tempGrid)

  #debug block
  textfile = open("15grids.txt", "w")
  print("Rows: " + str(len(data)))
  count = 0
  for i in range(len(newGrids)):
    print("\n" + str(i))
    for row in newGrids[i]:
      if count % 10 == 0:
        print("Cols: " + str(len(row)))
      for num in row:
        textfile.write(str(num))
      textfile.write("\n")
      count += 1
    textfile.write("\n")
  textfile.close()

  for i in range((gridFactor-1)*2):
    if i < gridFactor - 1:
      print("Growing from row 1")
      for row in range(100):
        data.append(newGrids[i][row])
#      for row in range(100):
        data[row].extend(newGrids[i][row])
    if i >= gridFactor - 1:
      print("Extending")
      offset = 100
      grid = i - 3
      for _ in range(gridFactor-1):
        print("Extending chunk from " + str(offset) + " to " + str(offset+99))
        print("Adding from grid: " + str(grid))
        print(len(data[offset]))
        print(len(newGrids[grid][0]))
        for row in range(offset, offset+100):
          data[row].extend(newGrids[grid][row-offset])
        print(len(data[offset]))
        grid += 1
        offset += 100

#debug block
  textfile = open("15grids2.txt", "w")
  print("Rows: " + str(len(data)))
  count = 0
  for i in range(len(newGrids)):
    print("\n" + str(i))
    for row in newGrids[i]:
      if count % 10 == 0:
        print("Cols: " + str(len(row)))
      for num in row:
        textfile.write(str(num))
      textfile.write("\n")
      count += 1
    textfile.write("\n")
  textfile.close()  

#debug block
  textfile = open("15bData.txt", "w")
  print("Rows: " + str(len(data)))
  count = 0
  for row in data:
    if count % 100 == 0:
      print("Cols: " + str(len(row)))
    for num in row:
      textfile.write(str(num))
    textfile.write("\n")
    count += 1
  textfile.close()  

  for row in range(100*gridFactor):
    for col in range(100*gridFactor):
      shortestPaths[(row, col)] = 100000

  path_step(0, 0, data, -3, shortestPaths, 1)
  
  #debug block
  textfile = open("15answer.txt", "w")
  for element in shortestPaths:
    textfile.write("(" + str(element) + "): " + str(shortestPaths[element]) + "\n")
  textfile.close()  

  print(answer)

if __name__ == "__main__":
  main()