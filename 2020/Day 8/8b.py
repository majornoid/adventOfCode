from os import closerange


def parse_data():
  with open('8input.txt', 'r') as inFile:
    rawData = inFile.read().split()
  data = rawData

  return data



def main():
  acc = 0
  currInstruction = 0
  ranLines = []
  answer = 0
  data = parse_data()
  #print(data)


  #This block finds all lines that run in the original input
  while True:
    command = data[currInstruction]
    value = int(data[currInstruction + 1])
    line = int(currInstruction/2)+1
    #print(str(int(currInstruction/2)+1) + ":" + command + ":" + str(value), end=", ")
    if line not in ranLines:
      ranLines.append(line)
      if command == 'acc':
        #acc += value
        currInstruction += 2
      elif command == 'jmp':
        currInstruction += (value * 2)
      elif command == 'nop':
        currInstruction += 2
    else:
      break
  
  print(ranLines)
  #this initial set of exit lines was manually determined
  exitLines = [*range(629, 634)]

  # this block works from the end to determine which lines can exit the program
  # once a jmp that leads to and exit line is found, it will iterate back until
  # a jmp is found, adding each instruction to exit lines. If that jmp is in
  # ran instructions, it would mark it as the answer since these two paths now
  # overlap
  currInstruction = 0
  while answer == 0:
    print(exitLines)
    currInstruction = 0
    while currInstruction + 1 < len(data):
      command = data[currInstruction]
      value = int(data[currInstruction + 1])
      line = int(currInstruction/2)+1
      #print("testing line: " + str(line))
      if line not in exitLines:
        if command == 'jmp':
          if line + value in exitLines:# or line + value >= 436 and line + value <= 439 or line + value >= 281 and line + value <= 281 or line + value >= 249 and line + value <= 251:
            exitLines.append(line)
            command = ''
            while command != 'jmp':
              currInstruction -= 2
              command = data[currInstruction]
              line = int(currInstruction/2)+1
              if command != 'jmp':
                exitLines.append(line)
              elif line in ranLines:
                print("answer at line: " + str(line))
                answer = line
                break
        elif command == 'nop':
          if line + value in exitLines and line in ranLines:# or line + value >= 436 and line + value <= 439 or line + value >= 281 and line + value <= 281 or line + value >= 249 and line + value <= 251:
            exitLines.append(line)
            answer = line
            break
      currInstruction += 2

  #print(set(ranLines))
  #print(exitLines)

  # this runs through like before, but changes the command on problem line
  currInstruction = 0
  ranLines = []
  while currInstruction + 1 < len(data):
    command = data[currInstruction]
    value = int(data[currInstruction + 1])
    line = int(currInstruction/2)+1
    if line == answer:
      if command == 'jmp':
        command = 'nop'
      else:
        command = 'jmp'
    #print(str(int(currInstruction/2)+1) + ":" + command + ":" + str(value), end=", ")
    if line not in ranLines:
      ranLines.append(line)
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