inFile = open("2input.txt" , 'r')
commands = inFile.read().split()
forward = 0
depth = 0
print(len(commands))

for x in range(0, len(commands)):
  if x % 2 == 1: # keywords and amounts alternate
    if commands[x-1] == "forward":
      forward += int(commands[x])
    elif commands[x-1] == "down":
      depth += int(commands[x])
    elif commands[x-1] == "up":
      depth -= int(commands[x])

print(forward*depth)