inFile = open("tinput.txt" , 'r')
numbers = inFile.read().split("\n")
numbers = [i.split(' ') for i in numbers]
#numbers = [i.replace('-',',').split(',') for i in numbers]
answer = 0

x = 1
cycles = [x]

for command in numbers:
  if command[0] == 'noop':
    cycles.append(x)
  elif command[0] == 'addx':
    cycles.append(x)
    cycles.append(x)
    x += int(command[1])

print(cycles[20]*20 + cycles[60]*60 + cycles[100]*100 + cycles[140]*140 + cycles[180]*180 + cycles[220]*220)