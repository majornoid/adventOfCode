from os import closerange


def parse_data():
  with open('8input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = rawData

  return data



def main():
  acc = 0
  currInstruction = 0
  ranInstructions = []
  answer = 0
  data = parse_data()
  #print(data)

  while True:
    command = data[currInstruction]
    value = int(data[currInstruction + 1])
    print(str(int(currInstruction/2)+1) + ":" + command + ":" + str(value), end=", ")
    if currInstruction not in ranInstructions:
      ranInstructions.append(currInstruction)
      if command == 'acc':
        acc += value
        currInstruction += 2
      elif command == 'jmp':
        currInstruction += (value * 2)
      elif command == 'nop':
        currInstruction += 2
    else:
      break

  answer = acc

  print(answer)

if __name__ == "__main__":
  main()