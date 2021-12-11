def parse_data():
  with open('1input.txt', 'r') as inFile:
    rawData = inFile.read().replace("\n", "")
  data = rawData
  return data

def main():
  answer = 0
  floor = 0
  data = parse_data()
  for i in range(len(data)):
    if data[i] == '(':
      floor += 1
    elif data[i] == ')':
      floor -= 1
    if floor < 0:
      answer = i + 1
      break
     
  print(answer)

if __name__ == "__main__":
  main()