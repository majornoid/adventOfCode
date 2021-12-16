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

def path_step(row, col, data, answer, count):
  count += data[row][col]
  if count >= answer[0]:
    return
  if row < 99:
    #print("Row up: " + str(row))
    path_step(row+1, col, data, answer, count)
  if col < 99:
    if row == 0:
      print("Col Advanced: " + str(col))
    path_step(row, col+1, data, answer, count)
  elif row >= 99:
    if count < answer[0]:
      print(answer[0])
      answer[0] = count


def main():
  answer = []
  answer.append(100000000)
  data = parse_data()

  path_step(0, 0, data, answer, 0)
  

  print(answer[0])

if __name__ == "__main__":
  main()