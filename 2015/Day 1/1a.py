def parse_data():
  with open('1input.txt', 'r') as inFile:
    rawData = inFile.read()
  data = rawData
  return data

def main():
  answer = 0
  floor = 0
  data = parse_data()
  for char in data:
    if char == '(':
      floor += 1
    elif char == ')':
      floor -= 1
  print(floor)

if __name__ == "__main__":
  main()