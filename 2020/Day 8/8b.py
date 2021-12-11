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

  while currInstruction < len(data):
    command = data[currInstruction]
    value = int(data[currInstruction + 1])
    line = int(currInstruction/2)+1
    #print(str(line) + ":" + command + ":" + str(value), end=", ")
    #if currInstruction not in ranInstructions:
    #  ranInstructions.append(currInstruction)
    if command == 'acc':
      acc += value
      #currInstruction += 2
    elif command == 'jmp':
      if line + value >= 435 and line + value <= 435:# or line + value >= 436 and line + value <= 439 or line + value >= 281 and line + value <= 281 or line + value >= 249 and line + value <= 251:
        print("jmp" + str(line))
      #currInstruction += (value * 2)
    elif command == 'nop':
      if line + value >= 435 and line + value <= 435:# or line + value >= 436 and line + value <= 439 or line + value >= 281 and line + value <= 281 or line + value >= 249 and line + value <= 251:
        print("nop" + str(line))
      #currInstruction += 2
    currInstruction += 2
    #else:
    #  break


  answer = acc

  print(answer)

if __name__ == "__main__":
  main()