inFile = open("tinput.txt" , 'r')
numbers = inFile.read().split("\n")
numbers = [i.split(' ') for i in numbers]
#numbers = [i.replace('-',',').split(',') for i in numbers]
answer = 0


def getIndex(row, col):
  return (row*40)+col

def getRowCol(index):
  return [index//40, index%40]

def updateCrt(x, cycles, crt):
  if abs(x - getRowCol(len(cycles))[1]) < 2:
      a, b = getRowCol(len(cycles))
      crt[a][b] = '#'

x = 1
cycles = []
crt = [['.']*40 for i in range(6)]


for command in numbers:
  if command[0] == 'noop':
    updateCrt(x, cycles, crt)
    cycles.append(x)
  elif command[0] == 'addx':
    updateCrt(x, cycles, crt)
    cycles.append(x)
    updateCrt(x, cycles, crt)
    cycles.append(x)
    x += int(command[1])
   
for row in crt:
  print(''.join(row))
