def parse_data():
  with open('13input.txt', 'r') as inFile:
    rawData = inFile.read().split("\n\n")
  #print(rawData)
  points = rawData[0].split()
  folds = rawData[1].split('\n')
  points = [i.split(',') for i in points]
  for j in range(len(points)):
    points[j] = [int(i) for i in points[j]]
  folds = [i.replace('fold along ','').split('=') for i in folds]
  return points, folds

def main():
  answer = 0
  points, folds = parse_data()

  #print(points)
  #print(folds)
  for fold in folds: #this will be for part 2 (I have a hunch)
    pass

  fold = folds[0]
  line = int(fold[1])
  if fold[0] == 'x':
    for point in points:
      if point[0] > line:
        point[0] -= 2 * (point[0] - line)
  else:
    for point in points:
      if point[1] > line:
        point[1] -= 2 * (point[1] - line)


  temp = []
  [temp.append(x) for x in points if x not in temp]
  #print(temp)
  points = temp

  answer = len(points)
  print(answer)

if __name__ == "__main__":
  main()